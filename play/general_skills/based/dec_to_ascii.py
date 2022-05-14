#!/usr/bin/env/python3

from base64 import encode


b = "143 150 141 151 162"

for field in b.split():
    d = int(field, 10)
    h = hex(int(d))
    h = h.replace("0x", "")
    print(chr(int(h, 16)))


    