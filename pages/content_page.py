from pynput import keyboard

from controller import get_controller
from keyboard_registry import registry
from pages.page import print_content, Page
from router import router
from adapter import get_adapter
from config import app_config
from filter import filter_ads, filter_blank_lines


class ContentPage(Page):
    def __init__(self):
        registry.register(keyboard.Key.left, self.handle_return)
        registry.register(keyboard.Key.down, self.handle_next_page)
        self.content = filter_blank_lines(
            filter_ads(get_adapter().get_fiction_chapter_content(app_config.current_chapter_index)))

    def handle_next_page(self):
        pass

    def handle_return(self):
        router.pop()

    def on_destroy(self):
        registry.cancel_register(keyboard.Key.left, self.handle_return)
        registry.cancel_register(keyboard.Key.down, self.handle_next_page)

    @print_content
    def print(self):
        content = ''
        for line in self.content[app_config.current_chapter_line_index:app_config.line_size]:
            content += line
            content += '\n'
        content += get_controller(self.__class__.__name__)
        return content
