import traceback
import time
import re
from utils.decorate_util import action_decorate
from base.element import get_element
from base.element import get_elements
from utils.global_var import GlobalVarClass
from utils.logger_util import run_info_log
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

__author__ = "zzh"


class AppAction(object):
    def __init__(self, driver):
        self.driver = driver

    def log_screenshot(self, e=None):
        screenshot_file = GlobalVarClass.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
        self.driver.save_screenshot(GlobalVarClass.get_screenshot_path() + screenshot_file)
        print("        错误截图：")
        print('        <img src="http://192.168.200.171:8020/screenshot/' + screenshot_file + '" width="400px" />')
        run_info_log(str(traceback.format_exc()), GlobalVarClass.get_log_file())
        run_info_log(e, GlobalVarClass.get_log_file())

    def catch_exception(self, e):
        """
        操作方法异常处理
        :param e:
        :return:
        """
        self.log_screenshot(e)
        raise Exception()

    @action_decorate
    def is_element_present(self, locator):
        """
        判断当前元素是否存在
        :param locator: 操作的控件,["ID", "root"]
        :return: True or False
        """
        try:
            get_element(self.driver, locator)
            return True
        except Exception as e:
            self.log_screenshot(e)
            return False
        pass
