import datetime
from os.path import exists

import pandas as pd

float_sub = ["weight"]


class DaySummary:
    def __init__(self, subject="exercise"):
        self.subject = subject
        self.path = f"calendar/{subject}.csv"
        self.df = self.retrieve_data(self.path)

    def update(self):
        last_day = self.last_day_check()
        adding_df = pd.DataFrame()
        adding_df["Date"] = last_day
        adding_df["Eval"] = self.evaluate(self.subject) * len(last_day)
        pd.concat([adding_df, self.df], ignore_index=True, axis=0).to_csv(self.path, index=False)

    def last_day_check(self):
        if len(self.df) == 0:
            return [self._specific_date()]
        elif self._specific_date() == self.df["Date"].to_list()[0]:
            self.df = self.df.drop([0])
            return [self._specific_date()]
        elif self._specific_date(days=-1) == self.df["Date"].to_list()[0]:
            return [self._specific_date()]
        elif self._specific_date(days=-2) == self.df["Date"].to_list()[0]:
            return [self._specific_date(), self._specific_date(days=-1)]
        else:
            return [self._specific_date()]

    @staticmethod
    def evaluate(subject):
        if subject in float_sub:
            return [float(input(f"How was {subject} ?   "))]
        else:
            ans = str(input(f"How was {subject} ? [y/n]  "))
            return [True] if ans.lower() == "y" else [False]

    @staticmethod
    def _specific_date(days=0):
        date = datetime.datetime.now() + datetime.timedelta(days=days)
        return f"{date.year}_{date.month}_{date.day}"

    @staticmethod
    def retrieve_data(path):
        return pd.read_csv(path, usecols=["Date", "Eval"]) if exists(path) else pd.DataFrame(columns=["Date", "Eval"])
