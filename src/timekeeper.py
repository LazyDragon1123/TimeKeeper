import datetime
import time
from operator import sub
from os.path import exists

import numpy as np
import pandas as pd

from .endday import DaySummary
from .openday import OpenSummary
from .taskmanager import TaskManager


class TimeKeeper:
    
    task_list = ['work', 'future', 'play', 'exercise', 'sleep', 'commute', 'general', 'other']
    days_sum_list = ['exercise', 'caffein']
    
    def __init__(self, task = 'general'):
        if task not in self.task_list:
            raise ValueError('Unknow task')
        self.task = task
        self.date = datetime.datetime.now()
        self.taskmanager = TaskManager()
        self.begin_day = False
        
    def begin(self):
        if self.task == 'sleep':
            if str(input('End today ? [y/n]  ')) == 'y':
                self.begin_day = True
                for summary in self.days_sum_list:
                    daysummary = DaySummary(subject=summary)
                    daysummary.update()
        else:
            self.taskmanager.view()
        self.date = datetime.datetime.now()
        self._start_time = time.time()
        
    def terminate(self):
        self._end_time = time.time()
        self.work_time = int(np.ceil((self.end_time - self.start_time)/ 60))
        if self.begin_day:
            op = OpenSummary()
            op.summary()


        
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
    
