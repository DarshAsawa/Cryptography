# -*- coding: utf-8 -*-
"""
@author: dasaw
"""

def encrypt (key,message,encrypted) :
    encrypted_text = []
    encryptedText = "" 
    for i in range(3):
        for j in range(1):
                encrypted [i] [j]
                for k in range(3):
                    encrypted[i][j] += (key[i][k] * message[k][j])
                    encrypted[i][j] = encrypted[i][j]%26
        encrypted_text.append(chr(encrypted [i][0]+65))
    for element in encrypted_text:
        encryptedText+=element
    return encryptedText

key = input("Enter the key: ")
key = key. upper()
message = input("Enter the message: ")
message = message.upper()
key_matrix = [[0]*3 for i in range(3)]
message_matrix = [[0] for i in range(3)]
cipher_matrix = [[0] for i in range(3)]

k=0
for x in range(3):
    for y in range(3):
        key_matrix[x][y] = ord(key[k]) % 65
        k+=1
for i in range(3):
    message_matrix[i][0] = ord(message[i]) % 65


encrypted_text = encrypt(key_matrix,message_matrix,cipher_matrix)
print("\nEncrypted Text: "+ encrypted_text)