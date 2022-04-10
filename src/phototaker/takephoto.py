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
        imwrite(f"body/{path}.png", image)
