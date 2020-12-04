# coding: utf-8
import configparser
import codecs
import re
from utils.env_util import get_app_loc


# 全局变量
gblCfp = configparser.ConfigParser()


def get_cfg_loc(filename):
    return get_app_loc() + str(filename) + '.ini'


def parse_cfg(filename, sec):
    # 获取文件路径
    file_path = get_cfg_loc(filename)

    content = open(file_path, "r", encoding="gbk").read()
    # Window下用记事本打开配置文件并修改保存后，编码为UNICODE或UTF-8的文件的文件头
    # 会被相应的加上\xff\xfe（\xff\xfe）或\xef\xbb\xbf，然后再传递给configparser解析的时候会出错
    # ，因此解析之前，先替换掉
    content = re.sub(r"\xfe\xff", "", content)
    content = re.sub(r"\xff\xfe", "", content)
    content = re.sub(r"\xef\xbb\xbf", "", content)
    open(file_path, 'w').write(content)

    # 解析配置文件
    gblCfp.read_file(codecs.open(file_path, 'r', "gbk"))

    cfg_data = gblCfp.items(sec)
    ret = dict()
    for it in cfg_data:
        ret[it[0]] = it[1]

    return ret
