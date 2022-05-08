#!/usr/bin/env/python3

"""
Convert hexadecimal to binary
"""

tmp = '0xf'

h = tmp.replace('0x', '')

d = int(h, 16)

b = str(bin(d)).replace('0b', '')

print(b)

