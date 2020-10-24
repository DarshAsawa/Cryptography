#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: darshasawa
"""


def encrypt(plaintext,key):
    ciphertext = ""
    key_length = len(key)
    for i in range(len(plaintext)):
        value =(ord(plaintext[i])+ord(key[(i%key_length)]))%26
        ciphertext+=chr(value+65)
    return ciphertext
def decrypt(ciphertext,key):
    plaintext = ''
    key_length = len(key)
    for i in range(len(ciphertext)):
        value =(ord(ciphertext[i]) - ord(key[(i%key_length)])+26)%26
        plaintext+=chr(value+65)
    return plaintext

phrase = input("Please enter the phrase: ")
key = input("Enter the key: ")
phrase = phrase.upper()
key=key.upper()

encryptedText = encrypt(phrase,key)
print("\n"+encryptedText)
print("\n"+decrypt(encryptedText,key))




