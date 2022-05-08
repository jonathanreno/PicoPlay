"""
Caesar Encrypt Method
"""

def caesar_encrypt(text):
    result = ""

    # Go through each character of the text in this for loop
    for i in range(len(text)):

        # Obtain the ASCII value using ord
        char_position = ord(text[i])

        # Add 3 to the position, as caesar does
        new_char_position = char_position + 3

        new_char_position = new_char_position % 123

        # Convert ASCII value to character and concatenate it to final result
        result = result + chr(new_char_position)

        print(result)
    return result



######################################################

""" 
Caesar Decrypt Method
"""

def caesar_decrypt(cipher_text):
    result = ""

    # Go through each character of the text in this for loop
    for i in range(len(cipher_text)):

        # Obtain the ASCII value using ord
        char_position = ord(cipher_text[i])

        # Substract 3 to the position, to get back original position
        new_char_position = char_position - 3

        new_char_position = new_char_position % 123

        # Convert ASCII value to character and concatenate it to final result
        result = result + chr(new_char_position)

        print(result)
    return result


e = caesar_encrypt("Hello")

d = caesar_decrypt(e)

print(e)

print(d)