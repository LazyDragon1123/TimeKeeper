import time
import datetime
from os.path import exists
import numpy as np
import pandas as pd

class TimeKeeper:
    
    task_list = ['work', 'future', 'play', 'exercise', 'sleep', 'commute', 'general', 'other']
    
    def __init__(self, task = 'general'):
        if task not in self.task_list:
            raise ValueError('Unknow task')
        self.task = task
        self.date = datetime.datetime.now()
        self._show_tasks()
        
    def begin(self):
        self.date = datetime.datetime.now()
        self._start_time = time.time()
        
    def terminate(self):
        self._end_time = time.time()
        self.work_time = int(np.ceil((self.end_time - self.start_time)/ 60))
        
    def date_start(self):
        return f"{self.date.year}_{self.date.month}_{self.date.day}"
    
    def when_start(self):
        return f"{self.date.hour} : {self.date.minute}"

    def _show_tasks(self):
        if exists(f'tasks/{self.date_start()}.csv'):
            task_df = pd.read_csv(f'tasks/{self.date_start()}.csv', usecols=['Group', 'Task'])
            groups = list(set(task_df['Group']))
            for group in groups:
                print(f'---  {group}  ---')
                print('')
                for task in task_df[task_df['Group'] == group].loc[:,'Task']:
                    print(f' *  {task}')
                print('')
            return
        return
        
    @property
    def start_time(self):
        return self._start_time
    
    @property
    def end_time(self):
        return self._end_time
    
