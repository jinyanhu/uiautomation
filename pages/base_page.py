import abc
import sys
import time
import importlib
import inspect
from selenium.common.exceptions import NoSuchElementException
from utils.global_var import GlobalVarClass
from base.browser_action import BrowserAction


def platform(platform_name):
    """
    平台装饰器
    :param platform_name: ios/android/browser
    :return:
    应用example：
        @platform("ios")
        def login_ios():
            print("ios")

        @platform("android")
        def login_android():
            print("android")

        @platform("browser")
        def login_browser():
            print("browser")

        if __name__ == "__main__":
            # 只需要调用3个login其中的一个，就可以根据运行平台自动识别运行哪个函数
            login_ios()
    """
    def _platform(func):
        def __platform(*args, **kwargs):
            if func.__name__.find(GlobalVarClass.get_platform()) >= 0:
                func(*args, **kwargs)
            elif func.__name__.find("all") >= 0 and GlobalVarClass.get_circle_num() > 1:
                func(*args, **kwargs)
            else:
                GlobalVarClass.set_circle_num(GlobalVarClass.get_circle_num() + 1)
                cls = args[0]
                func_name = func.__name__.replace(platform_name, GlobalVarClass.get_platform())
                new_args = list(args)
                new_args.pop(0)
                try:
                    getattr(cls, func_name)(*new_args, **kwargs)
                except Exception as e:
                    func_name = func.__name__.replace(platform_name, "all")
                    getattr(cls, func_name)(*new_args, **kwargs)
                    GlobalVarClass.set_circle_num(1)
                pass
        return __platform
    return _platform


def compatible(device_name):
    """
    设备兼容性装饰器
    :param device_name:
    :return:
    应用example：
        @compatible("huawei6")
        def login_huawei6():
            print("huawei6")

        @compatible("hongmi")
        def login_hongmi():
            print("hongmi")

        @compatible("all")
        def login_all():
            print("all")

        if __name__ == "__main__":
            # 只需要调用3个login其中的一个，就可以根据运行设备自动识别运行哪个函数
            login_hongmi()
    """
    def _compatible(func):
        def __compatible(*args, **kwargs):
            if func.__name__.find(GlobalVarClass.get_device_name()) >= 0:
                func(*args, **kwargs)
            elif func.__name__.find("all") >= 0 and GlobalVarClass.get_circle_num() > 1:
                func(*args, **kwargs)
            else:
                GlobalVarClass.set_circle_num(GlobalVarClass.get_circle_num() + 1)
                cls = args[0]
                func_name = func.__name__.replace(device_name, GlobalVarClass.get_device_name())
                new_args = list(args)
                new_args.pop(0)
                try:
                    getattr(cls, func_name)(*new_args, **kwargs)
                except Exception as e:
                    func_name = func.__name__.replace(device_name, "all")
                    getattr(cls, func_name)(*new_args, **kwargs)
                    GlobalVarClass.set_circle_num(1)
                pass
        return __compatible
    return _compatible


class BasePage(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver, filename):
        self.screen_shot_name = __name__
        self.driver = driver
        self.browser_action = BrowserAction(driver)

        # if self.is_run_ios():
        #     self.xml_file = filename[:filename.rfind(".")] + "IOS.xml"
        #     self.standard_xml_file = filename[:filename.rfind(".")] + "_ios.xml"
        # else:
        #     self.xml_file = filename[:filename.rfind(".")] + "Android.xml"
        #     self.standard_xml_file = filename[:filename.rfind(".")] + "_android.xml"

        self.xml_file = filename[:filename.rfind(".")] + ".xml"

        try:
            self.is_loaded()
        except NoSuchElementException:
            pass
        finally:
            pass

    def screen_shot(self):
        self.driver.save_screenshot(self.screen_shot_name)
        pass

    @abc.abstractmethod
    def is_loaded(self):
        """
        判断是否是当前页面
        """
        pass

    @abc.abstractmethod
    def page_factory(self):
        pass

    @abc.abstractmethod
    def initial_element(self):
        pass




