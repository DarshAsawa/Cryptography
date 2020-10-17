# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 21:54:07 2020

@author: darshasawa
"""

# Additive Cipher is also known as Caesar Cipher/Shift Cipher.

def caesar_cipher_encrypt(text,value):
    cipher = ''
    for char in text:
        if char == ' ':
            cipher+=char
        elif char.isupper():
            cipher += chr((ord(char) + value - 65)%26 +65)
        else: 
            cipher += chr((ord(char) + value - 97)%26 + 97)
            
    return cipher
    
def caesar_cipher_decrypt(cipher,value):
    plaintext = ''
    for char in cipher:
        if char == ' ':
            plaintext+=char
        elif char.isupper():
            plaintext+=chr((ord(char) - value - 65)%26 +65)
        else: 
            plaintext+=chr((ord(char) - value - 97)%26 + 97)
            
    return plaintext

text = input("Enter string: ")
shift_value = int(input("Enter shift value: "))

cipher_encrypted_text = caesar_cipher_encrypt(text,shift_value)
print(cipher_encrypted_text)

cipher_decrypted_text = caesar_cipher_decrypt(cipher_encrypted_text,shift_value)
print(cipher_decrypted_text) 