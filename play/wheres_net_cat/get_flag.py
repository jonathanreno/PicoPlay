#!/usr/bin/env/python3

with open("tmp.txt", "r") as file:
    with open("flag.txt", "w") as flag:
        for line in file:
            if line.startswith("pico"):
                flag.write(line)
                