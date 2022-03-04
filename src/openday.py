import imp


import pandas as pd

suffix = '\033['
tail = '\033[0m'

class OpenSummary:

    negative_health = ['caffein']

    def __init__(self, data_list = ['exercise', 'caffein']):
        self.data_list = data_list


    def summary(self):
        pass

    def get_news(self):
        pass

    def get_yourdata(self, ref_days = 7):
        for sub in self.data_list:
            df = pd.read_csv(f'calendar/{sub}.csv', usecols=['Date', 'Eval'])
            ref_dates = self.extract_day(df['Date'].to_list())[:ref_days]
            evals = df['Eval'].to_list()
            exhibits = self.make_exhibits(ref_dates, evals, negative=(sub in self.negative_health))
            print(f' *   {sub}')
            for e in exhibits:
                print(e)

    @staticmethod
    def extract_day(days):
        ###
        return [date for date in days]

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
