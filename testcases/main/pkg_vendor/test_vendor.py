import time
from hamcrest import *
from pages.pkg_login.page_login import PageLogin
from testcases.base_test_case import BaseTestCase
from testcases.main.pkg_vendor.date_vendor import DataVendor
from pages.page_vendor.page_vendor import PageVendor


__author__ = 'zzh'
__desc__ = "登录"


class TestVendor(BaseTestCase):
    """
    登录测试用例
    """
    def setUp(self):
        BaseTestCase.setUp(self)

        # 初始化page
        self.page_login = PageLogin(self.driver)
        self.page_vendor = PageVendor(self.driver)

    def test_login_success(self):
        """
        成功登录
        """
        self.page_login.login_common(DataVendor.url,DataVendor.company,DataVendor.username,DataVendor.password)
        time.sleep(2)
        """
        新增供应商
        """
        self.driver.get(DataVendor.vendor_url1)
        time.sleep(5)
        self.page_vendor.vendor_code(DataVendor.code)
        time.sleep(1)
        self.page_vendor.name(DataVendor.name)
        time.sleep(1)
        self.page_vendor.short_name(DataVendor.short_name)
        time.sleep(1)
        self.page_vendor.select_sort(DataVendor.sort)
        time.sleep(1)
        self.page_vendor.linkman(DataVendor.linkman)
        time.sleep(1)
        self.page_vendor.telephone(DataVendor.telephone)
        time.sleep(5)
        self.page_vendor.add_address(DataVendor.address)
        time.sleep(5)
        self.page_vendor.submit_query()
        time.sleep(20)
        """
        查询供应商
        """
        self.driver.get(DataVendor.vendor_url)
        time.sleep(2)
        self.page_vendor.input_vendor_code(DataVendor.vendor_code)
        time.sleep(1)
        self.page_vendor.input_vendor_short_code(DataVendor.vendor_short_code)
        time.sleep(1)
        self.page_vendor.select_state(DataVendor.state)
        time.sleep(1)
        self.page_vendor.cliet_query()
        time.sleep(5)

    def tearDown(self):
        pass




