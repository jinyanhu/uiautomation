# coding:utf-8
import os
import sys
import time
import datetime
import warnings
from unittest import TestCase
from unittest import SkipTest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.global_var import GlobalVarClass
from utils.env_util import get_app_loc
from utils.logger_util import run_info_log
from utils.parse_ini_util import parse_cfg


__author__ = "zzh"


class _ExpectedFailure(Exception):
    """
    Raise this when a test is expected to fail.

    This is an implementation detail.
    """

    def __init__(self, exc_info):
        super(_ExpectedFailure, self).__init__()
        self.exc_info = exc_info


class _UnexpectedSuccess(Exception):
    """
    The test was supposed to fail, but it didn't!
    """
    pass


class BaseTestCase(TestCase):
    def __init__(self, *args, **kwargs):
        super(BaseTestCase, self).__init__(*args, **kwargs)
        self.driver = None
        self.tear_run = 0
        self.success = False
        # 初始化账号管理器
        # self.account_manage = AccountManage()
        screenshot_path = get_app_loc() + "test_reports/screenshot/"
        if not os.path.isdir(screenshot_path):
            os.makedirs(screenshot_path)
        GlobalVarClass.set_screenshot_path(screenshot_path)
        video_path = get_app_loc() + "test_reports/video/"
        if not os.path.isdir(video_path):
            os.makedirs(video_path)
        GlobalVarClass.set_video_path(video_path)
        if GlobalVarClass.get_now_time() == "":
            now_time = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H_%M_%S'))
            GlobalVarClass.set_now_time(now_time)

    # def __del__(self, *args, **kwargs):
    #     self.account_manage.close_mysql()

    def setUp(self):
        chrome_option = Options()
        chrome_option.add_argument("disable-infobars")
        self.driver = webdriver.Chrome(chrome_options=chrome_option)
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver:
            self.driver.close()
            self.driver.quit()
            self.driver = None
        pass

    def recursion_run_case(self, testMethod, result=None, num=2):
        try:
            self.setUp()
        except SkipTest as e:
            self._addSkip(result, str(e))
        except KeyboardInterrupt:
            raise
        except Exception as e:
            result.addError(self, sys.exc_info())
            if self.driver:
                self.driver.close()
                self.driver.quit()
                self.driver = None
        else:
            try:
                testMethod()
                self.success = True
            except KeyboardInterrupt:
                raise
            except self.failureException:
                result.addFailure(self, sys.exc_info())
            except _ExpectedFailure as e:
                addExpectedFailure = getattr(result, 'addExpectedFailure', None)
                if addExpectedFailure is not None:
                    addExpectedFailure(self, e.exc_info)
                else:
                    warnings.warn("TestResult has no addExpectedFailure method, reporting as passes",
                                  RuntimeWarning)
                    result.addSuccess(self)
            except _UnexpectedSuccess:
                addUnexpectedSuccess = getattr(result, 'addUnexpectedSuccess', None)
                if addUnexpectedSuccess is not None:
                    addUnexpectedSuccess(self)
                else:
                    warnings.warn("TestResult has no addUnexpectedSuccess method, reporting as failures",
                                  RuntimeWarning)
                    result.addFailure(self, sys.exc_info())
            except SkipTest as e:
                self._addSkip(result, str(e))
            except Exception as e:
                if num > 0:
                    num -= 1
                    print("")
                    print("*****************case出错，重新运行一次case*****************")
                    video_p = None
                    # try:
                    #     if num == GlobalVar.get_case_error_num() - 1:
                    #         video_file = GlobalVar.get_case_name() + "_" + str(time.time()) + "_video.wma"
                    #         # video_cmd = 'ffmpeg -rtbufsize 2000M -r 25 -f dshow -i video="Medialooks Screen Capture"  ' + \
                    #         #     GlobalVar.get_video_path() + video_file
                    #         video_cmd = 'ffmpeg -rtbufsize 2000M -f dshow -i video="Medialooks Screen Capture" -r 20 -qscale 8  d:\direj.avi'
                    #         print (video_cmd)
                    #         video_p = subprocess.Popen(video_cmd)
                    #         # os.system(video_cmd)y
                    # except Exception as e:
                    #     print ("暂时无法进行错误录屏，请安装对应组件后再录屏")
                    self.recursion_run_case(testMethod, result, num)
                    # try:
                    #     if video_p:
                    #         video_p.terminate()
                    # except Exception as e:
                    #     pass
                else:
                    result.addError(self, sys.exc_info())
                    self.tearDown()
            else:
                try:
                    self.tearDown()
                    # self.tear_run += 1
                    # if num == 0 and self.tear_run == 1:
                    #     self.tearDown()
                except KeyboardInterrupt:
                    raise
                except:
                    # result.addError(self, sys.exc_info())
                    success = False
        return self.success

    def run(self, result=None):
        """
        每个case运行之前的前置操作
        """
        case_name = str(self._testMethodName)
        GlobalVarClass.set_case_name(case_name)
        case_doc = str(self._testMethodDoc).lstrip("\n").lstrip(" ").rstrip(" ").rstrip("\n")
        log_file = case_name + "_" + GlobalVarClass.get_now_time()
        GlobalVarClass.set_log_file(log_file)
        msg = "run case：" + case_name + "(" + case_doc + ")"
        run_info_log(msg, GlobalVarClass.get_log_file())
        # super(BaseTestCase, self).run(result)

        orig_result = result
        if result is None:
            result = self.defaultTestResult()
            startTestRun = getattr(result, 'startTestRun', None)
            if startTestRun is not None:
                startTestRun()

        self._resultForDoCleanups = result
        result.startTest(self)

        testMethod = getattr(self, self._testMethodName)
        if (getattr(self.__class__, "__unittest_skip__", False) or
            getattr(testMethod, "__unittest_skip__", False)):
            # If the class or method was skipped.
            try:
                skip_why = (getattr(self.__class__, '__unittest_skip_why__', '')
                            or getattr(testMethod, '__unittest_skip_why__', ''))
                self._addSkip(result, skip_why)
            finally:
                result.stopTest(self)
            return
        try:
            success = False
            success = self.recursion_run_case(testMethod, result, GlobalVarClass.get_case_error_num())
            cleanUpSuccess = self.doCleanups()
            success = success and cleanUpSuccess
            if success:
                result.addSuccess(self)
        finally:
            result.stopTest(self)
            if orig_result is None:
                stopTestRun = getattr(result, 'stopTestRun', None)
                if stopTestRun is not None:
                    stopTestRun()
        pass