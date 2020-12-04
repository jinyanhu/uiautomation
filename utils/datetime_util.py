import time
import datetime
import calendar


class DatetimeUtil(object):
    def __init__(self):
        pass

    def str_now_date_time(self):
        """
        返回当前时间的日期时间字符串：2018-02-06 20:19:41
        :return:
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def str_now_date(self):
        """
        返回当前时间的日期字符串：2018-02-06
        :return:
        """
        return time.strftime("%Y-%m-%d", time.localtime())

    def str_yesterday_by_time(self, str_time):
        """
        返回给定时间的前一天的日期字符串:2018-02-06
        :param str_time:
        :return:
        """
        format_time = datetime.datetime.strptime(str_time, "%Y-%m-%d")
        format_yesterday = format_time + datetime.timedelta(days=-1)
        str_yesterday = format_yesterday.strftime("%Y-%m-%d")
        return str_yesterday

    def str_tomorrow_by_time(self, str_time):
        """
        返回给定时间的后一天的日期字符串:2018-02-06
        :param str_time:
        :return:
        """
        format_time = datetime.datetime.strptime(str_time, "%Y-%m-%d")
        format_tomorrow = format_time + datetime.timedelta(days=1)
        str_tomorrow = format_tomorrow.strftime("%Y-%m-%d")
        return str_tomorrow

    def time_circle_list(self, start_time, end_time, step):
        """
        根据输入开始时间和结束时间及周期，返回时间周期列表
        :param start_time: 2018-02-05
        :param end_time: 2018-03-15
        :param step:day/week/month
        :return:['2018-02-04','2018-02-05',,,'2018-03-15']
        """
        time_circle_list = []
        start = datetime.datetime.strptime(start_time, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_time, "%Y-%m-%d")
        if step == "day":
            pre_start = start + datetime.timedelta(days=-1)
            pre_str = pre_start.strftime("%Y-%m-%d")
            time_circle_list.append(pre_str)
            start_str = start_time
            time_circle_list.append(start_str)
            while start != end:
                start = start + datetime.timedelta(days=1)
                start_str = start.strftime("%Y-%m-%d")
                time_circle_list.append(start_str)
        elif step == "week":
            start_friday = self.get_weekday(start, "Friday")
            end_friday = self.get_weekday(end, "Friday")
            pre_friday = start_friday + datetime.timedelta(days=-7)
            pre_str = pre_friday.strftime("%Y-%m-%d")
            start_str = start_friday.strftime("%Y-%m-%d")
            time_circle_list.append(pre_str)
            time_circle_list.append(start_str)
            while start_friday != end_friday:
                start_friday = start_friday + datetime.timedelta(days=7)
                start_str = start_friday.strftime("%Y-%m-%d")
                time_circle_list.append(start_str)
        elif step == "month":
            start_month_last_day = self.get_now_month_last_day(start)
            end_month_last_day = self.get_now_month_last_day(end)
            pre_month_last_day = self.get_now_month_first_day(start) + datetime.timedelta(days=-1)
            pre_str = pre_month_last_day.strftime("%Y-%m-%d")
            start_str = start_month_last_day.strftime("%Y-%m-%d")
            time_circle_list.append(pre_str)
            time_circle_list.append(start_str)
            while start_month_last_day != end_month_last_day:
                start_month_last_day = self.get_now_month_last_day(start_month_last_day + datetime.timedelta(days=1))
                start_str = start_month_last_day.strftime("%Y-%m-%d")
                time_circle_list.append(start_str)

        return time_circle_list

    def month_circle_list(self, the_time):
        """
        根据输入时间，返回月周期列表
        :param the_time: 字符串 2018-02-27
        :return:
        """
        time_circle_list = []
        the_time = datetime.datetime.strptime(the_time, "%Y-%m-%d")

        start = self.get_now_month_first_day(the_time)
        end = self.get_now_month_last_day(the_time)

        start_str = start.strftime("%Y-%m-%d")
        time_circle_list.append(start_str)
        while start != end:
            start = start + datetime.timedelta(days=1)
            start_str = start.strftime("%Y-%m-%d")
            time_circle_list.append(start_str)

        return time_circle_list

    def get_weekday(self, the_time, week):
        """
        根据给定的时间和星期几，获取给定时间最近的星期几的时间
        :param the_time:
        :param week:
        :return:
        """
        weekday_dict = {
            "Monday": 0,
            "Tuesday": 1,
            "Wednesday": 2,
            "Thursday": 3,
            "Friday": 4,
            "Saturday": 5,
            "Sunday": 6
        }
        the_weekday = the_time.strftime("%A")
        the_num = weekday_dict[the_weekday]
        week_num = weekday_dict[week]
        week_time = the_time + datetime.timedelta(days=(week_num - the_num))
        return week_time

    def get_now_month_first_day(self, the_time):
        """
        获取当前月的第一天
        :param the_time:
        :return:
        """
        year = int(the_time.strftime("%Y"))
        month = int(the_time.strftime("%m"))

        return datetime.datetime(year, month, 1)

    def get_now_month_last_day(self, the_time):
        """
        获取当前月的最后一天
        :param the_time:
        :return:
        """
        year = int(the_time.strftime("%Y"))
        month = int(the_time.strftime("%m"))

        days = calendar.monthrange(year, month)[1] - 1
        return datetime.datetime(year, month, 1) + datetime.timedelta(days=days)

    def get_delta_by_two_time(self, date1, date2):
        """
        获取2个时间的时间差，单位为分钟
        :param date1: 时间字符串
        :param date2: 时间字符串
        :return:
        """
        if not date1 or not date2:
            return 0
        date1 = time.strptime(date1, "%Y-%m-%d %H:%M:%S")
        date2 = time.strptime(date2, "%Y-%m-%d %H:%M:%S")
        date1 = datetime.datetime(date1[0], date1[1], date1[2], date1[3], date1[4], date1[5])
        date2 = datetime.datetime(date2[0], date2[1], date2[2], date2[3], date2[4], date2[5])
        return int((date2 - date1).seconds / 60) + (date2 - date1).days * 1440


if __name__ == '__main__':
    datetime_util = DatetimeUtil()
    date_list = datetime_util.month_circle_list("2017-12-03")
    print(date_list)
    pass