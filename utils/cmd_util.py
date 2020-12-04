import os
from time import sleep


def exec_cmd(cmd):
    """

    :param cmd:
    :type cmd:
    :return:
    :rtype:
    """
    try:
        r = os.popen(cmd)
        sleep(1)
        result = r.readlines()
        r.close()
        return result
    except Exception as e:
        print(e)