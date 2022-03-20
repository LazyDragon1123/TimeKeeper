import functools
import threading
import time


class RealTimer:
    
    def __init__(self):
        self.int_min = 0.1
    
    def log(self, text):
        print('')
        print(f"{self.int_min * text} MIN")
        print('')

    def start(self):
        for ind in range(1,10):
            t = threading.Timer(60 * self.int_min * ind, functools.partial(self.log, text = ind))
            t.start()
