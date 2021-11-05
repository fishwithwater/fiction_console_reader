def get_controller(page):
    if page == 'HomePage':
        return get_home_controller()
    elif page == 'ContentPage':
        return get_content_controller()


def get_content_controller():
    return '\n===[ESC]退出\t[↑]上一页\t[↓]下一页\t[→]查看目录===\n'


def get_home_controller():
    return '\n===[ESC]退出\t[↓]继续阅读\t[→]查看目录===\n'
