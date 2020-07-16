
class Controller:
    def __init__(self, config, fiction):
        self.config = config
        self.fiction = fiction
        self.current_chapter = None
        self.current_chapter_title = None
        self.offset = 0
        self.limit = config.line_limit

    def next_page(self):
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
        Controller.format_print(self.current_chapter[self.offset:self.offset + self.limit])

    def last_page(self):
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
        Controller.format_print(self.current_chapter[self.offset:self.offset + self.limit])

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
        size = len(self.current_chapter)
        offset = self.offset
        limit = self.limit
        if offset <= 0:
            return True
        return False

    def print_controller(self):
        print("\n===[{0}]:[{1}]:[{2}%]:[{3}]\t[ESC]退出\t[↑]上一页\t[↓]下一页===\n".format(
            self.fiction.fiction_title, self.current_chapter_title,
            round(self.offset / len(self.current_chapter) * 100, 2), self.offset))

    @classmethod
    def format_print(cls, content):
        print("\n".join(content))
