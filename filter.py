from config import app_config


def filter_blank_lines(content_list):
    return list(filter(lambda x: x.strip() != '', content_list))


def __filter_ad(content):
    for ad in app_config.ads:
        content = content.replace(ad)
    return content


def filter_ads(content_list):
    return list(map(__filter_ad, content_list))
