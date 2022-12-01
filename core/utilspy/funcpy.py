import sys
import os
import time
import datetime


def exit():
    print('Bye~')
    time.sleep(0.6)
    sys.exit(1)


def clear():
    os.system('cls')


def date():
    current_time = datetime.datetime.now()
    return str(current_time).split('.')[0]
