# coding=utf-8

"""
using method:
    input command in cmd linke "python runner.py case_2 case_1"
"""
import os
import sys
import time
import datetime
from importlib import reload


__author__ = "zzh"

# 当前路径
path = os.path.abspath(__file__)
path = os.path.dirname(path)
print(path)

sys.path.insert(0, path + "/../../")
sys.path.insert(0, '..')
print(sys.path)

from runners.runner import get_suites
from runners.runner import report_parse
from runners.runner import HTMLTestRunner
from utils.global_var import GlobalVarClass
from utils.ding_msg_send import DingMsgSend


# 获取当前时间，组成文件名
date = time.strftime("%Y%m%d", time.localtime())       # 日期【20150213】
timestamp = str(int(time.time()))   # 时间戳【1423813170】
report_file_name = date + timestamp + '.html'
if GlobalVarClass.get_now_time() == "":
    now_time = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H_%M_%S'))
    GlobalVarClass.set_now_time(now_time)


def run_test_cases(test_sets, report_dir, report_title):
    """
    运行测试用例
    test_sets：字典格式的测试集
    """
    # 判断报告文件夹是否存在，若不存在则创建
    is_exist = os.path.exists(report_dir)
    if is_exist is False:
        os.makedirs(report_dir)

    # 指定测试集
    root = os.path.dirname(os.path.abspath(__file__)) + "/../../testcases"
    test_suites = get_suites.generate_suites(root, test_sets)       # 只运行指定测试用例集
    # test_suites = nose.collector()                            # 运行全部用例

    # 定义报告名称
    file_path = report_dir + '/' + report_file_name
    print("报告目录" + file_path)
    fp = open(file_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=report_title      # 如：'共享平台接口测试[ApiTest for SDP]'
    )
    runner.run(test_suites)


def get_report_path(report_file):
    """
    根据配置的文件结构，生成文件路径
    path：当前路径
    """
    tmp = report_file.split('.')
    report_file_path = "test_reports"
    for i in tmp:
        report_file_path += "/"
        report_file_path += i
    report_dir = path + "/../../" + report_file_path

    return report_dir


if __name__ == "__main__":
    case_list = get_suites.set_case_list()      # 获取划分的测试集信息列表

    if case_list is None:
        print("case_list is empty")
        exit()

    for case_info in case_list:
        # print "case_info: ", case_info

        report_file_dir = case_info[u'report_file']
        test_sets = case_info[u'cases']
        receivers = case_info[u'receivers']
        group = case_info[u'group']
        title = case_info[u'title']

        report_dir = get_report_path(report_file_dir)
        run_test_cases(test_sets, report_dir, title)
        res = report_parse.get_result(report_dir, title, report_file_name)

        ding_send_msg = DingMsgSend(group[0])
        ding_send_msg.send_msg(res)

        # for g in group:
        #     receivers.append(g)
        # mail = Mail()
        # mail.subject = "UI自动化测试结果"
        # mail.mail_to = receivers
        # mail.send_mail(res)

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
