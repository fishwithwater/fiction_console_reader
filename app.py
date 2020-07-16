from config import Config
from fiction import Fiction
from controller import Controller,Mode
from pynput import keyboard

config = Config()
fiction = Fiction(config)
controller = Controller(config, fiction)
controller.print_home()


def on_press(key):
    if isinstance(key, keyboard.KeyCode):
        key = key.char
    if key == keyboard.Key.up:
        controller.last_page()
    elif key == keyboard.Key.down:
        if controller.mode == Mode.Home or controller.mode == Mode.Fiction:
            controller.next_page()
    elif key == keyboard.Key.left:
        if controller.mode == Mode.Fiction:
            controller.print_home()
    elif key == keyboard.Key.esc:
        print('Bye bye ~')
        return False


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
