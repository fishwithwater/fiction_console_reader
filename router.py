import pages.page as p


class Router:
    def __init__(self, page=None):
        self.page_stack = []
        if page is not None:
            self.push(page)

    def push(self, page):
        if page is None:
            pass
        self.page_stack.append(page)
        page.print()

    def pop(self):
        if len(self.page_stack) == 0:
            pass
        old_page = self.page_stack.pop()
        if (isinstance(old_page, p.Page)):
            old_page.on_destroy()
        self.page_stack[-1].print()

    def current_route(self):
        return self.page_stack[len(self.page_stack) - 1]


router = Router()
