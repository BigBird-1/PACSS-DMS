import time
import unittest
from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Dd(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "https://dms.t.hxqcgf.com/#/sso/login"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐性等待30秒
        self.driver.get(self.url)

    def slide(self):
        """滑动解锁"""
        div = self.driver.find_element_by_xpath("//form[@class='el-form']/div[4]/div/div[3]")
        action = ActionChains(self.driver)
        action.click_and_hold(div).perform()
        action.move_to_element_with_offset(to_element=div, xoffset=478, yoffset=0).release().perform()

    def login(self, username, password):
        self.driver.find_element_by_xpath("//form[@class='el-form']/div[1]/div/div/div/input").clear()
        self.driver.find_element_by_xpath("//form[@class='el-form']/div[1]/div/div/div/input").send_keys("HD340400")
        self.driver.find_element_by_xpath("//form[@class='el-form']/div[1]/div/div/div/input").send_keys(Keys.TAB)
        self.driver.find_element_by_xpath("//form[@class='el-form']/div[2]/div/div/input").clear()
        self.driver.find_element_by_xpath("//form[@class='el-form']/div[2]/div/div/input").send_keys(username)
        self.driver.find_element_by_xpath("//form[@class='el-form']/div[3]/div/div/input").clear()
        self.driver.find_element_by_xpath("//form[@class='el-form']/div[3]/div/div/input").send_keys(password)
        self.slide()
        self.driver.find_element_by_xpath("//form[@class='el-form']/div[5]/button").click()

    @parameterized.expand([("A08D", "hxqc2020!"), ("linjinjun", "123456")])
    def test_case(self, user, psd):
        self.login(user, psd)
        # self.assertEqual(self.driver.find_element_by_xpath("//div[@class='envShow']/span").text, "测试线环境")
        self.assertTrue(self.driver.find_element_by_xpath("//div[@class='envShow']/span"))

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

































