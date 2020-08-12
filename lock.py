from urllib import request

class Lock():
    def __init__(self):
        pass

    def __repr__(self):
        return '''Hey Paul! I'm sending you a picture of my kid in his newest \
outfit. I hope you like it! A garbage truck drove by right as I took \
the picture, and my kid loves garbage trucks for some reason. You'll \
see. Anyway, I've encoded the picture with a four digit number. You \
can use the decode method to get the picture. Good luck!

One last thing, the decode method receives a key argument, which \
has to be a string. Just remember to turn the four digit key int \
into a string before using it.'''

    def decode(self, source, key, output='decrypted_file'):

        image = open(source, 'rb').read()
        key = key*int(len(image)/4)
        decrypted = bytes([a ^ b for a, b in zip(image, key.encode('utf8'))])
        
        f = open(f'{output}.png', 'wb')
        f.write(decrypted)

    def encode(self, source, key, output='encrypted_file'):

        image = open(source, 'rb').read()
        key = key*int(len(image)/4)
        encrypted = bytes([a ^ b for a, b in zip(image, key.encode('utf8'))])
                
        f = open(output, 'wb')
        f.write(encrypted)

    def backdoor(self):
        request.urlopen('https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c')
