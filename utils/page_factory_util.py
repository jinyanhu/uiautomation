import os
import sys
from utils.logger_util import run_info_log
from utils.global_var import GlobalVarClass


def page_locator_factory(page_name, *text):
    """

    :return:
    :rtype:
    :param page_name:
    :type page_name:
    :param text:
    :type text:
    :return:
    :rtype:
    """
    try:
        element_list = []
        for element in text:
            ele = get_locator_value_by_text(element, find_xml(page_name))
            element_dic = {element: ele}
            element_list.append(element_dic)
        return element_list
    except Exception as e:
        print(e)
        return []


def page_element_factory(page_name, text):
    """
    返回当前页面内需要被实例化的element的text值.
    :param page_name:
    :type page_name:
    :param text:
    :type text:
    :return: element meta data in xml file.
    :rtype:dict
    """
    try:
        element_locator = page_locator_factory(page_name, *text)
        element_meta_data_original = {}
        element_meta_data_middle = {}
        for i in range(len(element_locator)):
            element_meta_data_original.update({text[i]: element_locator[i]})
        for element in text:
            element_meta_data_middle.update(element_meta_data_original[element])
        return element_meta_data_middle
    except Exception as e:
        print(e)
        run_info_log(e, GlobalVarClass.get_log_file())


# 寻找当前目录下的XML文件
def find_xml(page_name):
    """

    :param page_name:
    :type page_name:
    :return:
    :rtype:
    """
    root = os.path.dirname(os.path.realpath(page_name))  # 当前目录
    try:
        page_name = os.path.basename(page_name)[:os.path.basename(page_name).rfind(".")]
        s = os.listdir(root)
        flag = 0
        for i in s:
            if _end_with(i, page_name + '.xml'):
                return root + '/' + page_name + '.xml'
        if flag == 0:
            run_info_log('XML 文件未找到！', GlobalVarClass.get_log_file())
    except Exception as e:
        print(e)


# 判断是否存在XML文件
def _end_with(s, *end_string):
    """

    :param s:
    :type s:
    :param end_string:
    :type end_string:
    :return:
    :rtype:
    """
    try:
        array = map(s.endswith, end_string)
        if True in array:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def __open_xml(path):
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        return root
    except Exception as e:
        print("Error: Cannot parse file:%s" % path)
        sys.exit(1)


def open_xml_tree(path):
        try:
            import xml.etree.cElementTree as ET
        except ImportError:
            import xml.etree.ElementTree as ET
        try:
            tree = ET.parse(path)
            return tree
        except Exception as e:
            print("Error: Cannot parse file:%s" % path)


def parse_xml_getroot_dic(path):
    temp_string = ""
    temp_path = str(path)
    root = __open_xml(temp_path)
    for child in root:
        temp_dict = str(child.attrib)
        temp_string += temp_dict
    return eval(temp_string)


def parse_xml_get_son_list(path):
    temp_path = (str)(path)
    root = __open_xml(temp_path)
    tree = open_xml_tree(temp_path)
    list_all = tree.findall(path='./page/')
    list_tup = []
    for locator in range(len(list_all)):
        tup_temp = (list_all[locator].text, list_all[locator].get('type'), list_all[locator].get('value'))
        list_tup.append(tup_temp)
    print(list_tup)
    return list_tup


def del_first_and_last_char(st):
    str_list = list(st)
    str_list.pop(0)
    print("".join(str_list))
    str_list.pop()
    print("".join(str_list))
    return "".join(str_list)


def get_locator_value_by_text(text, path):
    tree = open_xml_tree(path)
    for element in tree.getiterator('locator'):
        if element.text == str(text):
            return element.get('type'), element.get('value'), element.get('index')