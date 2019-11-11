#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Version : python3.6
@Author  : Pengbl
@Time    : 2019/1/25 17:17
@Describe: log
"""
import datetime


def i(msg):
    """
    log打印
    :param msg: log
    """
    print("%s : %s" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), msg))
