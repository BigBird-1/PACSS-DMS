import time

from readConfig import read_config
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BaseMethod(object):
    BASE_URL = read_config.get_http("base_url")[:-11:]

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def open(self, url, wait=0):
        """打卡浏览器"""
        self.driver.get(url)
        self.driver.maximize_window()
        if wait != 0:
            self.wait(wait)

    @staticmethod
    def wait(sleep_time):
        """强制等待"""
        time.sleep(sleep_time)

    def quit_s(self):
        """退出浏览器"""
        self.driver.quit()

    def switch_window(self, window=1, close=False):
        """切换窗口"""
        ha = self.driver.window_handles
        if close:
            self.driver.close()
        self.driver.switch_to.window(ha[window])

    def locate(self, ele_tuple):
        """
        处理传过来的Xpath路径,
        :param ele_tuple: 元组或者字符串
        :return:
        """
        if isinstance(ele_tuple, str):
            return self.driver.find_element("xpath", ele_tuple)
        else:
            return self.driver.find_element(*ele_tuple)

    def click(self, ele_tuple, wait=0):
        """点击事件"""
        self.locate(ele_tuple).click()
        if wait != 0:
            self.wait(wait)

    def input(self, ele_tuple, txt, wait=0):
        """输入框输入"""
        self.locate(ele_tuple).clear()
        self.locate(ele_tuple).send_keys(txt)
        if wait != 0:
            self.wait(wait)

    def select(self, ele_tuple, txt):
        """下拉框选择"""
        self.click(ele_tuple, wait=1)
        self.driver.find_elements("xpath", "//span[text()={}]".format(txt))[0].click()
        self.wait(0.5)

    def double_click(self, ele_tuple):
        """左键双击事件"""
        ActionChains(self.driver).double_click(self.locate(ele_tuple)).perform()

    def web_driver_wait(self, ele_tuple):
        """显示等待10秒"""
        return WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locate(ele_tuple), message="未找到元素！")










