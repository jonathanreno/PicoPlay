#!/usr/bin/env/python3

with open("tmp.txt", "r") as file:
    with open("flag.txt", "w") as flag:
        for i in file:
            if i.startswith("pico"):
                flag.write(i)