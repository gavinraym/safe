from PIL import Image

class Lock():
    def __init__(self):
        self.combo = 'combo'

    def __repr__(self):
        return '''This is a safe. It contains a very special item.
        
        methods:
         - dial(combo): The safe's dial will receive and store a combo.
                  Combo = [string of any length].
         - handle(): The safe's handle will open the door.
                  Only works if the correct combination is used.
         '''

    def dial(self, combo):
        self.combo = combo

    def handle(self):
        image = open('.safe_contents', 'rb').read()
        key = self.combo*int(len(image)/4)
        dcr_img = bytes([a ^ b for a, b in zip(image, key.encode('utf8'))])
        f = open('safe_contents.png', 'wb')
        f.write(dcr_img)
        try:
            Image.open('safe_contents.png').show()
            print('Safe unlocked!')
        except:
            print('Wrong code.')

    def backdoor(self):
        return 'https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c'

    if __name__ == '__main__':
        'The Lock class can be instatiated with: lock = Lock()'