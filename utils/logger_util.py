import os
import logging
from utils.env_util import get_app_loc
from utils.global_var import GlobalVarClass
__author__ = "zzh"


class LogInfo(object):
    def __init__(self, logfile="error.log", logger_ins="ui_test"):
        try:
            self.logger = None
            # 指定log名，不要与selenium自带的logger冲突
            self.logger = logging.getLogger(logger_ins)
            # 获取日志文件句柄
            self.hdlr = logging.FileHandler(logfile)
            formatter = logging.Formatter("[%(asctime)s]:  %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S")
            self.hdlr.setFormatter(formatter)
            # 添加文件记录设施
            self.logger.addHandler(self.hdlr)
            self.logger.setLevel(logging.DEBUG)
        except Exception as e:
            print(e, "log init error!")

    def info(self, msg):
        self.logger.info(msg)

    def output(self, log_info, error_flag=0):
        try:
            if error_flag:
                self.logger.error("error: " + log_info)
            else:
                self.logger.info(log_info)
        except Exception as output_e:
            print(output_e, "log output error!")

    def close(self):
        try:
            self.hdlr.close()
            self.logger.removeHandler(self.hdlr)
        except Exception as close_e:
            print(close_e, "log close error!")


def run_info_log(error_msg, logfile="run_log"):
    logfile = get_log_file(logfile)
    log = LogInfo(logfile, logfile)
    log.output(error_msg)
    log.close()


def get_log_dir():
    app_loc = get_app_loc()
    log_dir = app_loc + '/log/' + GlobalVarClass.get_now_time() + "/"
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)
    return log_dir


def get_log_file(log_name):
    log_path = get_log_dir() + log_name + '.log'
    return log_path
