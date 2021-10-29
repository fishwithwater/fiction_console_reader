import os
import platform


def clear():
    if platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
