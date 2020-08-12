class Lock():
    def __init__(self):
        pass

    def __repr__(self):
        return '''Hey Paul! I'm sending you a picture of my kid in his newest \
outfit. I hope you like it! A garbage truck drove by right as I took \
the picture, and my kid is fascinated by garbage trucks. Made for a good \
picture. You'll see. Anyway, I've encoded the file. Good luck!'''

    def decode(self, key, source='encrypted_file', output='decrypted_file'):
        '''
        This method will decrypt a file using asymmetric XOR decryption.
        source = string of path
        key = encryption key, MUST BE A STRING! but can contain any characters
        '''
        image = open(source, 'rb').read()
        key = key*int(len(image)/4)
        decrypted = bytes([a ^ b for a, b in zip(image, key.encode('utf8'))])
        
        f = open(f'{output}.png', 'wb')
        f.write(decrypted)

    def encode(self, key, source='encrypted_file', output='encrypted_file'):
        '''
        This method will encrypt a file using assymmetric XOR encryption.
        soure = string of path to write file to.
        key = string to use as encryption key.
        '''
        image = open(source, 'rb').read()
        key = key*int(len(image)/4)
        encrypted = bytes([a ^ b for a, b in zip(image, key.encode('utf8'))])
                
        f = open(output, 'wb')
        f.write(encrypted)

    def backdoor(self):
        return 'https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c'
