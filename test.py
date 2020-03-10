#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zlib, base64

file = open('exemple1.txt', 'r')
text = file.read()
file.close()
print("Uncompressed Text: \n" + text)
# encoding the text
code = base64.b64encode(zlib.compress(text.encode('utf-8'), 9))
code = code.decode('utf-8')
f = open('output.txt', 'w')
f.write(code)
f.close()
print("Compressed text: \n" + code)
# decode the encoded text
decoded_txt = zlib.decompress(base64.b64decode(code)).decode('utf-8')

#print the text in a file to ensure the text has not been altered
f = open('output2.txt', 'w')
f.write(decoded_txt)
f.close()
print(decoded_txt)