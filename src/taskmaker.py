import datetime
import os
from copy import deepcopy
from os.path import exists

import numpy as np
import pandas as pd

daily_tasks = {"future": "leetcode", "exercise": "strech"}


class TaskTable:
    def __init__(self, reserve=1):
        os.makedirs("tasks", exist_ok=True)
        self.path = f"tasks/{self._specific_date(days=int(reserve))}.csv"
        self._retrieve_data()

    def __call__(self):
        self.groups = []
        self.tasks = []
        while self._task_create():
            print("------------------------------")
            print("NEXT TASK")
        self._adding_df = pd.DataFrame()
        self._adding_df["Group"] = self.groups
        self._adding_df["Task"] = self.tasks
        self._adding_df["State"] = [70] * len(self.tasks)
        self.everlasting_task(
            pd.concat([self._adding_df, self._df], ignore_index=True, axis=0)
        ).drop_duplicates().to_csv(self.path, index=False)

    def _task_create(self):
        group = str(input("Group ?   :"))
        if len(group) == 0:
            if len(self.groups) == 0:
                raise ValueError("No Task")
            else:
                group = self.groups[-1]
        elif group == "q" or group == "Q":
            if len(self.groups) == 0:
                raise ValueError("No Task")
            else:
                return False

        task = str(input("Task ?    :"))
        if len(task) == 0:
            raise ValueError("No task")
        elif task == "q" or task == "Q":
            if len(self.tasks) == 0:
                raise ValueError("No Task")
            else:
                return False
        self.groups.append(group)
        self.tasks.append(task)
        return True

    def _retrieve_data(self):
        if exists(self.path):
            try:
                self._df = pd.concat(
                    [pd.read_csv(self.path, usecols=["Group", "Task", "State"]), self._previousd_data()],
                    ignore_index=True,
                    axis=0,
                )
                return
            except:
                self._df = pd.read_csv(self.path, usecols=["Group", "Task"])
                self._df["State"] = [70] * len(self._df)
                self._df = pd.concat([self._df, self._previousd_data()], ignore_index=True, axis=0)
                return
        else:
            self._df = self._previousd_data()
            return

    def _previousd_data(self):
        prev_path = f"tasks/{self._specific_date(days=0)}.csv"
        if exists(prev_path):
            try:
                prev_df = pd.read_csv(prev_path, usecols=["Group", "Task", "State"])
                return prev_df[prev_df["State"] == 70]
            except:
                return pd.DataFrame(columns=["Group", "Task", "State"])
        else:
            return pd.DataFrame(columns=["Group", "Task", "State"])

    def _delete_donetask(self):
        prev_df = pd.read_csv(f"tasks/{self._specific_date(days=0)}.csv", usecols=["Group", "Task", "State"])
        for gr, ta, st in zip(
            prev_df.loc[:, "Group"].to_list(), prev_df.loc[:, "Task"].to_list(), prev_df.loc[:, "State"].to_list()
        ):
            self._df = self._df.reset_index(drop=True)
            if st == 90:
                self._df = self._df.drop(np.where((self._df["Group"] == gr) & (self._df["Task"] == ta))[0])
        self._df.drop_duplicates().to_csv(self.path, index=False)

    def _specific_date(self, days=1):
        self.date = datetime.datetime.now() + datetime.timedelta(days=days)
        return f"{self.date.year}_{self.date.month}_{self.date.day}"

    @staticmethod
    def everlasting_task(df):
        ret_df = deepcopy(df)
        for gp, dtask in daily_tasks.items():
            if dtask not in ret_df.Task:
                ret_df.loc[len(ret_df)] = [gp, dtask, 70]
        return ret_df
