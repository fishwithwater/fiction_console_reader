import os
import enum
import platform
from config import config
from fiction import fiction
from util import format_print
from catalog import catalog


def clear():
    if platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')


class Controller:
    def __init__(self):
        self.mode = Mode.Home
        self.current_chapter = fiction.get_fiction_chapter(config.fiction_index)

    def print_content(func):
        def wrapper(self, *args, **kwargs):
            clear()
            str = func(self, *args, **kwargs)
            print(str)
            self.print_controller()

        return wrapper

    @print_content
    def next_page(self):
        if self.mode != Mode.Fiction:
            self.mode = Mode.Fiction
        if self.current_chapter.need_next_chapter():
            config.next_page()
            self.current_chapter = fiction.get_fiction_chapter(config.fiction_index)
        return format_print(self.current_chapter.get_next_page())

    @print_content
    def last_page(self):
        if self.mode != Mode.Fiction:
            self.mode = Mode.Fiction
        if self.current_chapter.need_last_chapter():
            config.last_page()
            self.current_chapter = fiction.get_fiction_chapter(config.fiction_index)
            return format_print(self.current_chapter.get_last_page())
        else:
            return format_print(self.current_chapter.get_last_page())

    @print_content
    def show_chapter_next(self):
        if self.mode != Mode.Catalog:
            self.mode = Mode.Catalog
        return catalog.get_next_page()

    @print_content
    def show_chapter_last(self):
        if self.mode != Mode.Catalog:
            self.mode = Mode.Catalog
        return catalog.get_last_page()

    def print_controller(self):
        if self.mode == Mode.Fiction:
            print("\n===[{0}]:[{1}]:[{2}%]\t[ESC]退出\t[↑]上一页\t[↓]下一页\t[→]查看目录\t[←]返回===\n".format(
                fiction.fiction_title, self.current_chapter.chapter_name,
                round(self.current_chapter.get_chapter_percent() * 100, 2)))
        elif self.mode == Mode.Home:
            print("\n===[ESC]退出\t[↓]继续阅读\t[→]查看目录===\n")
        elif self.mode == Mode.Catalog:
            print("\n===[ESC]退出\t[↑]上一页\t[↓]下一页\t[←]返回===\n===")

    @print_content
    def print_home(self):
        self.mode = Mode.Home
        return "=====Fiction Console Reader=====\n" + "上次读到:《{0}》- {1} - 共{2}章节\n".format(fiction.fiction_title,
                                                                                          fiction.chapter_list[
                                                                                              config.fiction_index][
                                                                                              'title'],
                                                                                          len(
                                                                                              fiction.chapter_list))


class Mode(enum.Enum):
    Home = 'Home'
    Fiction = 'Fiction'
    Catalog = 'Catalog'
