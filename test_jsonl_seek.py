import unittest,tempfile,pathlib,copy
from jsonl_seek import build_index,get_record
class Tests(unittest.TestCase):
 def file(self,t,raw):p=pathlib.Path(t)/'data.jsonl';p.write_bytes(raw);return p
 def test_utf8_crlf_no_final_newline(self):
  with tempfile.TemporaryDirectory()as t:
   p=self.file(t,'{"v":"é"}\r\n42'.encode());j=build_index(p);self.assertEqual(j['offsets'],[0,12]);self.assertEqual(get_record(p,j,1),42)
 def test_stale_same_length(self):
  with tempfile.TemporaryDirectory()as t:
   p=self.file(t,b'1\n2\n');j=build_index(p);p.write_bytes(b'1\n3\n')
   with self.assertRaisesRegex(ValueError,'match'):get_record(p,j,1)
 def test_tampered_offsets(self):
  with tempfile.TemporaryDirectory()as t:
   p=self.file(t,b'1\n2\n');j=build_index(p);j['offsets']=[2,2]
   with self.assertRaises(ValueError):get_record(p,j,0)
 def test_blank_and_nonfinite(self):
  for raw in [b'1\n\n',b'NaN\n',b'1e400\n',b'\xff\n',b'{broken}\n']:
   with tempfile.TemporaryDirectory()as t:
    with self.assertRaises(ValueError):build_index(self.file(t,raw))
 def test_bound(self):
  with tempfile.TemporaryDirectory()as t:
   with self.assertRaises(ValueError):build_index(self.file(t,b'"'+b'x'*1048576+b'"'))
 def test_out_of_range(self):
  with tempfile.TemporaryDirectory()as t:
   p=self.file(t,b'1\n');j=build_index(p)
   with self.assertRaises(ValueError):get_record(p,j,1)
 def test_empty(self):
  with tempfile.TemporaryDirectory()as t:self.assertEqual(build_index(self.file(t,b''))['offsets'],[])
