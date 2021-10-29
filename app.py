from pages.home_page import HomePage
from router import router
from pynput import keyboard
from keyboard_registry import registry
from util import clear


def handle_exit():
    clear()
    exit(0)


def register_app_listener():
    registry.register(keyboard.Key.esc, handle_exit)


if __name__ == '__main__':
    register_app_listener()
    home_page = HomePage()
    router.push(home_page)

with keyboard.Listener(on_press=registry.dispatch) as listener:
    listener.join()
