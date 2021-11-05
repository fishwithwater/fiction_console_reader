import json

config_name = 'fiction.json'


class Config:
    def __init__(self, jsonData=None):
        self.source_website = ''
        self.fiction_index_url = ''
        self.encode = 'utf-8'
        self.line_size = 10
        self.current_chapter_index = 0
        self.current_chapter_line_index = 0
        self.ads = []
        if jsonData is not None:
            self.__dict__ = jsonData

    def __str__(self):
        return str(self.__dict__)

    def change_chapter_line(self, index):
        self.current_chapter_line_index = index

    def change_chapter(self, index):
        self.current_chapter_index = index
        self.current_chapter_line_index = 0

    def persistent(self):
        with open(self.config_filename, 'w') as config_file:
            config_file.write(json.dumps(self.__dict__))


def read_config():
    with open(config_name, 'r') as config_file:
        raw_data = config_file.readlines()
        config_dict = json.loads("".join(raw_data))
        config = Config(config_dict)
        return config


app_config = read_config()
