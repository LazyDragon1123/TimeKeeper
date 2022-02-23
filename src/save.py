import pandas as pd
from os.path import exists
from .timekeeper import TimeKeeper


class TimeSave:
    
    def __init__(self, timekeeper: TimeKeeper):
        self.path = 'limited_life.csv'
        self.path_copy = 'limited_life_copy.csv'
        self._retrieve_data()
        self._timekeeper = timekeeper
        
    def __call__(self):
        self._timekeeper.terminate()
        self._adding_df = pd.DataFrame({
            'Date': self._timekeeper.date_start(),
            'Start Time': self._timekeeper.when_start(),
            'Work Mins': self._timekeeper.work_time,
            'Task': self._timekeeper.task},index=[0])
        pd.concat([self._adding_df, self.df], ignore_index=True, axis=0).to_csv(self.path, index=False)
        
    def _retrieve_data(self):
        if exists(self.path):
            self._df = pd.read_csv(self.path, usecols=['Date', 'Start Time', 'Work Mins', 'Task'])
            self._df.to_csv(self.path_copy, index=False)
            return
        else:
            self._df = pd.DataFrame(columns=['Date', 'Start Time', 'Work Mins', 'Task'])
            return
    
    
    @property
    def df(self):
        return self._df