import os
__author__ = 'zzh'


# 获取当前uiautomation文件夹所在位置，如 E:\project\uiautomation
def get_app_loc():
    local_dir = os.path.dirname(__file__)

    if not local_dir:
        local_dir = "."

    return local_dir + '/../'
