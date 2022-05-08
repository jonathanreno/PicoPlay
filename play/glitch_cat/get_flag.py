#!/usr/bin/env/python3

"""
python -c 'with open("tflag.txt", "r") as file: with open("tmpflag.txt", "w") as flag: flag.write("".join(line.strip() for line in file))' 
"""

with open("tflag.txt", "r") as file:
    with open("flag.txt", "w") as flag:
        flag_str = "".join(line.strip() for line in file)
        flag_str = flag_str.replace("'", "")
        flag.write(flag_str)
        