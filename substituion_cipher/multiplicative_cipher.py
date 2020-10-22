# -*- coding: utf-8 -*-
"""
@author: darshasawa
"""

# key domain for any multiplicative cipher : 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25.

key_domain = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

def multi_cipher_encrypt(text,value):
    cipher = ''
    for char in text:
        char = char.lower()
        if char == ' ':
            cipher+=char
        else:
            cipher += chr((((ord(char)-97) * value)%26)+97)
    return cipher
    

text = input("Enter string: ")
shift_value = int(input("Enter shift value: "))
if shift_value in key_domain:
    cipher_encrypted_text = multi_cipher_encrypt(text,shift_value)
    print(cipher_encrypted_text)
    
else:
    print("\nThe key entered doesn't exists in domain")