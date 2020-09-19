import string

class Cesar_Cipher:
    
    def __init__(self, data, key):
        self.alphabets = list(string.ascii_lowercase)
        self.data = data.lower()
        self.key = key
        
    def encrypt_data(self):
        encrypted = ''
        for i in self.data:
            index = self.alphabets.index(i)
            k = (index + self.key) % len(self.alphabets)
            encrypted += self.alphabets[k]
        print(encrypted)
    
    def decrypt_data(self):
        decrypted =''
        for i in self.data:
            index = self.alphabets.index(i)
            k = index - self.key
            decrypted += self.alphabets[k]
        print(decrypted)
  

if __name__ == '__main__':  
    print('Let\'s Encrypt or Decrypt using "Cesar Cipher"')
        
    while True:
        action = input('Would you like to Encrypt or Decrypt?').lower()
        if action in ('e','d'):
            break
        
    text_to_use = input('Please Enter your Message...')
    key_to_use = int(input('Plese Enter your key:'))
        
    run = Cesar_Cipher(text_to_use, key_to_use)
    if action == 'e':
            run.encrypt_data()
              
    elif action == 'd':
            run.decrypt_data()