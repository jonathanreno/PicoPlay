#!/usr/bin/env/python3

"""
Syntax : { } .format(value)

Parameters : 
(value) : Can be an integer, floating point numeric constant, string, characters or even variables.
Returntype : Returns a formatted string with the value passed as parameter in the placeholder position. 
"""

number = 15

binary_number = int("{0:08b}".format(number))

flipped_binary_number = ~ binary_number

flipped_binary_number = flipped_binary_number + 1

str_twos_complement = str(flipped_binary_number)

twos_complement = int(str_twos_complement, 2)

print(twos_complement) 
