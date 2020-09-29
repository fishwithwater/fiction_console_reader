from lxml import etree
from config import config

def parse_html(res):
    res.encoding = config.encoding
    return etree.HTML(res.text)


def format_chapter(content):
    return ["".join(x.split()) for x in content]


def filter_ad(content):
    return content.replace("手机站全新改版升级地址：http://m.xbiquge.la，数据和书签与电脑站同步，无广告清新阅读！", "") \
        .replace("亲,点击进去,给个好评呗,分数越高更新越快,据说给新笔趣阁打满分的最后都找到了漂亮的老婆哦!", "") \
        .replace("(千载中文-.提供最新章节阅读>", "")


def filter_ads(content_list):
    return list(map(filter_ad, content_list))


def format_print(content_list):
    return "\n".join(content_list)


def format_catalog(current_page_chapter_list, limit):
    res_str = ''
    maxlen = max(len(x['title']) for x in current_page_chapter_list)
    for i in range(limit):
        if i % 3 == 0 and i != 0:
            res_str += '\n'
        res_str += ('{0:{1}<' + str(maxlen) + '}\t').format(current_page_chapter_list[i]['title'], chr(12288))
    return res_str
