"""Create a byte-offset JSONL index and verify content before random access."""
import argparse,json,hashlib,pathlib,math
LIMIT=1048576
def value(raw):
    def reject(x):raise ValueError('non-finite JSON number: '+x)
    def number(text):
        x=float(text)
        if not math.isfinite(x):raise ValueError('JSON float outside finite range')
        return x
    return json.loads(raw.decode('utf-8'),parse_constant=reject,parse_float=number)

def build_index(source):
    h=hashlib.sha256();offsets=[];offset=0
    with pathlib.Path(source).open('rb')as f:
        while True:
            raw=f.readline(LIMIT+1)
            if not raw:break
            if len(raw)>LIMIT:raise ValueError('line exceeds 1 MiB')
            try:value(raw)
            except (ValueError,UnicodeError,RecursionError)as e:raise ValueError(f'line {len(offsets)+1}: {e}')
            offsets.append(offset);h.update(raw);offset+=len(raw)
            if len(offsets)>1000000:raise ValueError('one million record limit exceeded')
    return {'version':1,'sha256':h.hexdigest(),'size':offset,'offsets':offsets}

def get_record(source,index,record):
    if type(record)is not int or record<0:raise ValueError('record must be a zero-based nonnegative integer')
    if not isinstance(index,dict)or set(index)!={'version','sha256','size','offsets'}or index.get('version')!=1:raise ValueError('invalid index')
    # Rebuild offsets as well as the digest: a modified index cannot silently select another record.
    actual=build_index(source)
    if index!=actual:raise ValueError('index does not match current source bytes and offsets')
    if record>=len(index['offsets']):raise ValueError('record out of range')
    with pathlib.Path(source).open('rb')as f:f.seek(index['offsets'][record]);return value(f.readline(LIMIT+1))

def main():
    p=argparse.ArgumentParser(description=__doc__);s=p.add_subparsers(dest='command',required=True);b=s.add_parser('index');b.add_argument('source');b.add_argument('output');g=s.add_parser('get');g.add_argument('source');g.add_argument('index');g.add_argument('record',type=int);a=p.parse_args()
    try:
        if a.command=='index':
            result=build_index(a.source)
            if pathlib.Path(a.source).resolve()==pathlib.Path(a.output).resolve():raise ValueError('index output cannot be the source')
            with pathlib.Path(a.output).open('x',encoding='utf-8')as f:json.dump(result,f)
            print(json.dumps({'records':len(result['offsets']),'sha256':result['sha256']}))
        else:
            with pathlib.Path(a.index).open('rb')as f:raw=f.read(20_000_001)
            if len(raw)>20_000_000:raise ValueError('index exceeds 20 MB')
            print(json.dumps(get_record(a.source,json.loads(raw),a.record),ensure_ascii=True))
        return 0
    except (ValueError,OSError,UnicodeError,RecursionError,TypeError)as e:print(json.dumps({'error':str(e)}));return 2
if __name__=='__main__':raise SystemExit(main())
