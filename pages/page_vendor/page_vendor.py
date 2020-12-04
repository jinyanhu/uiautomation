from selenium.common.exceptions import NoSuchWindowException
from pages.base_page import BasePage
from utils.page_factory_util import page_element_factory
from base.browser_action import BrowserAction
import redis
import json
from utils.http_util import Http


__author__ = "zzh"
__desc__ = "登录Page"


class PageVendor(BasePage):
    """
    供应商Page
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
        name_list = [
            "input_vendor_code_locator",
            "input_short_code_locator",
            "input_state_locator",
            "select_state_locator",
            "input_query_locator",
            "input_code_locator",
            "input_name_locator",
            "input_short_name_locator",
            "input_sort_locator",
            "select_sort_locator",
            "input_linkman_locator",
            "input_telephone_locator",
            "input_address_locator",
            "input_submit_locator"

        ]

        ele_dic = page_element_factory(self.xml_file, name_list)
        # 供应商编码输入框
        self.input_vendor_code_locator = ele_dic["input_vendor_code_locator"]

        # 供应商简称输入框
        self.input_short_code_locator = ele_dic["input_short_code_locator"]

        # 状态文本框
        self.input_state_locator = ele_dic["input_state_locator"]

        # 启用禁用状态下拉框
        self.select_state_locator = ele_dic["select_state_locator"]

        # 查询点击框
        self.input_query_locator = ele_dic["input_query_locator"]

        # 录入页面供应商编码输入框
        self.input_code_locator = ele_dic["input_code_locator"]

        # 录入页面供应商名称输入框
        self.input_name_locator = ele_dic["input_name_locator"]

        # 录入页面供应商简称输入框
        self.input_short_name_locator = ele_dic["input_short_name_locator"]

        # 录入页面所属来源文本框
        self.input_sort_locator = ele_dic["input_sort_locator"]

        # 录入页面供应商所属分类选择框
        self.select_sort_locator = ele_dic["select_sort_locator"]

        # 录入页面联系人1输入框
        self.input_linkman_locator = ele_dic["input_linkman_locator"]

        # 录入页面手机1输入框
        self.input_telephone_locator = ele_dic["input_telephone_locator"]

        # 录入页面地址1输入框
        self.input_address_locator = ele_dic["input_address_locator"]

        # 录入页面提交按钮点击框
        self.input_submit_locator = ele_dic["input_submit_locator"]

    def is_loaded(self):
        pass

    def input_vendor_code(self, vendor_code):
        '''
        输入供应商编码
        :param vendor_code:
        :return:
        '''
        self.browser_action.send_keys(self.input_vendor_code_locator, vendor_code, self.input_vendor_code_locator[2])

    def input_vendor_short_code(self, vendor_short_code):
        '''
        输入供应商简称
        :param vendor_short_code:
        :return:
        '''
        self.browser_action.send_keys(self.input_short_code_locator, vendor_short_code, self.input_short_code_locator[2])

    def select_state(self, state):
        '''
        选择供应商状态:1启用，0禁用
        :param state:
        :return:
        '''
        self.browser_action.click(self.input_state_locator, self.input_state_locator[2])
        self.browser_action.click(self.select_state_locator, [state])

    def cliet_query(self):
        '''
        点击查询按钮
        :return:
        '''
        self.browser_action.click(self.input_query_locator, self.input_query_locator[2])

    def vendor_code(self, code):
        '''
        输入供应商编码
        :return:
        '''
        self.browser_action.send_keys(self.input_code_locator, code, self.input_code_locator[2])

    def name(self, name):
        '''
        输入供应商名称
        :return:
        '''
        self.browser_action.send_keys(self.input_name_locator, name, self.input_name_locator[2])

    def short_name(self, short_name):
        """
        输入供应商简称
        :return:
        """
        self.browser_action.send_keys(self.input_short_name_locator, short_name, self.input_short_name_locator[2])

    def select_sort(self, sort):
        '''
        所属分类选择文本框
        :return:
        '''
        self.browser_action.click(self.input_sort_locator, self.input_sort_locator[2])
        self.browser_action.click(self.select_sort_locator, [sort])

    def linkman(self, linkman):
        '''
        联系人1输入框
        :param linkman:
        :return:
        '''
        self.browser_action.send_keys(self.input_linkman_locator, linkman, self.input_linkman_locator[2])

    def telephone(self, telephone):
        '''
        手机1输入框
        :param :
        :return:
        '''
        self.browser_action.send_keys(self.input_telephone_locator, telephone, self.input_telephone_locator[2])

    def add_address(self, address):
        '''
        地址1输入框
        :param :
        :return:
        '''
        self.browser_action.send_keys(self.input_address_locator, address, [self.input_address_locator[2]])

    def submit_query(self):
        '''
        提交按钮
        :return:
        '''
        self.browser_action.click(self.input_submit_locator, self.input_submit_locator[2])





