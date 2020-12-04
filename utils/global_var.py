__author__ = "zzh"


class GlobalVarClass(object):
    # 设置日志文件名称
    log_file = ''

    # 截图路径
    screenshot_path = ''

    # 当前运行的用例名称
    case_name = ''

    # 当前运行用例的时间
    now_time = ''

    # 用例出错，重新运行该用例的次数
    case_error_num = 0

    # 错误用例录屏路径
    video_path = ''

    # 当前错误用例是第几次运行
    now_error_num = 0

    # case运行的平台环境
    case_platform = ""

    # page运行的平台环境
    page_platform = ""

    # 设备device对应的device_name
    device_name = ""

    # 循环用变量
    circle_num = 1

    # android/ios
    platform = "android"

    # 当前运行的第几个用例
    now_case_time = 1

    def __init__(self):
        pass

    @staticmethod
    def set_log_file(log_file):
        GlobalVarClass.log_file = log_file

    @staticmethod
    def get_log_file():
        return GlobalVarClass.log_file

    @staticmethod
    def set_screenshot_path(screenshot_path):
        GlobalVarClass.screenshot_path = screenshot_path

    @staticmethod
    def get_screenshot_path():
        return GlobalVarClass.screenshot_path

    @staticmethod
    def set_case_name(case_name):
        GlobalVarClass.case_name = case_name

    @staticmethod
    def get_case_name():
        return GlobalVarClass.case_name

    @staticmethod
    def set_now_time(now_time):
        GlobalVarClass.now_time = now_time

    @staticmethod
    def get_now_time():
        return GlobalVarClass.now_time

    @staticmethod
    def set_case_error_num(case_error_num):
        GlobalVarClass.case_error_num = case_error_num

    @staticmethod
    def get_case_error_num():
        return GlobalVarClass.case_error_num

    @staticmethod
    def set_video_path(video_path):
        GlobalVarClass.video_path = video_path

    @staticmethod
    def get_video_path():
        return GlobalVarClass.video_path

    @staticmethod
    def set_now_error_num(now_error_num):
        GlobalVarClass.now_error_num = now_error_num

    @staticmethod
    def get_now_error_num():
        return GlobalVarClass.now_error_num

    @staticmethod
    def set_case_platform(case_platform):
        GlobalVarClass.case_platform = case_platform

    @staticmethod
    def get_case_platform():
        return GlobalVarClass.case_platform

    @staticmethod
    def set_page_platform(page_platform):
        GlobalVarClass.page_platform = page_platform

    @staticmethod
    def get_page_platform():
        return GlobalVarClass.page_platform

    @staticmethod
    def set_device_name(device_name):
        GlobalVarClass.device_name = device_name

    @staticmethod
    def get_device_name():
        return GlobalVarClass.device_name

    @staticmethod
    def set_circle_num(circle_num):
        GlobalVarClass.circle_num = circle_num

    @staticmethod
    def get_circle_num():
        return GlobalVarClass.circle_num

    @staticmethod
    def set_platform(platform):
        GlobalVarClass.platform = platform

    @staticmethod
    def get_platform():
        return GlobalVarClass.platform

    @staticmethod
    def set_now_case_time(now_case_time):
        GlobalVarClass.now_case_time = now_case_time

    @staticmethod
    def get_now_case_time():
        return GlobalVarClass.now_case_time
