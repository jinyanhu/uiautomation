# coding=utf-8

"""
解析测试报告内容，组成推送信息
using method:
    input command in cmd linke "python runner.py case_2 case_1"
"""
import os
import sys
import time
import socket

__author__ = "zzh"
__package__ = "IscsUIAutomation"
# reload(sys)
# sys.setdefaultencoding('utf8')
sys.path.insert(0, '..')


# 获取当前时间
date = time.strftime("%Y%m%d", time.localtime())       # 日期【20150213】
timestamp = str(int(time.time()))   # 时间戳【1423813170】

# 当前路径
path = os.path.abspath(__file__)
path = os.path.dirname(path)


def get_data_old(all_the_text):
    """
    获取结果报告中每一项的数值
    text:报告内容
    keyword：该项内容的关键字
    """
    # runtime
    start = all_the_text.find("<strong>Start Time:</strong>")
    end = all_the_text.find("</p>", start+29)
    runtime = str(all_the_text[start+29:end])
    # timeSpend
    start = all_the_text.find("<strong>Duration:</strong>")
    end = all_the_text.find("</p>", start+27)
    time_spend = str(all_the_text[start+27:end])

    hour_end = time_spend.find(":")
    hour = int(time_spend[0:hour_end])
    min_start = hour_end+1
    min_end = time_spend.find(":", min_start)
    min = int(time_spend[min_start:min_end])
    second_start = min_end+1
    second_end = time_spend.find(".", second_start)
    second = int(time_spend[second_start:second_end])
    mis = time_spend[second_end:]
    time_spend = float(str(3600*hour+60*min+second)+mis)

    # total
    start = all_the_text.find("<td>Total</td>")
    end = all_the_text.find("</td>", start+23)
    total_num = int(all_the_text[start+23:end])
    # pass
    start = end
    end = all_the_text.find("</td>", start+14)
    pass_num = int(all_the_text[start+14:end])
    # failed
    start = end
    end = all_the_text.find("</td>", start+14)
    failed_num = int(all_the_text[start+14:end])
    # error
    start = end
    end = all_the_text.find("</td>", start+14)
    error_num = int(all_the_text[start+14:end])
    # percent + avgTime
    percent = 0.0
    avg_time = 0.0
    if total_num != 0:
        percent = int((float(total_num-failed_num-error_num)/total_num)*10000)/100.0
        avg_time = int(float(time_spend/total_num)*100)/100.0

    return [runtime, time_spend, total_num, pass_num, failed_num, error_num, percent, avg_time]


def get_data(all_the_text):
    """
    获取结果报告中每一项的数值
    text:报告内容
    keyword：该项内容的关键字
    """
    # runtime
    start = all_the_text.find("<strong>该次测试执行于:</strong>")
    end = all_the_text.find("</p>", start+25)
    runtime = str(all_the_text[start+25:end])
    # timeSpend
    start = all_the_text.find("<strong>运行时间:</strong>")
    end = all_the_text.find("</p>", start+22)
    time_spend = str(all_the_text[start+22:end])

    hour_end = time_spend.find(":")
    hour = int(time_spend[0:hour_end])
    min_start = hour_end+1
    min_end = time_spend.find(":", min_start)
    min = int(time_spend[min_start:min_end])
    second_start = min_end+1
    second_end = time_spend.find(".", second_start)
    second = int(time_spend[second_start:second_end])
    mis = time_spend[second_end:]
    time_spend = float(str(3600*hour+60*min+second)+mis)

    # total
    start = all_the_text.find("<td>Total</td>")
    end = all_the_text.find("</td>", start+23)
    total_num = int(all_the_text[start+23:end])
    # pass
    start = end
    end = all_the_text.find("</td>", start+14)
    pass_num = int(all_the_text[start+14:end])
    # failed
    start = end
    end = all_the_text.find("</td>", start+14)
    failed_num = int(all_the_text[start+14:end])
    # error
    start = end
    end = all_the_text.find("</td>", start+14)
    error_num = int(all_the_text[start+14:end])
    # percent + avgTime
    percent = 0.0
    avg_time = 0.0
    if total_num != 0:
        percent = int((float(total_num-failed_num-error_num)/total_num)*10000)/100.0
        avg_time = int(float(time_spend/total_num)*100)/100.0

    return [runtime, time_spend, total_num, pass_num, failed_num, error_num, percent, avg_time]


def get_result(report_dir, report_title, report_file_name):
    """
    获取测试报告结果内容，组成推送信息
    report_dir：报告所在的文件夹路径
    """
    # 打开文件
    file_path = report_dir + '/' + report_file_name
    file_object = open(file_path, "r", encoding='utf-8')
    all_the_text = ""
    try:
        all_the_text = file_object.read()
    finally:
        file_object.close()

    data = get_data(all_the_text)

    # 获取本地ip
    csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    csock.connect(('10.228.81.143', 80))
    (local_ip, port) = csock.getsockname()
    csock.close()
    # local_ip = socket.gethostbyname(socket.gethostname())
    port = "8222"      # 报告地址的端口，若使用默认端口（80）可以为空

    # 获取报告的相对目录，作为url目录
    # index = len(path) + 28
    # relative_directory = (report_dir[index:]).replace("\\", "/")
    relative_directory = report_dir.split("../../")[1]
    relative_directory = relative_directory.split("/")[1]

    if port != "":
        report_url = "http://" + local_ip + ":" + port + "/" + relative_directory + "/" + date + timestamp + '.html'
    else:
        report_url = "http://" + local_ip + relative_directory + "/" + date + timestamp + '.html'
    result = "[" + data[0] + "]" + report_title +"测试结果： " \
             + "\n所有测试： " + str(data[2]) + "个" \
             + ",  通过： " + str(data[3]) + "个" \
             + ",  错误： " + str(data[5]) + "个" \
             + ",  失败： " + str(data[4]) + "个" \
             + ",  通过率： " + str(data[6]) \
             + "%, 运行时间： " + str(data[1]) + "s"
    vag_time = data[7]
    threshold = 100
    if vag_time > threshold:
        result += ".\n平均用例运行时间为" + str(vag_time) +"s，超过" + str(threshold) + "s，请及时关注"
    result += ".\n具体测试结果请查看： " + report_url

    # if str(data[5]) == "0" and str(data[4]) == "0":
    #     result = "[" + data[0] + "]" + report_title + "自动化构建结果： 全部通过（共" + str(data[2]) + "个）"

    return result


if __name__ == "__main__":
    pass
