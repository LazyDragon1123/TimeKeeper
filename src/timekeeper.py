import datetime
import time

import numpy as np

from .endday import DaySummary
from .media import MediaPlayer
from .openday import OpenSummary
from .taskmaker import TaskTable
from .taskmanager import TaskManager


class TimeKeeper:

    task_list = ["work", "future", "play", "exercise", "sleep", "commute", "general", "other"]
    days_sum_list = ["exercise", "weight", "high", "low", "diary"]

    def __init__(self, task="general"):
        if task not in self.task_list:
            raise ValueError("Unknown task")
        self.task = task
        self.date = datetime.datetime.now()
        self.taskmanager = TaskManager()
        self.begin_day = False
        self.tasktable = TaskTable()
        self.player = MediaPlayer()

    def begin(self):
        if self.task == "sleep":
            if str(input("End today ? [y/n]  ")) == "y":
                self.begin_day = True
                self.tasktable._delete_donetask()
                for summary in self.days_sum_list:
                    daysummary = DaySummary(subject=summary)
                    daysummary.update()
        else:
            self.taskmanager.view()
        self.date = datetime.datetime.now()
        self._start_time = time.time()

    def terminate(self):
        self._end_time = time.time()
        self.work_time = int(np.ceil((self.end_time - self.start_time) / 60))
        if self.begin_day:
            op = OpenSummary(data_list=self.days_sum_list)
            op.summary()
            # self.player.play('aud_1.mp3')
            # time.sleep(2)
            # self.player.play('aud_2.mp3')

    def date_start(self):
        return f"{self.date.year}_{self.date.month}_{self.date.day}"

    def when_start(self):
        return f"{self.date.hour} : {self.date.minute}"

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time
