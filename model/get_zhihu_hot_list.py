#!/usr/bin/env python3
# encoding: utf-8
import os
import time

from tools.driver_utils import DriverUtils
from tools.logutil import i
from tools.utils import Utils

"""
@version: 3.6
@author: pengbeilin
@file: get_zhihu_hot_list.py
@time: 2019/11/7 10:40
"""


def get_hot_list():
    driver_utils = DriverUtils("chrome")
    try:
        i("打开‘知乎热榜’")
        driver_utils.minimize_window()
        driver_utils.open_url("https://www.zhihu.com/billboard")
        elems = driver_utils.wait_get_elems('class', 'HotList-item')
        times = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
        base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        write_path = "%s\\data_zhihu\\%s.txt" % (base_path, times)
        with open(write_path, "a+", encoding="utf-8") as f:
            for e in elems:
                title = e.find_element_by_class_name('HotList-itemTitle')
                des = e.find_element_by_class_name('HotList-itemExcerpt')
                print(title.text)
                print(des.text)
                f.write(title.text)
                f.write("\n")
                e.click()
                print(driver_utils.current_url())
                driver_utils.back()
                Utils.sleep(1)

    except Exception as e:
        i(e)
    finally:
        driver_utils.quit()
        i("退出")


def get_hot_list_des():
    driver_utils = DriverUtils("chrome")
    try:
        i("打开‘知乎热榜’")
        driver_utils.minimize_window()
        times = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
        base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        write_path = "%s\\data_zhihu\\%s.txt" % (base_path, times)
        with open(write_path, "a+", encoding="utf-8") as f:
            for x in range(0, 20):
                driver_utils.open_url("https://www.zhihu.com/billboard")
                elem = driver_utils.wait_get_elems('class', 'HotList-item')[x]
                title = elem.find_element_by_class_name('HotList-itemTitle').text
                des = elem.find_element_by_class_name('HotList-itemExcerpt').text
                elem.click()
                current_url = driver_utils.current_url()
                f.write("[%s](%s)\n%s\n" % (title, current_url, des))
                print(title, "\n", current_url)
                driver_utils.back()
                Utils.sleep(1)

    except Exception as e:
        i(e)
    finally:
        driver_utils.quit()
        i("退出")


if __name__ == '__main__':
    get_hot_list()
