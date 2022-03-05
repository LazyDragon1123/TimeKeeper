from datetime import datetime

import pandas as pd
from collector.collector import Weather

suffix = '\033['
tail = '\033[0m'

class OpenSummary:

    negative_health = ['caffein']

    def __init__(self, data_list = ['exercise', 'caffein']):
        self.data_list = data_list
        self.w = Weather()


    def summary(self):
        self.get_news()
        self.get_yourdata()

    def get_news(self):
        self.w()

    def get_yourdata(self, ref_days = 7):
        for sub in self.data_list:
            df = pd.read_csv(f'calendar/{sub}.csv', usecols=['Date', 'Eval'])
            ref_dates = self.extract_day(df['Date'].to_list())[:ref_days]
            evals = df['Eval'].to_list()
            exhibits = self.make_exhibits(ref_dates, evals, negative=(sub in self.negative_health))
            print(f' **  {sub}  **  ')
            for e in exhibits:
                print(e, end=' ')
            print('')
        print('')

    @staticmethod
    def extract_day(days):
        return [datetime.strptime(date, '%Y_%m_%d').day for date in days]

    @staticmethod
    def make_exhibits(text, evals, negative=False):
        if negative:
            evals = [~eval for eval in evals]
        exhibits = []
        for t, e in zip(text, evals):
            if e:
                exhibits.append('{}{}m{}{}'.format(suffix, '96', t, tail))
            else:
                exhibits.append('{}{}m{}{}'.format(suffix, '90', t, tail))
        return exhibits
