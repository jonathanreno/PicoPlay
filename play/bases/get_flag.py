#!/usr/bin/env/python3

with open("tmp.txt", "r") as file:
    with open("flag.txt", "w") as flag:
        contents = file.read()
        flag_str = "picoCTF{" + contents + "}"
        flag.write(flag_str)
