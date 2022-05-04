import os
from tkinter.messagebox import NO


class MediaPlayer:

    def __init__(self, album=None):
        self.media_path = 'media/sound/'
        if album is not None:
            self.media_path = f'media/{album}/'
            self.files = []
            for file in os.listdir(self.media_path):
                if file.endswith(".mp3"):
                    self.files.append(file)

    def play(self, file_):
        if isinstance(file_, str):
            os.system(f'mpg123 -q {self.media_path + file_}')
        elif isinstance(file_, list):
            for f in file_:
                os.system(f'mpg123 -q {self.media_path + f}')
