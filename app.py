from config import Config
from fiction import Fiction
from controller import Controller
from pynput import keyboard
import os

config = Config()
fiction = Fiction(config)
controller = Controller(config, fiction)
controller.next_page()
controller.print_controller()

def clear():
    os.system('cls')

def on_press(key):
    if isinstance(key, keyboard.KeyCode):
        key = key.char
    if key == keyboard.Key.up:
        clear()
        controller.last_page()
        controller.print_controller()
    elif key == keyboard.Key.down:
        clear()
        controller.next_page()
        controller.print_controller()
    elif key == keyboard.Key.esc:
        print('Bye bye ~')
        return False

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
