import os
import enum
import platform


def clear():
    if platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')


class Controller:
    def __init__(self, config, fiction):
        self.config = config
        self.fiction = fiction
        self.current_chapter = None
        self.current_chapter_title = None
        self.offset = 0
        self.limit = config.line_limit
        self.mode = Mode.Home

    def print_content(func):
        def wrapper(self, *args, **kwargs):
            clear()
            str = func(self, *args, **kwargs)
            print(str)
            self.print_controller()

        return wrapper

    @print_content
    def next_page(self):
        self.mode = Mode.Fiction
        if self.need_next_page():
            if self.current_chapter is not None:
                self.config.next_page()
            self.current_chapter = Controller.format_chapter_content(
                self.fiction.get_fiction_chapter(self.config.fiction_index))
            self.current_chapter_title = self.fiction.get_fiction_chapter_title(self.config.fiction_index)
            self.offset = 0
        elif self.current_chapter is None:
            self.current_chapter = Controller.format_chapter_content(
                self.fiction.get_fiction_chapter(self.config.fiction_index))
            self.current_chapter_title = self.fiction.get_fiction_chapter_title(self.config.fiction_index)
        elif self.current_chapter is not None:
            self.offset += self.limit
        return Controller.format_print(self.current_chapter[self.offset:self.offset + self.limit])

    @print_content
    def last_page(self):
        self.mode = Mode.Fiction
        if self.need_last_page():
            self.config.last_page()
            self.current_chapter = Controller.format_chapter_content(
                self.fiction.get_fiction_chapter(self.config.fiction_index))
            self.current_chapter_title = self.fiction.get_fiction_chapter_title(self.config.fiction_index)
            self.offset = len(self.current_chapter) - self.limit
        else:
            self.offset -= self.limit
            if self.offset == 0:
                self.offset = 0
        return Controller.format_print(self.current_chapter[self.offset:self.offset + self.limit])

    @classmethod
    def format_chapter_content(cls, content):
        return content.split('\n')

    def need_next_page(self):
        if self.current_chapter is None:
            return False
        size = len(self.current_chapter)
        limit = self.limit
        offset = self.offset
        if offset + limit > size:
            return True
        return False

    def need_last_page(self):
        offset = self.offset
        if offset <= 0:
            return True
        return False

    def print_controller(self):
        if self.mode == Mode.Fiction:
            print("\n===[{0}]:[{1}]:[{2}%]:[{3}]\t[ESC]退出\t[↑]上一页\t[↓]下一页\t[→]查看目录(暂未支持)\t[←]返回===\n".format(
                self.fiction.fiction_title, self.current_chapter_title,
                round(self.offset / len(self.current_chapter) * 100, 2), self.offset))
        elif self.mode == Mode.Home:
            print("\n===[ESC]退出\t[↓]继续阅读\t[→]查看目录(暂未支持)===\n")

    @classmethod
    def format_print(cls, content):
        return "\n".join(content)

    @print_content
    def print_home(self):
        self.mode = Mode.Home
        return "=====Fiction Console Reader=====\n" + "上次读到:《{0}》- {1} - 共{2}章节\n".format(self.fiction.fiction_title,
                                                                                    self.fiction.chapter_list[
                                                                                        self.config.fiction_index][
                                                                                        'title'],
                                                                                    len(self.fiction.chapter_list))


class Mode(enum.Enum):
    Home = 'Home'
    Fiction = 'Fiction'
    Catalog = 'Catalog'
