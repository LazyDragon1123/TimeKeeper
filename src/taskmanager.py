import datetime
import time
from os.path import exists

import numpy as np
import pandas as pd

suffix = '\033['
tail = '\033[0m'

class TaskManager:
    
    def __init__(self):
        self.date = datetime.datetime.now()

    def update(self):
        self._show_tasks(num=True)
        ind = int(input("Id ?    "))
        self.update_by_id(self.get_taskdf(), ind).to_csv(f'tasks/{self._specific_date()}.csv',  index=False)
        pd.read_csv(f'tasks/{self._specific_date()}.csv', usecols=['Group', 'Task', 'State']).to_csv(f'tasks/{self._specific_date(days=-1)}.csv',  index=False)
        print('')
        print('\033[96mGood Job ! !\033[0m')
        print('')

    def view(self):
        self._show_tasks()
        
    def _specific_date(self, days=0):
        self.date = datetime.datetime.now() + datetime.timedelta(days=days)
        return f"{self.date.year}_{self.date.month}_{self.date.day}"

    def _show_tasks(self, num=None):
        task_df = self.get_taskdf()
        groups = np.sort(list((set(task_df['Group']))))
        cout = 0
        self.tasks = []
        self.groups = []
        for group in groups:
            print(f'---  {group}  ---')
            print('')
            for task, cnum in zip(task_df[task_df['Group'] == group].loc[:,'Task'], task_df[task_df['Group'] == group].loc[:,'State']):
                if num is None:
                    self.color_print(" *  {}".format(task), cnum) 
                else:
                    self.color_print(" {}.  {}".format(cout, task), cnum) 
                    self.groups.append(group)
                    self.tasks.append(task)
                cout += 1
            print('')
        return

    def get_taskdf(self):
        if exists(f'tasks/{self._specific_date()}.csv'):
            try:
                return pd.read_csv(f'tasks/{self._specific_date()}.csv', usecols=['Group', 'Task', 'State'])
            except:
                task_df = pd.read_csv(f'tasks/{self._specific_date()}.csv', usecols=['Group', 'Task'])
                task_df['State'] = [70] * len(task_df)
                return task_df
        else:
            return pd.DataFrame(columns=['Group', 'Task', 'State'])

    def update_by_id(self, taskdf, id):
        taskdf_g = taskdf[taskdf['Group'] == self.groups[id]]
        ind = taskdf_g[taskdf_g['Task'] == self.tasks[id]].index[0]
        taskdf.iloc[ind, np.where(np.array(taskdf.columns == 'State'))[0][0]] = 90
        return taskdf

    @staticmethod
    def color_print(text, cnum=70):
        print("{}{}m{}{}".format(suffix, str(int(cnum)), text, tail))
    
