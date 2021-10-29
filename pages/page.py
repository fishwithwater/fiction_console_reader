from abc import abstractmethod

from util import clear


def print_content(func):
    def wrapper(self, *args, **kwargs):
        clear()
        str = func(self, *args, **kwargs)
        print(str)

    return wrapper


class Page:

    @abstractmethod
    def on_destroy(self):
        pass

    @abstractmethod
    def print(self):
        pass
