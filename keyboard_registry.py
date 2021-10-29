from pynput import keyboard


class KeyboardRegistry:

    def __init__(self):
        self.keyboard_registry = {}

    def register(self, code, func):
        if code not in self.keyboard_registry:
            self.keyboard_registry[code] = []
        self.keyboard_registry[code].append(func)

    def cancel_register(self, code, func):
        if code in self.keyboard_registry:
            self.keyboard_registry[code].remove(func)

    def dispatch(self, key):
        if isinstance(key, keyboard.KeyCode):
            key = key.char
        if key in self.keyboard_registry:
            for f in self.keyboard_registry[key]:
                f()


registry = KeyboardRegistry()
