import time
from hamcrest import *
from pages.pkg_login.page_login import PageLogin
from pages.pkg_brand.create_brand import CreateBrand
from testcases.base_test_case import BaseTestCase
from testcases.main.pkg_brand.data_brand import DataBrand



__author__ = ""
__desc__ = ""


class TestCreateBrand(BaseTestCase):
    """
    品牌测试用例
    """
    def setUp(self):
        BaseTestCase.setUp(self)
        # 初始化page
        self.page_login = PageLogin(self.driver)
        self.create_brand = CreateBrand(self.driver)

    def test_brand(self):
        """
        成功创建品牌
        :return:
        """

        self.page_login.login_common(DataBrand.url,DataBrand.company,DataBrand.username,DataBrand.password)
        self.driver.get(DataBrand.creatbrandurl)
        self.create_brand.input_brand_number(DataBrand.brand_no)
        self.create_brand.select_vendor_level(DataBrand.vendor_level)
        self.create_brand.input_brand_name(DataBrand.brand_name)
        self.create_brand.input_prefix(DataBrand.prefix)
        self.create_brand.select_customer(DataBrand.customer)
        self.create_brand.input_address(DataBrand.address,DataBrand.phone,DataBrand.ratio)
        self.create_brand.input_recipient(DataBrand.recipient)
        self.create_brand.click_enable()
        assert_that(self.create_brand.verify_button_element(),equal_to(False))

    def tearDown(self):
        pass




