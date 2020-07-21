from controller import Controller, Mode
from pynput import keyboard

controller = Controller()
controller.print_home()


def on_press(key):
    if isinstance(key, keyboard.KeyCode):
        key = key.char
    if key == 'w' or key == keyboard.Key.up:
        if controller.mode == Mode.Home or controller.mode == Mode.Fiction:
            controller.last_page()
        if controller.mode == Mode.Catalog:
            controller.show_chapter_last()
    elif key == 's' or key == keyboard.Key.down:
        if controller.mode == Mode.Home or controller.mode == Mode.Fiction:
            controller.next_page()
        if controller.mode == Mode.Catalog:
            controller.show_chapter_next()
    elif key == keyboard.Key.left:
        if controller.mode == Mode.Fiction:
            controller.print_home()
    elif key == keyboard.Key.right:
        controller.show_chapter_next()
    elif key == keyboard.Key.esc:
        print('Bye bye ~')
        return False


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
