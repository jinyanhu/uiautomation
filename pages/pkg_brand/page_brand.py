from selenium.common.exceptions import NoSuchWindowException
from pages.base_page import BasePage
from utils.page_factory_util import page_element_factory
import redis
import json
from utils.http_util import Http


__author__ = "zxf"
__desc__ = "品牌查询Page"


class PageBrand(BasePage):
    """
    品牌查询Page
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
        name_list = ["input_state_locator","select_state_locator",
                     "input_brand_no_locator","button_query_locator",
                     "table_first_locator"]

        ele_dic = page_element_factory(self.xml_file, name_list)
        #状态选择文本框
        self.input_state_locator = ele_dic["input_state_locator"]
        #状态选择下拉框
        self.select_state_locator = ele_dic["select_state_locator"]
        # 品牌编码输入框
        self.input_brand_no_locator = ele_dic["input_brand_no_locator"]
        # 查询按钮
        self.button_query_locator = ele_dic["button_query_locator"]
        #第二行数据
        self.table_first_locator = ele_dic["table_first_locator"]

    def is_loaded(self):
        pass

    def select_state(self, state):
        """
        选择品牌状态:0启用，1禁用
        :return:
        """
        self.browser_action.click(self.input_state_locator, self.input_state_locator[2])
        self.browser_action.click(self.select_state_locator, [state])

    def input_brand_no(self, brandno):
        """
        输入品牌编码
        :param brandno:
        :return:
        """
        self.browser_action.send_keys(self.input_brand_no_locator, brandno)

    def click_button_query(self):
        """
        点击查询按钮
        :return:
        """
        self.browser_action.click(self.button_query_locator,self.button_query_locator[2])

    def get_table_text(self,row,column):
        '''

        :param row: 表格的第几行
        :param column: 行的第几列
        :return: 对应行列的文本值
        '''
        return self.browser_action.get_table_col_text_by_row_col_not_header(self.table_first_locator,row,column)



