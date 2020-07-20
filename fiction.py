import requests
from util import parse_html
from chapter import Chapter
from config import config


class Fiction():
    def __init__(self):
        res = requests.get(config.url_prefix + config.fiction_url)
        self.fiction_html = parse_html(res)
        self.fiction_title = self.get_fiction_title()
        self.chapter_list = self.get_fiction_chapter_list()

    '''获取章节列表'''

    def get_fiction_chapter_list(self):
        chapter_a_list = self.fiction_html.xpath('//div[@id="list"]//a')
        chapter_list = [{'title': chapter_a.text, 'href': chapter_a.get('href')} for chapter_a in chapter_a_list]
        return chapter_list

    '''获取小说名称'''

    def get_fiction_title(self):
        return self.fiction_html.xpath('//div[@id="info"]/h1//text()')[0]

    '''获取小说章节'''

    def get_fiction_chapter(self, index):
        if len(self.chapter_list) <= index:
            print("没有更多章节了")
            return None
        else:
            current_chapter_info_dict = self.chapter_list[config.fiction_index]
            return Chapter(current_chapter_info_dict['title'], current_chapter_info_dict['href'])

    '''获取章节标题'''

    def get_fiction_chapter_title(self, index):
        if len(self.chapter_list) <= index or index < 0:
            print("没有更多章节了")
            return None
        else:
            return self.chapter_list[index]['title']


fiction = Fiction()
