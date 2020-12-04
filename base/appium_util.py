# coding:utf-8
import os
import re
import socket
import subprocess
from time import sleep
from utils.cmd_util import exec_cmd

__package__ = "IscsUIAutomation"


def start_android_appium(device_name):
    """
    :param device_name:
    :type device_name:
    """
    try:
        if not _is_open('127.0.0.1', 4723):
            cmd = "start /b appium -a 127.0.0.1 -p 4723  -U " + device_name + \
                  " --command-timeout 600  --session-override"
            subprocess.call(cmd, shell=True, stdout=open("d:\\log.log", "w"), stderr=subprocess.STDOUT)
            sleep(2)
            print('开启appium服务成功')

        else:
            print('appium服务已开启，不需要开启')
            pass
    except Exception as e:
        print(e)


def start_ios_appium(udid):
    try:
        if not _is_open('127.0.0.1', 4723):
            cmd = "appium -a 127.0.0.1 -p 4723 -U " + udid + " --command-timeout 600 --session-override&"
            subprocess.call(cmd, shell=True, stdout=open("Appium.log", "w"), stderr=subprocess.STDOUT)
            sleep(2)
            print('开启appium服务成功\n')
        else:
            print('appium服务已开启，不需要开启\n')
    except Exception as e:
        print(e)


def restart_adb():
    """
    重启adb
    :return:
    """
    try:
        cmd = 'adb kill-server'
        os.popen(cmd)
        print('adb服务关闭')
        sleep(2)
        cmd = 'adb start-server'
        os.popen(cmd)
        print('adb服务启动')
        sleep(4)
        cmd = "adb devices"
        os.popen(cmd)
        sleep(2)
    except Exception as e:
        print(e)


def _is_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        s.shutdown(2)
        return True
    except Exception as e:
        return False


def stop_android_appium():
    """
    """
    try:
        cmd = 'taskkill /F /IM node.exe /T'
        os.popen(cmd)
        print('appium服务关闭')
    except Exception as e:
        print(e)


def stop_ios_appium(pwd='123'):     # 默认密码为1，根据自己的情况改动
    pids = _get_pid_list()
    if pids is None:
        print('appium已关闭')
        return
    else:
        for pid in pids:
            try:
                print(pid)
                exec_cmd('kill %s' % pid)
                print('appium服务关闭')
            except:
                print('appium已关闭')


def _get_pid_list():
    """
    摘出pid
    yuetianzhuangdeMac-mini:~ yuetianzhuang$ lsof -i:4723
    COMMAND  PID          USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
    node    1267 yuetianzhuang   11u  IPv4 0x96eced274f15cf0d      0t0  TCP localhost:4723 (LISTEN)
    :return:
    """
    try:
        cmd = 'lsof -i:4723'
        result = exec_cmd(cmd)[1:]
        pid_list = []
        for i in range(len(result)):
            seen = set()
            seen_add = seen.add
            k = [x for x in result[i].split(' ') if not (x in seen or seen_add(x))]    # get multi-pid by yongli
            pid_list.append(k[2])
        return pid_list
    except Exception as e:
        print(e)
        return []


def get_android_udid():
    """

    :return:
    :rtype:
    """
    try:
        cmd = 'adb devices'
        result = exec_cmd(cmd)
        a = result[1].split('\t')
        return a[0]
    except Exception as e:
        print(e)

        return False


def get_ios_udid():
    """

    :rtype:
    :return:
    :rtype:
    """
    try:
        result = exec_cmd('idevice_id -l')
        udid = result[len(result) - 1]
        udid = udid[:udid.find('\n')]
        return udid
    except Exception as e:
        print(e)
        return False


def get_ios_udid_cy():
    try:
        result = exec_cmd('idevice_id -l')
        print(result)
        a = '323a7aa5ec9caafa323b1cd85bb818dfb68b836e\n', '3390dbb0be9120f691eb3a7b3b35ecc88ffb02e9\n', \
            '58a11c857c303cc76afa4c7ada384de8886ab769\n', '7346c53b0b9e8fdb2f0287719646b94656c318bc\n'
        for i in range(len(a)):
            if a[i] in result:
                result.remove(a[i])
            pass
        print(result)
        print(result[0].replace('\n', ''))  # cy 私用 误传 注释即可，因为这台mini总是莫名其妙出现俩UdId，特殊处理了下
        udid = result[0].replace('\n', '')
        return udid
    except Exception as e:
        print(e)
        return False


def get_user_id(mobile=None):
    """
    手机号对应的USER_ID
    cy
    smoking 6
    :param mobile:
    :return:

    """
    try:
        # con, curs = sit()
        con, curs = cit()
        sql = '''select t.user_id from xdw_app.ba_user t where mobile =
basic_owner.des_encrypt('%s','b0NmiFbH')''' % mobile
        curs.execute(sql)
        number = curs.fetchone()
        close_oracle(con, curs)
        print(number[0])
        return number[0]
    except Exception as e:
        print(e)
if __name__ == '__main__':
    _get_pid_list()
    stop_ios_appium()

