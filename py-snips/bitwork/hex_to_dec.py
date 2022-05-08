#!/usr/bin/env/python3

"""
Convert hexadecimal to decimal
"""

tmp = '0xf'

h = tmp.replace('0x', '')

d = int(h, 16)

print(d)