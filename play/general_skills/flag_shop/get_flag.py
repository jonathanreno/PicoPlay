#!/usr/bin/env/python3

with open("notes.txt", "r") as file:
    with open("twos.txt", "w") as twos:
        for line in file.read().split():

            print(hex(int(line)))