import os
from time import sleep

from cv2 import VideoCapture, imwrite


class TakePhoto:
    def __init__(self):
        self.camera = VideoCapture(0)

    def take(self, path):
        print("Ready picture  3.2.1...")
        sleep(3)
        _, image = self.camera.read()
        os.makedirs("body", exist_ok=True)
        os.makedirs("body/front", exist_ok=True)
        imwrite(f"body/front/{path}.png", image)
        print("Ready Side picture  3.2.1...")
        sleep(3)
        _, image = self.camera.read()
        os.makedirs("body/lateral", exist_ok=True)
        imwrite(f"body/lateral/{path}.png", image)
        
        while str(input('try again ? [y/]')) == 'y':
            print("Ready picture  3.2.1...")
            sleep(3)
            _, image = self.camera.read()
            os.makedirs("body", exist_ok=True)
            os.makedirs("body/front", exist_ok=True)
            imwrite(f"body/front/{path}.png", image)
            print("Ready Side picture  3.2.1...")
            sleep(3)
            _, image = self.camera.read()
            os.makedirs("body/lateral", exist_ok=True)
            imwrite(f"body/lateral/{path}.png", image)            

if __name__ == '__main__':
    t = TakePhoto()
    t.take('2022_4_12')
