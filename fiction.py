import requests
from lxml import etree


class Fiction:
    def __init__(self, config):
        self.config = config
        res = requests.get(config.url_prefix + config.fiction_url)
        self.fiction_html = Fiction.parse_html(res)
        self.fiction_title = self.get_fiction_title()
        print("小说名：{}".format(self.fiction_title))
        self.chapter_list = self.get_fiction_chapter_list()
        print("章节数：{}".format(len(self.chapter_list)))

    def get_fiction_chapter_list(self):
        chapter_a_list = self.fiction_html.xpath('//div[@id="list"]//a')
        chapter_list = [{'title': chapter_a.text, 'href': chapter_a.get('href')} for chapter_a in chapter_a_list]
        return chapter_list

    def get_fiction_title(self):
        return self.fiction_html.xpath('//div[@id="info"]/h1//text()')[0]

    def get_fiction_chapter(self, index):
        if len(self.chapter_list) <= index:
            print("没有更多章节了")
            return None
        else:
            chapter_dict = self.chapter_list[index]
            chapter_page_res = requests.get(self.config.url_prefix + chapter_dict['href'])
            chapter_html = Fiction.parse_html(chapter_page_res)
            content = chapter_html.xpath('//div[@id="content"]//text()')
            content_format = Fiction.filter_ad(Fiction.format_chapter(content))
            return content_format

    def get_fiction_chapter_title(self, index):
        if len(self.chapter_list) <= index or index < 0:
            print("没有更多章节了")
            return None
        else:
            return self.chapter_list[index]['title']

    @classmethod
    def parse_html(cls, res):
        res.encoding = 'utf-8'
        return etree.HTML(res.text)

    @classmethod
    def format_chapter(cls, content):
        return "\n".join(["".join(x.split()) for x in content])

    @classmethod
    def filter_ad(cls, content):
        return content.replace("手机站全新改版升级地址：http://m.xbiquge.la，数据和书签与电脑站同步，无广告清新阅读！", "") \
            .replace("亲,点击进去,给个好评呗,分数越高更新越快,据说给新笔趣阁打满分的最后都找到了漂亮的老婆哦!", "")
