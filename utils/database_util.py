"""
数据库封装类
"""

import time
import pymysql
import pymssql
from automationTestPlatform.settings import DATABASES

# 数据库连接参数
connect_obj_local = {'host': "10.228.81.217",
                     'user': "sa",
                     'passwd': "Chenfan@123!@#",
                     'database': "UFDATA_015_2016",
                     'charset': 'utf8'}


class Database:
    """
    Database封装类
    """

    error_code = ''  # 错误号码

    _conn = None  # 数据库conn
    _cur = None  # 游标

    _TIMEOUT = 30  # 默认超时60秒
    _time_count = 0

    def __init__(self, database_type="pymssql", connect_obj=''):
        """
        构造器：根据数据库连接对象，创建数据库连接
        :param connect_obj:
        """
        try:
            if not connect_obj:
                connect_obj = connect_obj_local
            if database_type == "pymssql":
                self._database_type = pymssql
                self._conn = pymssql.connect(host=connect_obj['host'],
                                             user=connect_obj['user'],
                                             password=connect_obj['passwd'],
                                             database=connect_obj['database'],
                                             charset=connect_obj['charset'])
            else:
                self._database_type = pymysql
                self._conn = pymysql.connect(host=connect_obj['host'],
                                             port=connect_obj['port'],
                                             user=connect_obj['user'],
                                             passwd=connect_obj['passwd'],
                                             db=connect_obj['database'],
                                             charset=connect_obj['charset'])
        except self._database_type.Error as e:
            self.error_code = e.args[0]
            error_msg = 'Database error! ', e.args[0], e.args[1]
            print(error_msg)

            # 如果没有超过预设超时时间，则再次尝试连接，
            if self._time_count < self._TIMEOUT:
                interval = 2
                self._time_count += interval
                time.sleep(interval)
                self.__init__(database_type)
            else:
                raise Exception(error_msg)

        self._cur = self._conn.cursor()

    def query(self, sql):
        """
        执行 SELECT 语句
        :param sql:
        :return:
        """
        try:
            result = self._cur.execute(sql)
        except self._database_type.Error as e:
            self.error_code = e.args[0]
            print("数据库错误代码:", e.args[0], e.args[1])
            result = False
        return result

    def update(self, sql):
        """
        执行 UPDATE 及 DELETE 语句
        :param sql:
        :return:
        """
        try:
            result = self._cur.execute(sql)
            self._conn.commit()
        except self._database_type.Error as e:
            self.error_code = e.args[0]
            print("数据库错误代码:", e.args[0], e.args[1])
            result = False
        return result

    def insert(self, sql):
        """
        执行 INSERT 语句。如主键为自增长int，则返回新生成的ID
        :param sql:
        :return:
        """
        try:
            self._cur.execute(sql)
            self._conn.commit()
            return self._conn.insert_id()
        except self._database_type.Error as e:
            self.error_code = e.args[0]
            return False

    def fetch_all_rows(self):
        """
        返回结果列表
        :return:
        """
        return self._cur.fetchall()

    def fetch_one_row(self):
        """
        返回一行结果，然后游标指向下一行。到达最后一行以后，返回None
        :return:
        """
        return self._cur.fetchone()

    def get_row_count(self):
        """
        获取结果行数
        :return:
        """
        return self._cur.rowcount

    def commit(self):
        """
        数据库commit操作
        :return:
        """
        self._conn.commit()

    def rollback(self):
        """
        数据库回滚操作
        :return:
        """
        self._conn.rollback()

    def __del__(self):
        """
        释放资源（系统GC自动调用）
        :return:
        """
        try:
            self._cur.close()
            self._conn.close()
        except:
            pass

    def close(self):
        """
        关闭数据库连接
        :return:
        """
        self.__del__()


if __name__ == '__main__':
    """
    示例
    """
    # 连接数据库，创建这个类的实例
    db = Database("pymssql")

    # 操作数据库
    sql = "select * from vendor"
    db.query(sql)

    # 获取结果列表
    result = db.fetch_all_rows()

    # 相当于php里面的var_dump
    print(result)

    # 对行进行循环
    for row in result:
        # 使用下标进行取值
        print(row[0])

        # 对列进行循环
        for colum in row:
            print(colum)

    # 关闭数据库
    db.close()