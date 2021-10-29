from pynput import keyboard

from keyboard_registry import registry
from pages.page import print_content, Page
from router import router


class ContentPage(Page):
    def __init__(self):
        registry.register(keyboard.Key.left, self.handle_return)

    def handle_return(self):
        router.pop()

    def on_destroy(self):
        registry.cancel_register(keyboard.Key.left, self.handle_return)

    @print_content
    def print(self):
        return '456'
