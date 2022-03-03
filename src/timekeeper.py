import time
import datetime
from os.path import exists
import numpy as np
import pandas as pd
from taskmanager import TaskManager

class TimeKeeper:
    
    task_list = ['work', 'future', 'play', 'exercise', 'sleep', 'commute', 'general', 'other']
    
    def __init__(self, task = 'general'):
        if task not in self.task_list:
            raise ValueError('Unknow task')
        self.task = task
        self.date = datetime.datetime.now()
        self.taskmanager = TaskManager()
        
    def begin(self):
        self.taskmanager.view()
        self.date = datetime.datetime.now()
        self._start_time = time.time()
        
    def terminate(self):
        self._end_time = time.time()
        self.work_time = int(np.ceil((self.end_time - self.start_time)/ 60))
        
    def date_start(self):
        return f"{self.date.year}_{self.date.month}_{self.date.day}"
    
    def when_start(self):
        return f"{self.date.hour} : {self.date.minute}"

    @property
    def start_time(self):
        return self._start_time
    
    @property
    def end_time(self):
        return self._end_time
    
