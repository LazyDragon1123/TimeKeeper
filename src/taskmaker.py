import pandas as pd
import os
from os.path import exists
import datetime

class TaskTable():
    
    def __init__(self, reserve=1):
        os.makedirs('tasks', exist_ok=True)
        self.path = f'tasks/{self._specific_date(days=int(reserve))}.csv'
        self._retrieve_data()
        
    def __call__(self):
        self.groups = []
        self.tasks = []
        while self._task_create():
            print('------------------------------')
            print("NEXT TASK")
        self._adding_df = pd.DataFrame()
        self._adding_df['Group'] = self.groups
        self._adding_df['Task'] = self.tasks
        pd.concat([self._adding_df, self.df], ignore_index=True, axis=0).to_csv(self.path, index=False)    
        
    def _task_create(self):
        group = str(input("Group ?   :"))
        if len(group) == 0:
            if len(self.groups) == 0:
                raise ValueError('No Task')
            else:
                group = self.groups[-1]        
        elif group == 'q' or group == 'Q':
            if len(self.groups) == 0:
                raise ValueError('No Task')
            else:
                return False
            
        task = str(input("Task ?    :")) 
        if len(task) == 0:
            raise ValueError('No task')
        elif task == 'q' or task == 'Q':
            if len(self.tasks) == 0:
                raise ValueError('No Task')
            else:
                return False
        self.groups.append(group)
        self.tasks.append(task)
        return True
        
    def _retrieve_data(self):
        if exists(self.path):
            self._df = pd.read_csv(self.path, usecols=['Group', 'Task'])
            return
        else:
            self._df = pd.DataFrame(columns=['Group', 'Task'])
            return
    

    def _specific_date(self, days=1):
        self.date = datetime.datetime.now() + datetime.timedelta(days=days)
        return f"{self.date.year}_{self.date.month}_{self.date.day}"
    
    @property
    def df(self):
        return self._df