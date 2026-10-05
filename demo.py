from jsonl_seek import build_index,get_record
import tempfile,pathlib,json
with tempfile.TemporaryDirectory()as t:
 p=pathlib.Path(t)/'sample.jsonl';p.write_text('{"id":1}\n{"id":2}\n');i=build_index(p);v=get_record(p,i,1);assert v=={'id':2};print(json.dumps({'index':i,'record':v}))
