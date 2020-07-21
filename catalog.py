from fiction import fiction
from util import format_catalog


class Catalog:
    def __init__(self, chapter_list):
        self.chapter_list = chapter_list
        self.offset = 0
        self.limit = 30

    def get_next_page(self):
        if self.offset > len(self.chapter_list) - self.limit:
            return "没有更多章节啦"
        current_page_chapter_list = self.chapter_list[self.offset:self.offset + self.limit]
        self.offset += self.limit
        return format_catalog(current_page_chapter_list, self.limit)

    def get_last_page(self):
        self.offset -= self.limit
        if self.offset < self.limit:
            return "没有更多章节啦"
        current_page_chapter_list = self.chapter_list[self.offset - self.limit:self.offset]
        return format_catalog(current_page_chapter_list, self.limit)


catalog = Catalog(fiction.get_fiction_chapter_list())
