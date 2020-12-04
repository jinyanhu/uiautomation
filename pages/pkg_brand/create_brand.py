from selenium.common.exceptions import NoSuchWindowException
from pages.base_page import BasePage
from utils.page_factory_util import page_element_factory
import redis
import json
from utils.http_util import Http


__author__ = "zxf"
__desc__ = "品牌查询Page"


class CreateBrand(BasePage):
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
        name_list = ["input_brandno_locator",
                     "input_brandname_locator","input_prefix_locator",
                     "input_customer_locator","select_customer_locator",
                     "input_address_locator","input_recipient_locator",
                     "input_phone_locator","input_ratio_locator",
                     "button_enable_locator","button_save_locator",
                     "input_vendor_locator","select_level_locator"]

        ele_dic = page_element_factory(self.xml_file, name_list)

        #品牌编码输入
        self.input_brandno_locator = ele_dic["input_brandno_locator"]
        #品牌名称输入
        self.input_brandname_locator = ele_dic["input_brandname_locator"]
        #前缀输入
        self.input_prefix_locator = ele_dic["input_prefix_locator"]
        #供应商的等级
        self.input_vendor_locator = ele_dic["input_vendor_locator"]
        #选择供应商等级
        self.select_level_locator = ele_dic["select_level_locator"]
        #销售客户
        self.input_customer_locator = ele_dic["input_customer_locator"]
        #选择销售客户
        self.select_customer_locator = ele_dic["select_customer_locator"]
        #地址输入
        self.input_address_locator = ele_dic["input_address_locator"]
        #联系人输入
        self.input_recipient_locator = ele_dic["input_recipient_locator"]
        #电话输入
        self.input_phone_locator = ele_dic["input_phone_locator"]
        #倍率输入
        self.input_ratio_locator = ele_dic["input_ratio_locator"]
        #启用按钮
        self.button_enable_locator = ele_dic["button_enable_locator"]
        #保存按钮
        self.button_save_locator = ele_dic["button_save_locator"]

    def is_loaded(self):
        pass

    def input_brand_number(self, brand_no):
        """
        输入品牌编码
        :param brand_no:
        :return:
        """
        self.browser_action.send_keys(self.input_brandno_locator, brand_no)

    def input_brand_name(self,brandname):
        '''
        输入品牌名称
        :param brandname:
        :return:
        '''
        self.browser_action.send_keys(self.input_brandname_locator,brandname,self.input_brandname_locator[2])

    def input_prefix(self,prefix):
        '''
        输入品牌前缀
        :param prefix:
        :return:
        '''
        self.browser_action.send_keys(self.input_prefix_locator,prefix,self.input_prefix_locator[2])

    def select_vendor_level(self,vendor_level):
        '''
        选择最低供应商等级
        :param level:供应商等级
        :return:
        '''
        self.browser_action.click(self.input_vendor_locator, self.input_vendor_locator[2])
        self.browser_action.click(self.select_level_locator, [vendor_level])

    def select_customer(self,customer):
        '''
        选择销售客户
        :param customer:
        :return:
        '''
        self.browser_action.click(self.input_customer_locator, [self.input_customer_locator[2]])
        self.browser_action.click(self.select_customer_locator, [customer])

    def input_address(self,address,phone,ratio):
        '''
        输入收货地址、电话和倍率
        :param address:
        :return:
        '''
        self.browser_action.send_keys(self.input_address_locator,address,[self.input_address_locator[2]])

        self.browser_action.send_keys(self.input_phone_locator,phone,[self.input_phone_locator[2]])
        self.browser_action.send_keys(self.input_ratio_locator, ratio, [self.input_ratio_locator[2]])

    def input_recipient(self,recipient):
        '''
        输入收货人
        :param recipient:
        :return:
        '''
        self.browser_action.send_keys(self.input_recipient_locator, recipient, [self.input_recipient_locator[2]])

    def click_enable(self):
        '''
        点击启用按钮和保存按钮
        :return:
        '''
        self.browser_action.click(self.button_enable_locator)
        self.browser_action.click(self.button_save_locator)

    def verify_button_element(self):
        '''
        验证保存按钮是否还存在
        :return:
        '''
        return self.browser_action.is_element_present(self.button_enable_locator)
