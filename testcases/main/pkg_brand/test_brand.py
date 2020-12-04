import time
from hamcrest import *
from pages.pkg_login.page_login import PageLogin
from pages.pkg_brand.page_brand import PageBrand
from testcases.base_test_case import BaseTestCase
from testcases.main.pkg_brand.data_brand import DataBrand



__author__ = ''
__desc__ = ""


class TestBrand(BaseTestCase):
    """
    品牌测试用例
    """
    def setUp(self):
        BaseTestCase.setUp(self)

        # 初始化page
        self.page_login = PageLogin(self.driver)
        self.page_brand = PageBrand(self.driver)

    def test_brand(self):
        """
        成功查询到品牌
        """

        self.page_login.login_common(DataBrand.url,DataBrand.company,DataBrand.username,DataBrand.password)
        self.driver.get(DataBrand.brandurl)
        self.page_brand.select_state(DataBrand.state)
        self.page_brand.input_brand_no(DataBrand.brandno)
        self.page_brand.click_button_query()
        result = self.page_brand.get_table_text(DataBrand.row, DataBrand.column)
        assert_that(result,equal_to("00019"))

    def tearDown(self):
        pass




