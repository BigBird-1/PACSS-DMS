# -*- coding:utf-8 -*
# @FileName:   base_page.py
# @Author:     刘峰
# @CreateTime: 2022/7/19 10:05
'''
    封装常用关键字类，供page继承调用
'''
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    SERVER = "https://dms.hxqcgf.com/"

    # 初始化
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    # 打开浏览器
    def open(self, url, wait=0):
        self.driver.get(url)
        self.driver.maximize_window()
        if wait != 0:
            self.wait(wait)

    # 定位元素，loc为元组
    def locate(self, loc):
        if type(loc) is str:
            return self.driver.find_element("xpath", loc)
        else:
            return self.driver.find_element(*loc)

    # 点击元素
    def click(self, loc, wait=0):
        self.locate(loc).click()
        if wait != 0:
            self.wait(wait)

    # 通过text点击元素
    def clickByText(self, txt):
        loc = "//*[text()='{}']".format(txt)
        self.locate(loc).click()
        self.wait(0.5)

    # 输入内容
    def input(self, loc, txt, isclear=False, wait=0):
        if isclear:
            self.locate(loc).clear()
        self.locate(loc).send_keys(txt)
        if wait != 0:
            self.wait(wait)

    # 等待
    def wait(self, time_):
        time.sleep(time_)

    # 关闭driver
    def close(self):
        self.driver.quit()

    # 获取元素的值
    def getText(self, loc):
        return self.locate(loc).text

    # 下拉框选择
    def select(self, loc, txt, istxt=True):
        self.click(loc, 0.5)
        if istxt:
            elements = self.driver.find_elements("xpath", "//span[text()='{}']".format(txt))
        else:
            elements = self.driver.find_elements("css selector", 'li.el-select-dropdown__item')
        for element in elements:
            if txt == element.text:
                element.click()
                self.wait(0.5)
                break

    # 切换窗口
    def switchWindow(self, window=1, close=False):
        ha = self.driver.window_handles
        if close:
            self.driver.close()
        self.driver.switch_to.window(ha[window])

    # 显式等待
    def webDriverWait(self, loc):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locate(loc), message="未找到元素！")

    # 左键双击
    def doubleClick(self, loc):
        ActionChains(self.driver).double_click(self.locate(loc)).perform()

    # # 根据页面坐标进行点击
    # def clickByCoord(self, x, y):
    #     ActionChains(self.driver).move_by_offset(x, y).click().perform()

    # # 修改属性值
    # def editAttribute(self, loc, name, value):
    #     self.driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])", self.locate(loc), name, value)
    #
    # # 删除属性值
    # def deleteAttribute(self, loc, name):
    #     self.driver.execute_script("arguments[0].removeAttribute(arguments[1])", self.locate(loc), name)
