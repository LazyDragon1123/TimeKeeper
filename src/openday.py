from datetime import datetime, timedelta

import pandas as pd
from collector.collector import Weather

from src.phototaker.takephoto import TakePhoto

suffix = "\033["
tail = "\033[0m"


class OpenSummary:

    negative_health = ["caffein", "weight"]
    floatval = ["weight", 'high', 'low']
    not_shown = ['diary']

    def __init__(self, data_list=["exercise", "caffein"]):
        self.data_list = data_list
        self.w = Weather()
        self.takephoto = TakePhoto()

    def summary(self):
        self.takephoto.take(self._specific_date())
        self.get_news()
        self.get_yourdata()

    def get_news(self):
        self.w()

    def get_yourdata(self, ref_days=7):
        for sub in self.data_list:
            if sub in self.not_shown:
                continue
            df = pd.read_csv(f"calendar/{sub}.csv", usecols=["Date", "Eval"])
            ref_dates = self.extract_day(df["Date"].to_list())[:ref_days]
            evals = df["Eval"].to_list()
            if self.is_today(ref_dates[0]):
                ref_dates = ref_dates[1:]
                evals = evals[1:]
            exhibits = self.make_exhibits(
                ref_dates, evals, negative=(sub in self.negative_health), floatval=(sub in self.floatval)
            )
            print(f" **  {sub}  **  ")
            for e in exhibits:
                print(e, end=" ")
            print("")
        print("")

    @staticmethod
    def is_today(todate):
        if datetime.now().day == int(todate):
            return True
        else:
            return False

    @staticmethod
    def extract_day(days):
        return [datetime.strptime(date, "%Y_%m_%d").day for date in days]

    @staticmethod
    def make_exhibits(text, evals, negative=False, floatval=False):
        if floatval:
            sign = -1 if negative else 1
            exhibits = []
            for ind in range(len(text)):
                e = float(evals[ind])
                if e * sign >= evals[ind + 7] * sign:
                    exhibits.append("{}{}m{}{}".format(suffix, "96", str(e), tail))
                else:
                    exhibits.append("{}{}m{}{}".format(suffix, "90", str(e), tail))
            return exhibits
        else:
            if negative:
                evals = [not eval for eval in evals]
            exhibits = []
            for ind in range(len(text)):
                e = evals[ind]
                t = text[ind]
                if e:
                    exhibits.append("{}{}m{}{}".format(suffix, "96", t, tail))
                else:
                    exhibits.append("{}{}m{}{}".format(suffix, "90", t, tail))
            return exhibits

    def _specific_date(self, days=0):
        self.date = datetime.now() + timedelta(days=days)
        return f"{self.date.year}_{self.date.month}_{self.date.day}"
