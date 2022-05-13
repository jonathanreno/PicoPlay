#!/usr/bin/env/python3

from base64 import encode


encoded = input("enter here: ")

encoded_arr = encoded.split()

for field in encoded_arr:
    f = f'0b{field}' 
    print(chr(int(f, 2)))
    