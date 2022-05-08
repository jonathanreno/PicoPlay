#!/usr/bin/env/python3

"""
Convert binary to hexadecimal
"""

b = '1111'

d = int(b, 2)

h = hex(d).replace('0x', '')

print(h)