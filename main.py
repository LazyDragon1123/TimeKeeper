import argparse

from src.save import TimeSave
from src.termination import Termination
from src.timekeeper import TimeKeeper

parser = argparse.ArgumentParser()
parser.add_argument("-t", type=str)
args = parser.parse_args()

timer = TimeKeeper(task=args.t)
terminator = Termination()
saver = TimeSave(timer)


def main():
    timer.begin()
    terminator()
    saver()
    exit()


if __name__ == "__main__":
    main()
