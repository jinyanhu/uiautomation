

def get_element(driver, element_meta_list):
    """
    获取单个元素
    :param driver: webdriver
    :param element_meta_list: ["ID", "root"]
    """
    by = element_meta_list[0]
    by = by.upper()
    value = element_meta_list[1]
    if by == 'IOS_UIAUTOMATION':
        return driver.find_element_by_ios_uiautomation(value)
    if by == 'ANDROID_UIAUTOMATOR':
        return driver.find_element_by_android_uiautomator(value)
    if by == 'ACCESSIBILITY_ID':
        return driver.find_element_by_accessibility_id(value)
    if by == 'ID':
        return driver.find_element_by_id(value)
    if by == 'XPATH':
        return driver.find_element_by_xpath(value)
    if by == 'LINK_TEXT':
        return driver.find_element_by_link_text(value)
    if by == 'PARTIAL_LINK_TEXT':
        return driver.find_element_by_partial_link_text(value)
    if by == 'NAME':
        return driver.find_element_by_name(value)
    if by == 'TAG_NAME':
        return driver.find_element_by_tag_name(value)
    if by == 'CLASS_NAME':
        return driver.find_element_by_class_name(value)
    if by == 'CSS_SELECTOR':
        return driver.find_element_by_css_selector(value)
    if by == "JS":
        """
        value是js脚本，必须能且只能返回一个元素
        """
        return driver.execute_script(value)
    else:
        raise Exception("元素获取类型不存在")


def get_elements(driver, element_meta_list):
    """
    获取元素列表
    :param driver: webdriver
    :param element_meta_list: ["ID", "root"]
    """
    by = element_meta_list[0]
    by = by.upper()
    value = element_meta_list[1]
    if by == 'IOS_UIAUTOMATION':
        return driver.find_elements_by_ios_uiautomation(value)
    if by == 'ANDROID_UIAUTOMATOR':
        return driver.find_elements_by_android_uiautomator(value)
    if by == 'ACCESSIBILITY_ID':
        return driver.find_elements_by_accessibility_id(value)
    if by == 'ID':
        return driver.find_elements_by_id(value)
    if by == 'XPATH':
        return driver.find_elements_by_xpath(value)
    if by == 'LINK_TEXT':
        return driver.find_elements_by_link_text(value)
    if by == 'PARTIAL_LINK_TEXT':
        return driver.find_elements_by_partial_link_text(value)
    if by == 'NAME':
        return driver.find_elements_by_name(value)
    if by == 'TAG_NAME':
        return driver.find_elements_by_tag_name(value)
    if by == 'CLASS_NAME':
        return driver.find_elements_by_class_name(value)
    if by == 'CSS_SELECTOR':
        return driver.find_elements_by_css_selector(value)
    if by == "JS":
        """
        value是js脚本，必须返回元素列表
        """
        return driver.execute_script(value)
    else:
        raise Exception("元素获取类型不存在")







