import traceback
from utils.logger_util import run_info_log
from utils.global_var import GlobalVarClass


def action_decorate(func):
    """
    action装饰器
    :param func:
    :return:
    应用example：
        @action_decorate
        def is_element_present(self, locator):
            pass
    """
    def _action_decorate(*args, **kwargs):
        track_str = traceback.extract_stack()
        page_name_all = track_str[-2][0]
        page_name = page_name_all.split("pages\\")[1]
        page_name = page_name.replace("\\\\", "\\")
        msg = "当前执行的Page：" + page_name
        print(msg)
        run_info_log(msg, GlobalVarClass.get_log_file())
        msg = "    Page中执行的函数：" + str(track_str[-2][2])
        print(msg)
        run_info_log(msg, GlobalVarClass.get_log_file())
        msg = "    Page中执行的函数所在行：" + str(track_str[-2][1])
        print(msg)
        run_info_log(msg, GlobalVarClass.get_log_file())
        args_str = ""
        for k, v in enumerate(args):
            if k != 0:
                args_str += str(v) + "  "
        args_str.replace("\\", "")
        msg = "    Action中执行的函数名：" + func.__name__ + "；参数：" + args_str
        print(msg)
        run_info_log(msg, GlobalVarClass.get_log_file())
        try:
            result = func(*args, **kwargs)
            msg = "        操作运行结果：" + str(result)
            print(msg)
            print("")
            run_info_log(msg, GlobalVarClass.get_log_file())
            return result
        except Exception as e:
            msg = "        操作运行结果：失败！"
            print(msg)
            print("")
            run_info_log(msg, GlobalVarClass.get_log_file())
            raise
    return _action_decorate