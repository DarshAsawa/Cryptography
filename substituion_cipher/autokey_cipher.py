# -*- coding: utf-8 -*-
"""
@author: dasaw
"""
def autokey_encrypt(plaintext,key):
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

def autokey_decrypt(ciphertext,key):
    plaintext = ''
    ciphertext = ciphertext.lower()
    key = key.lower()
    for letter in ciphertext:
        letter_val = ord(letter)
        key_val = ord(key)
        if letter == ' ':
            plaintext+=' '
        elif letter_val >= key_val:
            plaintext_value = chr(((letter_val - 97) - (key_val - 97)) % 26 + 97)
            plaintext+=plaintext_value
            key = plaintext_value
        else:
            plaintext_value = chr(((letter_val - 97) - (key_val - 97) + 26) % 26 + 97)
            plaintext+=plaintext_value
            key = plaintext_value
    return plaintext

plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

cipher_text = autokey_encrypt(plaintext,key) 
print("Encrypted Text: ", cipher_text)

decrypt_text = autokey_decrypt(cipher_text,key)
print("Decrypted Text: ", decrypt_text)
            
