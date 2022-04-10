import argparse

from src.taskmaker import TaskTable

parser = argparse.ArgumentParser()
parser.add_argument("-d", type=int, default=1)
args = parser.parse_args()


def main():
    taskmaker = TaskTable(args.d)
    taskmaker()


if __name__ == "__main__":
    main()
