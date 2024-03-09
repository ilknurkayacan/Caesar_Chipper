# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 22:56:57 2024

@author: ilknu
"""
def encoders(text,shift):
    crypto_alfhabet=[]
    crypto_text=""
    text.split()
    
    for i in range(len(alphabet)):
        if (i+shift)>=len(alphabet):
            x=i+shift-len(alphabet)
            crypto_alfhabet.append(alphabet[x])
        else:
            crypto_alfhabet.append(alphabet[i+shift])
    
    for i in range(len(text)):
        for k in range(len(alphabet)):
            if text[i] == alphabet[k]:
                
                crypto_text += crypto_alfhabet[k]
                

                
    return crypto_text

def decoders(text,shift):
    decrypto_text=""
    text.split()
    crypto_alphabet=[]
    
    for i in range(len(alphabet)):
        if (i+shift)>=len(alphabet):
            x=i+shift-len(alphabet)
            crypto_alphabet.append(alphabet[x])
        else:
            crypto_alphabet.append(alphabet[i+shift])
    
    for k in range(len(text)):
        for i in range(len(crypto_alphabet)):
            if text[k] == crypto_alphabet[i]:
                decrypto_text += alphabet[i]
    
    return decrypto_text

        
        
    
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


if direction=="encode":
    print(encoders(text,shift))
elif direction=="decode":
    print(decoders(text,shift))