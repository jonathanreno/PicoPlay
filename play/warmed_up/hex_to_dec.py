#!/usr/bn/env/python3 

# Convert hex to dec

tmp = '0x3D'

h = tmp.replace('0x', '')

d = int(h, 16)

print(d)