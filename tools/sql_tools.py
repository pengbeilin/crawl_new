#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Version : python3.6
@Author  : Song Yancong
@Time    : 2018/6/26 2018/6/26 15:33
@Describe: TODO
"""

import pymysql
import argparse


class SqlTools:
    def __init__(self, host, user, password, db, auto_close=True,
                 as_dict=False):
        self._host = host
        self._user = user
        self._password = password
        self._db = db
        self._auto_close = auto_close
        self._as_dict = as_dict

    def _get_connect(self):
        if self._as_dict:
            self.conn = pymysql.connect(self._host, self._user, self._password, self._db, charset='utf8',
                                        cursorclass=pymysql.cursors.DictCursor)
        else:
            self.conn = pymysql.connect(self._host, self._user, self._password, self._db, charset='utf8')

    def insert(self, sql, args=None):
        self._get_connect()
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, args)
            self.conn.commit()
        except Exception as e:
            print(sql)
            print(e)
            self.conn.rollback()
        finally:
            self.conn.auto_close()

    def inserts(self, sql_s):
        self._get_connect()
        cursor = self.conn.cursor()
        s = ''
        try:
            for s in sql_s:
                if type(s) is str:
                    cursor.execute(s)
                else:
                    cursor.execute(s[0], s[1])
            self.conn.commit()
        except Exception as e:
            print(s)
            print(e)
            self.conn.rollback()
        finally:
            self.conn.auto_close()

    def select(self, sql, args=None):
        self._get_connect()
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, args)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print(e)
        finally:
            if self._auto_close:
                self.conn.auto_close()

    def update(self, sql, args=None):
        self._get_connect()
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, args)
            self.conn.commit()
        except Exception as e:
            print(e)
            print(sql)
            self.conn.rollback()
        finally:
            self.conn.auto_close()

    def update_s(self, sql_s):
        self._get_connect()
        cursor = self.conn.cursor()
        sql = ''
        try:
            for index, sql in enumerate(sql_s):
                if type(sql) == str:
                    rs = cursor.execute(sql)
                else:
                    rs = cursor.execute(*sql)
                if result > 0:
                    print(index, rs)
            self.conn.commit()
        except Exception as e:
            print(e)
            print(sql)
            self.conn.rollback()
        finally:
            self.conn.auto_close()

    def is_close(self):
        return self._db

    def auto_close(self):
        if self._auto_close:
            self.close()

    def close(self):
        try:
            self.conn.auto_close()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('-host', type=str, default='10.100.13.65')
    parser.add_argument('-user', type=str, default='root')
    parser.add_argument('-pw', type=str, default='szso2019')
    parser.add_argument('-db', type=str, default='base')
    parser.add_argument('-sql', type=str, default='')
    args = parser.parse_args()
    try:
        st = SqlTools(args.host, args.user, args.pw, args.db)
        result = st.select('select * from reporturl where gaiyao=%s', 'Login')
        print(result)
        print("successful!")
    except Exception as e1:
        print('fail', e1)
