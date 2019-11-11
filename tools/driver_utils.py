#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Version : python3.6
@Author  : Pengbl
@Time    : 2019/1/25 17:34
@Describe: 驱动工具类
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants.constants import CHROME_DRIVER_PATH


class DriverUtils:
    def __init__(self, browser='chrome'):
        """
        初始化,实例化浏览器驱动对象
        :param browser:
        """
        try:
            if browser == 'ff' or browser == 'firefox':  # 火狐
                self.driver = webdriver.Firefox()
            elif browser == 'chrome':  # 谷歌
                option = webdriver.ChromeOptions()
                option.add_argument("--start-maximized")
                self.driver = webdriver.Chrome(chrome_options=option, executable_path=CHROME_DRIVER_PATH)
            elif browser == 'ie' or browser == 'internet explorer':  # IE
                self.driver = webdriver.Ie()
            elif browser == "opera":
                self.driver = webdriver.Opera()
            elif browser == "phantomjs":
                self.driver = webdriver.PhantomJS()
            elif browser == 'edge':
                self.driver = webdriver.Edge()
            else:
                raise NameError("Not found %s browser" % browser)
        except Exception:
            raise NameError("Not found %s browser" % browser)

    def element_wait(self, by, value, timeout=5):
        """
        等待元素出现
        :param by: 查找元素的方法
        :param value: 属性值
        :param timeout: 等待时长(s)
        :return:
        """
        if by == "id":
            WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(By.ID, value))
        elif by == 'name':
            WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(By.NAME, value))
        elif by == "class":
            WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")

    def get_element(self, by, value):
        """
        根据id，name，class，link_text，xpath，css 获取单个元素
        :param by: 查找元素的方法
        :param value: 属性值
        :return: element
        """
        if by == 'id':
            element = self.driver.find_element_by_id(value)
        elif by == 'name':
            element = self.driver.find_element_by_name(value)
        elif by == 'class':
            element = self.driver.find_element_by_class_name(value)
        elif by == 'link_text':
            element = self.driver.find_element_by_link_text(value)
        elif by == 'xpath':
            element = self.driver.find_element_by_xpath(value)
        elif by == 'css':
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def get_elements(self, by, value):
        """
        根据id，name，class，link_text，xpath，css 获取多个元素
        :param by: 查找元素的方法
        :param value: 属性值
        :return: elements
        """
        if by == 'id':
            elements = self.driver.find_elements_by_id(value)
        elif by == 'name':
            elements = self.driver.find_elements_by_name(value)
        elif by == 'class':
            elements = self.driver.find_elements_by_class_name(value)
        elif by == 'link_text':
            elements = self.driver.find_elements_by_link_text(value)
        elif by == 'xpath':
            elements = self.driver.find_elements_by_xpath(value)
        elif by == 'css':
            elements = self.driver.find_elements_by_css_selector(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return elements

    def wait_get_elem(self, by, value, timeout=5):
        """
        :param by: 查找元素的方法
        :param value: 属性值
        :param timeout: 属性值
        :return: 元素
        """
        self.element_wait(by, value, timeout)
        return self.get_element(by, value)

    def wait_get_elems(self, by, value, timeout=5):
        """
        :param by: 查找元素的方法
        :param value: 属性值
        :param timeout: 属性值
        :return: 元素集合
        """
        self.element_wait(by, value, timeout)
        return self.get_elements(by, value)

    def open_url(self, url):
        """
        打开一个url
        :param url: url
        """
        self.driver.get(url)

    def close_page(self):
        """
        关闭当前窗口
        """
        self.driver.close()

    def max_windows(self):
        """
        窗口最大化
        """
        self.driver.maximize_window()

    def set_windows_size(self, width, height):
        """
        设置窗口大小
        :param width: 宽
        :param height: 高
        """
        self.driver.set_window_size(width=width, height=height)

    def input_text(self, by, value, massage):
        """
        输入文本
        :param by: 查找元素的方法
        :param value: 属性值
        :param massage: 输入的值
        """
        self.element_wait(by, value)
        self.get_element(by, value).send_keys(massage)

    def clear_text(self, by, value):
        """
        输入文本
        :param by: 查找元素的方法
        :param value: 属性值
        """
        self.element_wait(by, value)
        self.get_element(by, value).clear()

    def click(self, by, value):
        """
        鼠标左键单击
        :param by: 查找元素的方法
        :param value: 属性值
        """
        self.element_wait(by, value)
        self.get_element(by, value).click()

    def right_click(self, by, value):
        """
        鼠标右键单击
        :param by: 查找元素的方法
        :param value: 属性值
        :return:
        """
        self.element_wait(by, value)
        ActionChains(self.driver).context_click(self.get_element(by, value)).perform()

    def double_click(self, by, value):
        """
        鼠标左键双击
        :param by: 查找元素的方法
        :param value: 属性值
        """
        self.element_wait(by, value)
        ActionChains(self.driver).double_click(self.get_element(by, value)).perform()

    def move_to_target_element(self, by, value):
        """
        移动鼠标到指定元素(默认在元素的中间位置)
        :param by: 查找元素的方法
        :param value: 属性值
        :return:
        """
        self.element_wait(by, value)
        ActionChains(self.driver).move_to_element(self.get_element(by, value)).perform()

    def move_to_target_element_with_offset(self, by, value, xoffset, yoffset):
        """
        移动鼠标到指定元素,并且指定位于元素的x,y偏移量(偏移量相对于元素的左上角)
        :param by: 查找元素的方法
        :param value: 属性值
        :param xoffset: x偏移量
        :param yoffset: y偏移量
        :return:
        """
        self.element_wait(by, value)
        ActionChains(self.driver).move_to_element_with_offset(self.get_element(by, value), xoffset, yoffset).perform()

    def quit(self):
        """
        关闭浏览器驱动
        """
        self.driver.quit()

    def f5(self):
        """
        刷新当前页面,相当于点击F5
        :return:
        """
        self.driver.refresh()

    def back(self):
        """
        返回上一个页面
        """
        self.driver.back()

    def forward(self):
        """
        跳转到下一个页面
        """
        self.driver.forward()

    def js(self, java_script):
        """
        执行指定的js代码
        :param java_script: js代码
        """
        self.driver.execute_script(java_script)

    def add_cookie(self, cookie):
        """
        :param cookie:
        Usage:
            driver.add_cookie({'name' : 'foo', 'value' : 'bar'})
            driver.add_cookie({'name' : 'foo', 'value' : 'bar', 'path' : '/'})
            driver.add_cookie({'name' : 'foo', 'value' : 'bar', 'path' : '/', 'secure':True})
        """
        self.driver.add_cookie(cookie)

    def delete_cookies(self):
        """
        清理之前所有的cookies
        """
        self.driver.delete_all_cookies()

    def delete_cookie(self, name):
        """
        清理之前所有的cookies
        :param name: 需要被删除的cookie的name
        """
        self.driver.delete_cookie(name)

    def get_cookies(self):
        """
        获取所有的cookie
        """
        self.driver.get_cookies()

    def minimize_window(self):
        """
        窗口最小化
        """
        self.driver.minimize_window()

    def maximize_window(self):
        """
        窗口最大化
        """
        self.driver.maximize_window()

    def current_url(self):
        """
        current_url
        """
        return self.driver.current_url
