from selenium.common.exceptions import NoSuchWindowException
from pages.base_page import BasePage
from utils.page_factory_util import page_element_factory
import redis
import json
import time
from hamcrest import *
from utils.http_util import Http


__author__ = "zzh"
__desc__ = "登录Page"


class PageLogin(BasePage):
    """
    登录Page
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        try:
            self.initial_element()
        except Exception as e:
            raise

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            raise
        pass

    def page_factory(self):
        name_list = ["input_company_locator",
                     "select_company_locator",
                     "input_username_locator",
                     "input_password_locator",
                     "input_verify_code_locator",
                     "button_login_locator"]

        ele_dic = page_element_factory(self.xml_file, name_list)
        # 企业和非企业选择文本框
        self.input_company_locator = ele_dic["input_company_locator"]
        # 企业和非企业选择下拉框
        self.select_company_locator = ele_dic["select_company_locator"]
        # 用户名文本框
        self.input_username_locator = ele_dic["input_username_locator"]
        # 密码文本框
        self.input_password_locator = ele_dic["input_password_locator"]
        # 验证码文本框
        self.input_verify_code_locator = ele_dic["input_verify_code_locator"]
        # 登录按钮
        self.button_login_locator = ele_dic["button_login_locator"]

    def is_loaded(self):
        pass

    def select_company(self, company_index):
        """
        选择企业和非企业登录:0企业，1非企业
        :return:
        """
        self.browser_action.click(self.input_company_locator, self.input_company_locator[2])
        self.browser_action.click(self.select_company_locator, [company_index])

    def input_username(self, username):
        """
        输入用户名
        :param username:
        :return:
        """
        self.browser_action.send_keys(self.input_username_locator, username, self.input_username_locator[2])

    def input_password(self, password):
        """
        输入密码
        :param password:
        :return:
        """
        self.browser_action.send_keys(self.input_password_locator, password, self.input_password_locator[2])

    def input_verify_code(self):
        """
        输入验证码
        :param url:
        :return:
        """
        # rd = redis.Redis(host='10.228.81.233', port=6379, db=1)
        # http = Http()
        # res = http.get(url + "verify_code")
        # res_json = json.loads(res.text)
        # token = res_json["obj"]["token"]
        # verify_code = rd.get("verifyCodeToken:" + token).decode("utf-8")
        self.browser_action.send_keys(self.input_verify_code_locator, "zhihe666", self.input_verify_code_locator[2])

    def click_button_login(self):
        """
        点击登录按钮
        :return:
        """
        self.browser_action.click(self.button_login_locator)

    def verify_username_element_exist(self):
        """
        验证用户名输入框控件是否存在
        :return:
        """
        return self.browser_action.is_element_present(self.input_username_locator)

    def login_common(self, url, company_index, username, password):
        """
        登录的公共方法
        :param url:
        :param company_index:
        :param username:
        :param password:
        :return:
        """
        self.driver.get(url)
        self.select_company(company_index)
        self.input_username(username)
        self.input_password(password)
        self.input_verify_code()
        self.click_button_login()
        time.sleep(3)
        assert_that(self.verify_username_element_exist(), equal_to(False))





