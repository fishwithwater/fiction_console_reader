import requests
from util import parse_html, filter_ads, format_chapter
from config import config


class Chapter:
    def __init__(self, chapter_name, chapter_url):
        self.chapter_name = chapter_name
        self.chapter_url = chapter_url
        self.content_list = []
        self.offset = 0
        self.refresh()

    '''刷新章节数据'''

    def refresh(self):
        chapter_page_res = requests.get(config.url_prefix + self.chapter_url)
        chapter_html = parse_html(chapter_page_res)
        content = chapter_html.xpath('//div[@id="content"]//text()')
        content_format = filter_ads(format_chapter(content))
        self.content_list = content_format

    '''是否需要加载下一章'''

    def need_next_chapter(self):
        return self.offset >= len(self.content_list) - config.line_limit

    '''是否需要加载上一章'''

    def need_last_chapter(self):
        return self.offset <= config.line_limit

    '''获取下一页'''

    def get_next_page(self):
        limit = config.line_limit
        offset = self.offset
        end = offset + limit
        if end > len(self.content_list):
            end = len(self.content_list)
        content = self.content_list[offset:end]
        self.offset += limit
        return content

    '''获取上一页'''

    def get_last_page(self):
        limit = config.line_limit
        if self.offset == 0:
            self.offset = len(self.content_list)
        offset = self.offset
        start = offset - limit
        if start < 0:
            start = 0
        content = self.content_list[start:offset]
        self.offset = start
        return content

    def get_chapter_percent(self):
        return self.offset / len(self.content_list)
