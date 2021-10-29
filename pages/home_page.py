from router import router
from pages.content_page import ContentPage
from pages.page import Page, print_content
from pynput import keyboard
from keyboard_registry import registry
from adapter import get_adapter
from config import app_config
from controller import get_controller


class HomePage(Page):
    def __init__(self):
        registry.register(keyboard.Key.right, self.handle_read)

    def handle_read(self):
        router.push(ContentPage())

    def on_destroy(self):
        registry.cancel_register(keyboard.Key.right, self.handle_read)

    @print_content
    def print(self):
        content = '=====Fiction Console Reader=====\n'
        adapter = get_adapter()
        content += '当前小说:《{0}》\n'.format(adapter.get_fiction_title())
        content += '上次读到:{0}\n'.format(adapter.get_fiction_chapter_list()[app_config.current_chapter_index]['title'])
        content += '总共{0}章节，本书进度{1}%'.format(len(adapter.get_fiction_chapter_list()),
                                             app_config.current_chapter_index / len(adapter.get_fiction_chapter_list()))
        content += get_controller(self.__class__.__name__)
        return content
