import json


class Config:
    config_filename = 'fiction.json'

    def __init__(self):
        with open(self.config_filename, 'r') as config_file:
            raw_data = config_file.readlines()
            config_dict = json.loads("".join(raw_data))
            '''文章目录页'''
            self.fiction_url = config_dict['fiction_url']
            '''章节下标'''
            self.fiction_index = config_dict['fiction_index']
            '''笔趣阁主页'''
            self.url_prefix = config_dict['url_prefix']
            '''每页行数'''
            self.line_limit = config_dict['line_limit']
            '''编码'''
            self.encoding = config_dict['encoding']

        if self.fiction_url is None:
            print("请配置小说目录页")
        if self.fiction_index is None:
            self.fiction_index = 0
        print("配置加载完毕")
        print(self.to_string())

    def next_page(self):
        self.fiction_index += 1
        with open(self.config_filename, 'w') as config_file:
            config_file.write(json.dumps(self.to_json()))

    def last_page(self):
        self.fiction_index -= 1
        with open(self.config_filename, 'w') as config_file:
            config_file.write(json.dumps(self.to_json()))

    def to_json(self):
        return {
            'fiction_url': self.fiction_url,
            'fiction_index': self.fiction_index,
            'url_prefix': self.url_prefix,
            'line_limit': self.line_limit,
            'encoding':self.encoding
        }

    def to_string(self):
        return '小说源:{url_prefix}\n主页:{fiction_url}\n每页行数:{line_limit}\n编码:{encoding}\n'.format(**self.to_json())


config = Config()
