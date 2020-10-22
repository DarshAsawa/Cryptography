# -*- coding: utf-8 -*-
"""
@author: dasaw
"""
def autokey_cipher(plaintext,key):
    cipher = ''
    plaintext = plaintext.lower()
    key = key.lower()
    for letter in plaintext:
        if letter == ' ':
            cipher+= ' '
        else:
            cipher+=chr(((ord(letter) -97) + (ord(key) - 97)) % 26 + 97)
            key = letter
    return cipher

plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")
print(autokey_cipher(plaintext,key))
            
