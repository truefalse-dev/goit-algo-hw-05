from colorama import Fore
from task1 import main as ts1
from task2 import main as ts2
from task3 import main as ts3
from task4 import main as ts4


BOLD_INIT = '\033[1m'
BOLD_RESET = '\033[0m'


def header(title):
    print("\n" + Fore.YELLOW + BOLD_INIT + f"{title}" + BOLD_RESET + Fore.LIGHTWHITE_EX)


if __name__ == '__main__':
    header("Task 1")
    ts1()
    header("Task 2")
    ts2()
    header("Task 3")
    ts3()
    header("Task 4")
    ts4()