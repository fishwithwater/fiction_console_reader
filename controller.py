def get_controller(page):
    if page == 'HomePage':
        return get_home_controller()


def get_home_controller():
    return '\n===[ESC]退出\t[↓]继续阅读\t[→]查看目录===\n'
