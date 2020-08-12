from PIL import Image
import os

class Safe():
    def __init__(self):
        self._combo = 'combo'

    def __repr__(self):
        return '''This is a safe. It contains a very special item.
        
        methods:
         - dial(combo): The safe's dial will receive and store a combo.
                  Combo = [string of any length].
         - handle(): The safe's handle will open the door.
                  Only works if the correct combination is used.
         '''

    def dial(self, combo):
        self._combo = combo

    def handle(self):
        image = open('.safe_contents', 'rb').read()
        key = self._combo*int(len(image)/4)
        dcr_img = bytes([a ^ b for a, b in zip(image, key.encode('utf8'))])
        f = open('safe_contents.png', 'wb')
        f.write(dcr_img)
        try:
            Image.open(f).show()
            f.close()
            print('Safe unlocked!')
        except:
            f.close()
            os.remove('safe_contents.png')
            print('Wrong code.')

    def backdoor(self):
        return 'https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c'