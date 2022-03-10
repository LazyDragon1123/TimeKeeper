import datetime

import numpy as np
import pandas as pd


def date_str_sort(dlist):
    dtimes = sorted([datetime.datetime.strptime(i, "%Y_%m_%d") for i in dlist])[::-1]
    return [i.strftime("%Y_%-m_%-d") for i in dtimes]

def main():
    df = pd.read_csv('limited_life.csv')
    dates = date_str_sort(list(set(list(df['Date']))))
    print('')
    for date in dates[:5]:
        df_date = df[df['Date'] == date]
        tasks = np.sort(list(set(list(df_date['Task']))))
        print(f'---  {date}  ---')
        for task in tasks:
            df_task = df_date[df_date['Task'] == task]
            hour, min = divmod(sum(df_task['Work Mins']),60)
            print(f'{task}  :  {int(hour)} 時間　{int(min)} 分')
        print('')
if __name__ == "__main__":
    main()
