# -*- coding: utf-8 -*-
"""
@author: dasaw
"""

key=input("Enter key : ")
key=key.replace(" ", "")
key=key.upper()
def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    
result=list()
for c in key: 
    if c not in result:
        if c=='J':
            result.append('I')
        else:
            result.append(c)
flag=0
for i in range(65,91): 
    if chr(i) not in result:
        if i==73 and chr(74) not in result:
            result.append("I")
            flag=1
        elif flag==0 and i==73 or i==74:
            pass    
        else:
            result.append(chr(i))
k=0
my_matrix=matrix(5,5,0) 
for i in range(0,5): 
    for j in range(0,5):
        my_matrix[i][j]=result[k]
        k+=1

def locindex(c): 
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt(plaintext):  
    plaintext=plaintext.upper()
    plaintext=plaintext.replace(" ", "")             
    i=0
    encrypted_text = '' 
    for s in range(0,len(plaintext)+1,2):
        if s<len(plaintext)-1:
            if plaintext[s]==plaintext[s+1]:
                plaintext=plaintext[:s+1]+'X'+plaintext[s+1:]
    if len(plaintext)%2!=0:
        plaintext=plaintext[:]+'X'
    while i<len(plaintext):
        loc=list()
        loc=locindex(plaintext[i])
        loc1=list()
        loc1=locindex(plaintext[i+1])
        if loc[1]==loc1[1]:
            encrypted_text += my_matrix[(loc[0]+1)%5][loc[1]]
            encrypted_text += my_matrix[(loc1[0]+1)%5][loc1[1]]
        elif loc[0]==loc1[0]:
            encrypted_text += my_matrix[loc[0]][(loc[1]+1)%5]
            encrypted_text += my_matrix[loc1[0]][(loc1[1]+1)%5]
            
        else:
            encrypted_text += my_matrix[loc[0]][loc1[1]]
            encrypted_text += my_matrix[loc1[0]][loc[1]]
        i=i+2        
    return encrypted_text         

   
def decrypt(ciphertext):  
    plaintext = ''
    ciphertext=ciphertext.upper()
    ciphertext=ciphertext.replace(" ", "")
    i=0
    while i<len(ciphertext):
        loc=list()
        loc=locindex(ciphertext[i])
        loc1=list()
        loc1=locindex(ciphertext[i+1])
        if loc[1]==loc1[1]:
            plaintext+=my_matrix[(loc[0]-1)%5][loc[1]]
            plaintext+=my_matrix[(loc1[0]-1)%5][loc1[1]]
        elif loc[0]==loc1[0]:
            plaintext+=my_matrix[loc[0]][(loc[1]-1)%5]
            plaintext+=my_matrix[loc1[0]][(loc1[1]-1)%5]
        else:
            plaintext+=my_matrix[loc[0]][loc1[1]]
            plaintext+=my_matrix[loc1[0]][loc[1]]
        i=i+2
    return plaintext        

plaintext = input("Enter the plaintext: ")
encrypted_text = encrypt(plaintext) 
print("\nCipher text: ",encrypted_text.lower())

decrypted_text = decrypt(encrypted_text)
print("\nPlain text: ",decrypted_text.lower())
