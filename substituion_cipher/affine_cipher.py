# -*- coding: utf-8 -*-
"""
@author: darshasawa
"""

key_domain = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

def affine_encrypt(text,key1,key2):
    cipher = ''
    for char in text:
        char = char.lower()
        if char == ' ':
            cipher+=char
        else:
            cipher += chr(((((ord(char)-97) * key1)+key2)%26)+97)
    return cipher
    

text = input("Enter string: ")
key1 = int(input("Enter Key 1 : "))
key2 = int(input("Enter Key 2 : "))
if key1 in key_domain:
    cipher_encrypted_text = affine_encrypt(text,key1,key2)
    print(cipher_encrypted_text)
    
else:
    print("\nThe key 1 entered doesn't exists in domain")