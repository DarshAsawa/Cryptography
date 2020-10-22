# Substitution Cipher

In substitution cipher, one symbol/character replaces with another. For example, replacing 'A' with 'D'.

## Types: 
 - **Monoalphabetic ciphers** : A character in plaintext is always changed to the same character in the ciphertext regardless of the position.
 - **Polyalphabetic ciphers** : In polyalphabetic substitution, each occurrence of a character may have a different substitute. The relationship between a character in the plaintext to a character in the ciphertext is one-to-many. 


## Implementation: 
1. **Additive or Caesar cipher** : Each character is assigned a unique integer value to the selected key value and perform modulo operation (Z26). Each character is assigned a unique integer value to the selected key value and perform modulo operation (Z26). It is also termed as 'Caesar cipher' or 'Shift cipher'.

2. **Multiplicative Cipher** : In multiplicative cipher, encryption algorithm specifies multiplication of the plaintext by the key. The key needs to be in Z26*. This set has only 12 members: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25.

3. **Affine Cipher** : Combine additive and multiplicative ciphers. Two keys are used in Affine ciphers. The affine cipher uses a pair of keys in which the first key is from Z26* and the second is from Z26. The size of the key domain is 26 × 12 = 312.



