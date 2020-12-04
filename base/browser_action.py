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


class BrowserAction(object):
    def __init__(self, driver):
        self.driver = driver

    def log_screenshot(self, e=None):
        screenshot_file = GlobalVarClass.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
        self.driver.save_screenshot(GlobalVarClass.get_screenshot_path() + screenshot_file)
        print("        错误截图：")
        print('        <img src="http://10.228.86.103:8222/screenshot/' + screenshot_file + '" width="400px" />')
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
    def execute_script(self, script):
        """
        调用WebDriver的execute_script方法，执行js脚本;
        :param script:
        :return:
        """
        try:
            res = self.driver.execute_script(script)
            return res
        except Exception as e:
            self.log_screenshot(e)
            return None
        pass

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
            return False
        pass

    def is_elements_present(self, locator):
        """
        判断当前元素列表是否存在
        :param locator: 操作的控件,["tag_name", "input"]
        :return: True or False
        """
        try:
            get_elements(self.driver, locator)
            return True
        except Exception as e:
            return False
        pass

    def wait_for_element_loaded(self, locator, time_out=10):
        """
        等待元素加载成功
        :param locator: 操作的控件,["ID", "root"]
        :param time_out: 最长等待时间，默认10s
        :return: True or False
        """
        i = 0
        while i < int(time_out) and (not self.is_element_present(locator)):
            time.sleep(1)
            i += 1
        if i > time_out - 1:
            self.log_screenshot("等待元素加载失败！！！")
            raise Exception()

    def wait_for_elements_loaded(self, locator, time_out=10):
        """
        等待元素列表加载成功
        :param locator: 操作的控件,["tag_name", "input"]
        :param time_out: 最长等待时间，默认10s
        :return: True or False
        """
        i = 0
        while i < int(time_out) and (not self.is_elements_present(locator)):
            time.sleep(1)
            i += 1
        if i > time_out - 1:
            self.log_screenshot("等待元素列表加载失败！！！")
            raise Exception()

    def wait_for_element_not_exist(self, locator, time_out=10):
        """
        等待元素不存在
        :param locator: 操作的控件,["ID", "root"]
        :param time_out: 最长等待时间，默认10s
        :return: True or False
        """
        i = 0
        while i < int(time_out) and self.is_element_present(locator):
            time.sleep(1)
            i += 1
        if i > time_out - 1:
            self.log_screenshot("等待元素消失失败！！！")
            raise Exception()

    def wait_for_elements_not_exist(self, locator, time_out=10):
        """
        等待元素列表不存在
        :param locator: 操作的控件,["tag_name", "input"]
        :param time_out: 最长等待时间，默认10s
        :return: True or False
        """
        i = 0
        while i < int(time_out) and self.is_elements_present(locator):
            time.sleep(1)
            i += 1
        if i > time_out - 1:
            self.log_screenshot("等待元素消失失败！！！")
            raise Exception()

    @action_decorate
    def get_elements_count(self, locator):
        """
        获取同类元素的个数
        :param locator:操作的控件，["ID", "root"]，["tag_name", "input"]
        :return:
        """
        self.wait_for_elements_loaded(locator)
        try:
            elems = get_elements(self.driver, locator)
            return len(elems)
        except Exception as e:
            self.catch_exception(e)

    @action_decorate
    def move_to_element(self, locator, locator_index=None):
        """
        鼠标移动到元素上
        :param locator:操作的控件，["ID", "root"]，["tag_name", "input"]
        :param locator_index:locator是元素列表才需要输入：第几个元素，数字，从0开始；
        :return:
        """
        if locator_index:
            self.wait_for_elements_loaded(locator)
            try:
                chain = ActionChains(self.driver)
                elem = get_elements(self.driver, locator)[int(locator_index)]
                chain.move_to_element(elem).perform()
            except Exception as e:
                self.catch_exception(e)
        else:
            self.wait_for_element_loaded(locator)
            try:
                chain = ActionChains(self.driver)
                elem = get_element(self.driver, locator)
                chain.move_to_element(elem).perform()
            except Exception as e:
                self.catch_exception(e)
        pass

    @action_decorate
    def click(self, locator, locator_list=None):
        """
        点击操作
        :param locator: 操作的控件，["ID", "root"]，["tag_name", "input"]
        :param locator_list: locator是元素列表才需要输入：list，eq.,[0],[0, 1, 2],默认None。如果控件定位到的是多个控件，要对第几个控件进行操作，
                            可以对多个控件进行操作
        :return:
        """
        if locator_list:
            self.wait_for_elements_loaded(locator)
            try:
                elements = get_elements(self.driver, locator)
                for i in locator_list:
                    elements[int(i)].click()
            except Exception as e:
                self.catch_exception(e)
        else:
            self.wait_for_element_loaded(locator)
            try:
                elem = get_element(self.driver, locator)
                elem.click()
            except Exception as e:
                self.catch_exception(e)
        pass

    @action_decorate
    def send_keys(self, locator, value, locator_list=None):
        """
        在控件中输入值
        :param locator: 操作的控件，["ID", "root"]，["tag_name", "input"]
        :param value: 输入的值
        :param locator_list: locator是元素列表才需要输入：list，eq.,[0],[0, 1, 2],默认None。如果控件定位到的是多个控件，要对第几个控件进行操作，
                            可以对多个控件进行操作
        :return:
        """
        if locator_list:
            self.wait_for_elements_loaded(locator)
            try:
                elements = get_elements(self.driver, locator)
                for i in locator_list:
                    elements[int(i)].send_keys(str(value))
            except Exception as e:
                self.catch_exception(e)
        else:
            self.wait_for_element_loaded(locator)
            try:
                elem = get_element(self.driver, locator)
                elem.send_keys(str(value))
            except Exception as e:
                self.catch_exception(e)
        pass

    @action_decorate
    def double_click(self, locator, locator_index=None):
        """
        鼠标双击控件
        :param locator: 操作的控件，["ID", "root"]，["tag_name", "input"]
        :param locator_index: locator是元素列表才需要输入：第几个元素，数字，从0开始；
        :return:
        """
        if locator_index:
            self.wait_for_elements_loaded(locator)
            try:
                chain = ActionChains(self.driver)
                elem = get_elements(self.driver, locator)[int(locator_index)]
                chain.double_click(elem).perform()
            except Exception as e:
                self.catch_exception(e)
        else:
            self.wait_for_element_loaded(locator)
            try:
                chain = ActionChains(self.driver)
                elem = get_element(self.driver, locator)
                chain.double_click(elem).perform()
            except Exception as e:
                self.catch_exception(e)
        pass

    @action_decorate
    def context_click(self, locator, locator_index=None):
        """
        右键点击控件
        :param locator: 操作的控件，["ID", "root"]，["tag_name", "input"]
        :param locator_index: locator是元素列表才需要输入：第几个元素，数字，从0开始；
        :return:
        """
        if locator_index:
            self.wait_for_elements_loaded(locator)
            try:
                chain = ActionChains(self.driver)
                elem = get_elements(self.driver, locator)[int(locator_index)]
                chain.context_click(elem).perform()
            except Exception as e:
                self.catch_exception(e)
        else:
            self.wait_for_element_loaded(locator)
            try:
                chain = ActionChains(self.driver)
                elem = get_element(self.driver, locator)
                chain.context_click(elem).perform()
            except Exception as e:
                self.catch_exception(e)
        pass

    @action_decorate
    def clear(self, locator, locator_list=None):
        """
        清空text控件中的文本
        :param locator:操作的控件
        :param locator_list: locator是元素列表才需要输入：list，eq.,[0],[0, 1, 2],默认None。如果控件定位到的是多个控件，要对第几个控件进行操作，
                            可以对多个控件进行操作
        :return:
        """
        if locator_list:
            self.wait_for_elements_loaded(locator)
            try:
                elements = get_elements(self.driver, locator)
                for i in locator_list:
                    elements[int(i)].clear()
            except Exception as e:
                self.catch_exception(e)
        else:
            self.wait_for_element_loaded(locator)
            try:
                elem = get_element(self.driver, locator)
                elem.clear()
            except Exception as e:
                self.catch_exception(e)
        pass

    @action_decorate
    def text(self, locator, locator_index=None):
        """
        获取控件的text属性值
        :param locator: 操作的控件
        :param locator_index: locator是元素列表才需要输入：第几个元素，数字，从0开始；
        :return: 控件的文本值
        """
        if locator_index:
            self.wait_for_elements_loaded(locator)
            try:
                elem = get_elements(self.driver, locator)[int(locator_index)]
                return elem.text
            except Exception as e:
                self.catch_exception(e)
        else:
            self.wait_for_element_loaded(locator)
            try:
                elem = get_element(self.driver, locator)
                return elem.text
            except Exception as e:
                self.catch_exception(e)
        pass
        """
        获取控件的text属性值
        :param locator: 操作的控件
        :param key: 属性名，可以是value/id/name/type等元素的属性
        :param locator_index: locator是元素列表才需要输入：第几个元素，数字，从0开始；
        :return: 控件的属性值
        """
        if locator_index:
            self.wait_for_elements_loaded(locator)
            try:
                elem = get_elements(self.driver, locator)[int(locator_index)]
                return elem.get_attribute(key)
            except Exception as e:
                self.catch_exception(e)
        else:
            self.wait_for_element_loaded(locator)
            try:
                elem = get_element(self.driver, locator)
                return elem.get_attribute(key)
            except Exception as e:
                self.catch_exception(e)
        pass

    @action_decorate
    def checkbox_click(self, locator, locator_list=None):
        """
        点击复选框
        :param locator:操作的控件
        :param locator_list: locator是元素列表才需要输入：list，eq.,[0],[0, 1, 2],默认None。如果控件定位到的是多个控件，要对第几个控件进行操作，
                            可以对多个控件进行操作
        :return:
        """
        if locator_list:
            self.wait_for_elements_loaded(locator)
            try:
                elements = get_elements(self.driver, locator)
                for i in locator_list:
                    elements[int(i)].click()
            except Exception as e:
                self.catch_exception(e)
        else:
            self.wait_for_element_loaded(locator)
            try:
                elem = get_element(self.driver, locator)
                elem.click()
            except Exception as e:
                self.catch_exception(e)
        pass

    @action_decorate
    def select_by_text(self, locator, text, locator_index=None):
        """
        根据文本选择下拉菜单的项
        :param locator: 操作的控件
        :param text: 下拉项的文本值
        :param locator_index: locator是元素列表才需要输入：第几个元素，数字，从0开始；
        :return:
        """
        if locator_index:
            self.wait_for_elements_loaded(locator)
            try:
                elem = get_elements(self.driver, locator)[int(locator_index)]
                select = Select(elem)
                select.select_by_visible_text(text)
            except Exception as e:
                self.catch_exception(e)
        else:
            self.wait_for_element_loaded(locator)
            try:
                elem = get_element(self.driver, locator)
                select = Select(elem)
                select.select_by_visible_text(text)
            except Exception as e:
                self.catch_exception(e)
        pass

    @action_decorate
    def select_by_idx(self, locator, idx, locator_index=None):
        """
        根据序号选择下拉菜单的项
        :param locator: 操作的控件
        :param idx: 下拉项的序号，从0开始算
        :param locator_index: locator是元素列表才需要输入：第几个元素，数字，从0开始；
        :return:
        """
        if locator_index:
            self.wait_for_elements_loaded(locator)
            try:
                elem = get_elements(self.driver, locator)[int(locator_index)]
                select = Select(elem)
                select.select_by_index(int(idx))
            except Exception as e:
                self.catch_exception(e)
        else:
            self.wait_for_element_loaded(locator)
            try:
                elem = get_element(self.driver, locator)
                select = Select(elem)
                select.select_by_index(int(idx))
            except Exception as e:
                self.catch_exception(e)
        pass

    @action_decorate
    def select_by_value(self, locator, value, locator_index=None):
        """
        根据value值选择下拉菜单的项
        :param locator: 操作的控件
        :param value: 下拉项的value值
        :param locator_index: locator是元素列表才需要输入：第几个元素，数字，从0开始；
        :return:
        """
        if locator_index:
            self.wait_for_elements_loaded(locator)
            try:
                elem = get_elements(self.driver, locator)[int(locator_index)]
                select = Select(elem)
                select.select_by_value(value)
            except Exception as e:
                self.catch_exception(e)
        else:
            self.wait_for_element_loaded(locator)
            try:
                elem = get_element(self.driver, locator)
                select = Select(elem)
                select.select_by_value(value)
            except Exception as e:
                self.catch_exception(e)
        pass

    @action_decorate
    def get_select_value_by_text(self, locator, text, locator_index=None):
        """
        根据文本获取下拉菜单某项的value值
        :param locator: 操作的控件
        :param text: 下拉项的文本值
        :param locator_index: locator是元素列表才需要输入：第几个元素，数字，从0开始；
        :return:
        """
        if locator_index:
            self.wait_for_elements_loaded(locator)
            try:
                elem = get_elements(self.driver, locator)[int(locator_index)]
                select = Select(elem)
                options = select.options
                if len(options) > 0:
                    for option in options:
                        option_text = option.text
                        if re.search(text, option_text):
                            return option.get_attribute('value')
            except Exception as e:
                self.catch_exception(e)
        else:
            self.wait_for_element_loaded(locator)
            try:
                elem = get_element(self.driver, locator)
                select = Select(elem)
                options = select.options
                if len(options) > 0:
                    for option in options:
                        option_text = option.text
                        if re.search(text, option_text):
                            return option.get_attribute('value')
            except Exception as e:
                self.catch_exception(e)
        pass

    @action_decorate
    def get_select_text_by_value(self, locator, value, locator_index=None):
        """
        根据value值获取下拉菜单某项的文本
        :param locator: 操作的控件
        :param value: 下拉项的value值
        :param locator_index: locator是元素列表才需要输入：第几个元素，数字，从0开始；
        :return:
        """
        if locator_index:
            self.wait_for_elements_loaded(locator)
            try:
                elem = get_elements(self.driver, locator)[int(locator_index)]
                select = Select(elem)
                options = select.options
                if len(options) > 0:
                    for option in options:
                        option_value = option.get_attribute('value')
                        if re.search(value, option_value):
                            return option.text
            except Exception as e:
                self.catch_exception(e)
        else:
            self.wait_for_element_loaded(locator)
            try:
                elem = get_element(self.driver, locator)
                select = Select(elem)
                options = select.options
                if len(options) > 0:
                    for option in options:
                        option_value = option.get_attribute('value')
                        if re.search(value, option_value):
                            return option.text
            except Exception as e:
                self.catch_exception(e)
        pass

    @action_decorate
    def get_select_text_by_idx(self, locator, idx, locator_index=None):
        """
        根据序号获取下拉菜单某项的文本
        :param locator: 操作的控件
        :param idx: 下拉项的序号，从0开始算
        :param locator_index: locator是元素列表才需要输入：第几个元素，数字，从0开始；
        :return:
        """
        if locator_index:
            self.wait_for_elements_loaded(locator)
            try:
                elem = get_elements(self.driver, locator)[int(locator_index)]
                select = Select(elem)
                options = select.options
                if len(options) > 0:
                    return options[int(idx)].text
            except Exception as e:
                self.catch_exception(e)
        else:
            self.wait_for_element_loaded(locator)
            try:
                elem = get_element(self.driver, locator)
                select = Select(elem)
                options = select.options
                if len(options) > 0:
                    return options[int(idx)].text
            except Exception as e:
                self.catch_exception(e)
        pass

    @action_decorate
    def get_select_value_by_idx(self, locator, idx, locator_index=None):
        """
        根据序号获取下拉菜单某项的value值
        :param locator: 操作的控件
        :param idx: 下拉项的序号，从0开始算
        :param locator_index: locator是元素列表才需要输入：第几个元素，数字，从0开始；
        :return:
        """
        if locator_index:
            self.wait_for_elements_loaded(locator)
            try:
                elem = get_elements(self.driver, locator)[int(locator_index)]
                select = Select(elem)
                options = select.options
                if len(options) > 0:
                    return options[int(idx)].get_attribute("value")
            except Exception as e:
                self.catch_exception(e)
        else:
            self.wait_for_element_loaded(locator)
            try:
                elem = get_element(self.driver, locator)
                select = Select(elem)
                options = select.options
                if len(options) > 0:
                    return options[int(idx)].get_attribute("value")
            except Exception as e:
                self.catch_exception(e)
        pass

    @action_decorate
    def click_table_by_search(self, table_locator, search_list, click_locator):
        """
        根据表格的某行的字段值列表，点击该行中的某个按钮
        :param table_locator: 表格控件
        :param click_locator: 要点击的控件
        :param search_list: 用于搜索行的list：["DH20180102", "测试"]
        :return:
        """
        self.wait_for_element_loaded(table_locator)
        self.wait_for_element_loaded(click_locator)
        try:
            table = get_element(self.driver, table_locator)
            trs = table.find_elements_by_css_selector("tr")
            for tr in trs:
                tr_text = tr.text
                flag = 1
                for search_text in search_list:
                    if not re.search(search_text, tr_text):
                        flag = 0
                        break
                if flag == 1:
                    elem = get_element(tr, click_locator)
                    elem.click()
        except Exception as e:
            self.catch_exception(e)

    @action_decorate
    def click_table_by_row_col(self, table_locator, row, col, click_locator=None):
        """
        根据表格的行号和列号，点击该行中的某个按钮
        :param table_locator: 表格控件
        :param click_locator: 要点击的控件
        :param row: 行号，从0开始算，表头不要计算在内
        :param col: 列号，从0开始算
        :return:
        """
        self.wait_for_element_loaded(table_locator)
        self.wait_for_element_loaded(click_locator)
        try:
            table = get_element(self.driver, table_locator)
            tr = table.find_elements_by_css_selector("tr")[row + 1]
            td = tr.find_elements_by_css_selector("td")[col]
            if click_locator:
                elem = get_element(td, click_locator)
                elem.click()
            else:
                td.click()
        except Exception as e:
            self.catch_exception(e)

    @action_decorate
    def get_table_col_text_by_search_name(self, table_locator, search_list, col_name):
        """
        根据表格某行其他字段的值获取该行对应列名的文本值
        :param table_locator: 表格控件
        :param search_list: 用于搜索行的list：["DH20180102", "测试"]
        :param col_name: 要获取文本值的列名
        :return:
        """
        self.wait_for_element_loaded(table_locator)
        try:
            table = get_element(self.driver, table_locator)
            trs = table.find_elements_by_css_selector("tr")
            ths = trs[0].find_elements_by_css_selector("th")
            index = 0
            for k, th in enumerate(ths):
                th_text = th.text
                if re.search(col_name, th_text):
                    index = k
                    break

            for tr in trs:
                tr_text = tr.text
                flag = 1
                for search_text in search_list:
                    if not re.search(search_text, tr_text):
                        flag = 0
                        break
                if flag == 1:
                    td = tr.find_elements_by_css_selector("td")[index]
                    return td.text
        except Exception as e:
            self.catch_exception(e)

    @action_decorate
    def get_table_col_text_by_row_col_not_header(self, table_locator, row, col):
        """
        表格没有表头的情况下，根据表格的行号列号来获取单元格的文本值
        :param table_locator: 表格控件
        :param row: 行号，从0开始算，表头不要计算在内
        :param col: 列号，从0开始算
        :return:
        """
        self.wait_for_element_loaded(table_locator)
        try:
            table = get_element(self.driver, table_locator)
            tr = table.find_elements_by_css_selector("tr")[row]
            td = tr.find_elements_by_css_selector("td")[col]
            return td.text
        except Exception as e:
            self.catch_exception(e)

    @action_decorate
    def get_table_col_text_by_row_col(self, table_locator, row, col):
        """
        表格有表头的情况下，根据表格的行号列号来获取单元格的文本值
        :param table_locator: 表格控件
        :param row: 行号，从0开始算，表头不要计算在内
        :param col: 列号，从0开始算
        :return:
        """
        self.wait_for_element_loaded(table_locator)
        try:
            table = get_element(self.driver, table_locator)
            tr = table.find_elements_by_css_selector("tr")[row + 1]
            td = tr.find_elements_by_css_selector("td")[col]
            return td.text
        except Exception as e:
            self.catch_exception(e)

    @action_decorate
    def get_table_elem_attr_by_search(self, table_locator, search_list, key, elem_locator):
        """
        根据表格某行其他字段的值获取该行某个元素的属性值
        :param table_locator: 表格控件
        :param search_list: 用于搜索行的list：["DH20180102", "测试"]
        :param key: 要获取的属性名
        :param elem_locator: 元素控件
        :return:
        """
        self.wait_for_element_loaded(table_locator)
        try:
            table = get_element(self.driver, table_locator)
            trs = table.find_elements_by_css_selector("tr")

            for tr in trs:
                tr_text = tr.text
                flag = 1
                for search_text in search_list:
                    if not re.search(search_text, tr_text):
                        flag = 0
                        break
                if flag == 1:
                    elem = get_element(tr, elem_locator)
                    return elem.get_attribute(key)
        except Exception as e:
            self.catch_exception(e)

    @action_decorate
    def get_table_elem_attr_by_row_col(self, table_locator, row, col, key, elem_locator):
        """
        根据表格的行号列号来获取单元格某个元素的属性值
        :param table_locator: 表格控件
        :param row: 行号，从0开始算，表头不要计算在内
        :param col: 列号，从0开始算
        :param key: 属性名
        :param elem_locator: 元素控件
        :return:
        """
        self.wait_for_element_loaded(table_locator)
        try:
            table = get_element(self.driver, table_locator)
            tr = table.find_elements_by_css_selector("tr")[row + 1]
            td = tr.find_elements_by_css_selector("td")[col]
            elem = get_element(td, elem_locator)
            return elem.get_attribute(key)
        except Exception as e:
            self.catch_exception(e)

    @action_decorate
    def switch_to_window(self, idx=-1, title=""):
        """
        进行window浏览器窗口跳转
        :param idx:窗口的序号
        :param title:标题
        :return:
        """
        try:
            handles = self.driver.window_handles
            if idx != -1 and title:
                handle = handles[idx]
                self.driver.switch_to_window(handle)
                t = self.driver.title
                if t != title:
                    raise Exception("要跳转的window窗口标题不对")
            elif idx != -1 and not title:
                handle = handles[idx]
                self.driver.switch_to_window(handle)
            elif idx == -1 and title:
                for handle in handles:
                    self.driver.switch_to_window(handle)
                    t = self.driver.title
                    if t == title:
                        break
            else:
                raise Exception("请输入参数")
        except Exception as e:
            self.catch_exception(e)

    @action_decorate
    def switch_to_frame(self, locator=None):
        """
        进行iframe跳转
        :param locator:iframe对应的选择器
        :return:
        """
        try:
            if not locator:
                self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
            else:
                self.driver.switch_to.frame(get_element(self.driver, locator))
        except Exception as e:
            self.catch_exception(e)

    @action_decorate
    def switch_to_default(self):
        """
        iframe跳转操作结束后，返回原来的frame
        :return:
        """
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            self.catch_exception(e)

    @action_decorate
    def alert_submit(self):
        """
        获取弹出框中的消息，并点击alert的确定按钮
        :return:
        """
        try:
            alert = self.driver.switch_to_alert()
            message = alert.text
            alert.accept()
            return message
        except Exception as e:
            self.catch_exception(e)

    @action_decorate
    def alert_close(self):
        """
        获取弹出框中的消息，并点击alert的关闭按钮
        :return:
        """
        try:
            alert = self.driver.switch_to_alert()
            message = alert.text
            alert.dismiss()
            return message
        except Exception as e:
            self.catch_exception(e)

    @action_decorate
    def driver_close(self):
        """
        关闭浏览器和driver
        :return:
        """
        try:
            self.driver.close()
            self.driver.quit()
            self.driver = None
        except Exception as e:
            self.catch_exception(e)

    @action_decorate
    def window_maxsize(self):
        """
        浏览器窗口最大化
        :return:
        """
        try:
            self.driver.maximize_window()
        except Exception as e:
            self.catch_exception(e)


