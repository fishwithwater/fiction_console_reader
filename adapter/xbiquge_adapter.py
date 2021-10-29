from adapter.adapter import Adapter
import requests
from config import app_config
from lxml import etree


class XbiqugeAdapter(Adapter):
    def __init__(self):
        res = requests.get(app_config.source_website + app_config.fiction_index_url)
        res.encoding = app_config.encode
        self.fiction_html = etree.HTML(res.text)
        self.fiction_title = self.fiction_html.xpath('//div[@id="info"]/h1//text()')[0]
        self.chapter_list = self.format_chapter_list()

    @classmethod
    def supports(cls, url):
        return ['http://www.xbiquge.la'].__contains__(url)

    def format_chapter_list(self):
        chapter_a_list = self.fiction_html.xpath('//div[@id="list"]//a')
        chapter_list = [{'title': chapter_a.text, 'href': chapter_a.get('href')} for chapter_a in chapter_a_list]
        return chapter_list

    def get_fiction_title(self):
        return self.fiction_title

    def get_fiction_chapter_list(self):
        return self.chapter_list

    def get_fiction_chapter_content(self):
        pass
