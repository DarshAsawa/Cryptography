# -*- coding: utf-8 -*-
"""
@author: dasaw
"""

def encrypt_railfence(message):
    message = message.lower()
    encrypted_text = message[0::2] + message[1::2]
    return encrypted_text

def decrypt_railfence(encrypted_text):
    encrypted_text = encrypted_text.lower()
    encrypted_length = len(encrypted_text)
    decrypted_text= "" 
    if encrypted_length%2==0:
        mid = encrypted_length // 2
        first_half = encrypted_text[:mid]
        second_half = encrypted_text[mid:]
        for i in range(mid):
            decrypted_text += first_half[i] + second_half[i]
        
    else:
        mid = encrypted_length // 2
        first_half = encrypted_text[:mid+1]
        second_half = encrypted_text[mid+1:]
        for i in range(len(second_half)):
            decrypted_text += first_half[i] + second_half[i]
        decrypted_text += first_half[len(first_half)-1]
    return decrypted_text
            
message = input("Enter the message: ")
encrypted_text = encrypt_railfence(message)
print("Encrypted Text: " + encrypted_text)
print("Decrypted Text: "+ decrypt_railfence(encrypted_text))           