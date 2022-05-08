#!/usr/bin/env/python3

with open("flag.txt", "r") as pieces:
    with open("complete.txt", "w") as flag:
        x = ''.join(line.strip() for line in pieces)
        flag.write(x)
            
            