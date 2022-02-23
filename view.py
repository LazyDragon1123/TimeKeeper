import pandas as pd
import numpy as np

def main():
    df = pd.read_csv('limited_life.csv')
    dates = np.sort(list(set(list(df['Date']))))[::-1]
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