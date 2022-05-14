#!/usr/bin/env/python3

a = """114
114
114
111
99
107
110
114
110
48
49
49
51
114"""

for i in a.split():
    print(chr(int(i)), end='')