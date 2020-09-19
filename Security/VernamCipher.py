# Vernam Cipher encryption and decryption Algoritm

import string
class Vernam_Cipher:
    
    def __init__(self,text,key):
        self.text = text
        self.key = key
        
        # Generates a string of alphabets from a to z in lower case
        self.alphabets = string.ascii_lowercase

    def encrypt(self):
        # for encrypting the given text using key text
        text_indices = []
        key_indices = []

        
        for i in self.text.lower():
            text_indices.append(self.alphabets.index(i))
            
        for j in self.key.lower():
            key_indices.append(self.alphabets.index(j))
            
        # summing up text and key indices and reducing it in case of index is greater than 26
        encrypted_index = [(x+y)%len(self.alphabets) for x,y in zip(text_indices,key_indices)]
        
        for i in encrypted_index:
            print(self.alphabets[i].upper(), end='')
        
        
    def decrypt(self):
        # decrypting the encrypted text using key
        text_indices = []
        key_indices = []
        
        for i in self.text.lower():
            text_indices.append(self.alphabets.index(i))
            
        for j in self.key.lower():
            key_indices.append(self.alphabets.index(j))
        
        # perforrming subtraction operation between decryped and key text indices
        decrypted_index = [(x-y) for x,y in zip(text_indices,key_indices)]
        
        for i in decrypted_index:
            if i < 0:
                i = 26-abs(i) #if index is negative
            print(self.alphabets[i].upper(), end='')
                        
            
if __name__ == '__main__':
    print('Let\'s Encrypt or Decrypt using "Vernam Cipher"')
        
    while True:
        action = input('Would you like to Encrypt or Decrypt?').lower()
        if action in ('e','d'):
            break
        
    text_to_use = input('Please Enter your Message...')
    key_to_use = input('Plese Enter your key:')
        
    run = Vernam_Cipher(text_to_use, key_to_use)
    if action == 'e':
            run.encrypt()
              
    elif action == 'd':
            run.decrypt()