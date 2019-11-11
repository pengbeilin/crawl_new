#!/usr/bin/env python3
# encoding: utf-8
import os
import time

import requests
import urllib3
import logging
from lxml import etree
from tools.driver_utils import DriverUtils
from tools.logutil import i

"""
@version: 3.6
@author: pengbeilin
@file: get_tencent_news.py
@time: 2019/10/28 10:28
"""


def analysis_context(text, condition):
    return etree.HTML(text).xpath(condition)


def get_details(url):
    urllib3.disable_warnings()
    logging.captureWarnings(True)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/77.0.3865.90 Safari/537.36'
    }
    r = requests.get(url, headers, verify=False)

    # print(r.text)
    onep = analysis_context(r.text, '//p[@class="one-p"]/text()')
    desc = analysis_context(r.text, '//div[@class="desc"]/text()')
    for j in desc:
        print(j)
    for i in onep:
        print(i)
    print("*" * 30)


def get_news():
    driver_utils = DriverUtils("chrome")
    try:
        i("打开‘腾讯新闻主页’")
        driver_utils.minimize_window()
        driver_utils.open_url("https://news.qq.com/")
        elems = driver_utils.wait_get_elems('class', 'detail')
        times = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
        base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        write_path = "%s\\data\\%s.txt" % (base_path, times)
        with open(write_path, "a+", encoding="utf-8") as f:
            for e in elems:
                a = e.find_element_by_tag_name('a')
                doc = "[%s](%s)" % (e.text.split("\n")[0], a.get_attribute("href"))
                f.write(doc)
                f.write("\n")
                print(doc)
                # get_details(a.get_attribute("href"))
    except Exception as e:
        i(e)
    finally:
        i("退出")
        driver_utils.quit()


if __name__ == '__main__':
    get_news()
