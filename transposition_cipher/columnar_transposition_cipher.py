# -*- coding: utf-8 -*-
"""
@author: dasaw
"""

import math 

def columnar_cipher_encrypt(message,key):
    cipher=""
    msg_len = len(message)
    msg_list = list(message)
    key_list = sorted(list(key))
    key_len = len(key)
    
    colns = key_len 
    rows = int(math.ceil(msg_len/colns))
    
    null_space = int((rows*colns)-msg_len)
    msg_list.extend('z'*null_space)
    
    encrypt_matrix = [msg_list[i:i+colns] for i in range(0,len(msg_list),colns)]
    
    index = 0
    for j in range(colns):
        current_i = key.index(key_list[index])
        cipher+= ''.join([r[current_i] for r in encrypt_matrix])
        index= index+1
        
    return cipher


key = input("Enter the key: ") 
message = input("Enter the message: ")
encrypt_text = columnar_cipher_encrypt(message,key)
print('Ecnrypted Text: ' + encrypt_text)
        