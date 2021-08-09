import base64
import sys

if len(sys.argv) == 2:
  data = None
  with open(sys.argv[1], 'r') as file:
      data = file.read().replace('\n', '')
  
  with open(sys.argv[1][:-3] + '.exe', "wb") as fh:
    fh.write(base64.decodebytes(bytes(data, 'utf8')))
  
