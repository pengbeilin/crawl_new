#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Version : python3.6
@Author  : Song Yancong
@Time    : 2019/1/24 2019/1/24 21:54
@Describe: SqlServer 连接工具类
"""

import pymssql


class SqlServerTools:
    def __init__(self, host, user, pwd, db, auto_close=True, as_dict=False):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self._auto_close = auto_close
        self.as_dict = as_dict
        self._cur = None

    def _get_connect(self):
        if self._cur:
            return self._cur
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="utf8",
                                    as_dict=self.as_dict)
        self._cur = self.conn.cursor()
        if not self._cur:
            raise (NameError, "连接数据库失败")
        else:
            return self._cur

    def query(self, sql):
        cur = self._get_connect()
        result = ''
        try:
            cur.execute(sql)
            result = cur.fetchall()
        except Exception as e:
            print(e, sql)
        finally:
            self.auto_close()
        return result

    def insert(self, sql):
        cur = self._get_connect()
        try:
            cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e, sql)
        finally:
            self.auto_close()

    def auto_close(self):
        if self._auto_close:
            self.close()

    def close(self):
        try:
            self.conn.auto_close()
        except Exception as e:
            print(e)
