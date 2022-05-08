#!/usr/bin/env/python3

with open("ascci_nums.txt", "r") as file:
    with open("vals.txt", "w") as vals:
        data = file.readlines()
        for line in data:
            word = line.split()
            #print(word)
            for i in word:
                i = ord(chr(int(i)))
                vals.write(chr(i))