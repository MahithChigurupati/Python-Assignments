import string
class Vignere_Cipher:
    
    def __init__(self,text,key):
        self.text = text
        self.key = key
        self.text_len = len(self.text)
        self.key_len = len(key)
        self.key= (self.key * (self.text_len % self.key_len))[:self.text_len]
        
        self.alphabets = string.ascii_lowercase
        total_len = len(self.alphabets)
        self.base_data = [[self.alphabets[(i+j) % total_len] for i in range(total_len)] for j in range(total_len)]
        
    def encrypt(self):
        '''
        performing Encryption opertion on text using key
        '''
        encrypted = ''
        
        for i in range(self.text_len):
            row = self.alphabets.index(self.text[i].lower())
            column = self.alphabets.index(self.key[i].lower())
            encrypted += self.base_data[row][column].upper()
            
        print(encrypted)

    def decrypt(self):
        
        '''
        performing decryption opertion on text using key
        '''
        decrypted = ''
        
        for i in range(self.text_len):
            row = self.alphabets.index(self.key[i].lower())
    
            for j in self.base_data[row]:
                if self.text[i].lower() == j:
                    original = self.base_data[row].index(j)
                    decrypted += self.alphabets[original].upper()
        print(decrypted)
    
    
print('Let\'s Encrypt or Decrypt using "Vignere Cipher"')
    
while True:
    action = input('Would you like to Encrypt or Decrypt?').lower()
    if action in ('e','d'):
        break
    
text_to_use = input('Please Enter your Message...')
key_to_use = input('Plese Enter your key:')
    
run = Vignere_Cipher(text_to_use, key_to_use)
if action == 'e':
        run.encrypt()
          
elif action == 'd':
        run.decrypt()