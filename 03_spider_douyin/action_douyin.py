# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 22:55
# @Author  : Nixin
# @Email   : nixin@foxmail.com
# @File    : action_douyin.py
# @Software: PyCharm

from appium import webdriver
from time import sleep
import random


class Action():
    def __init__(self):
        # 初始化配置，设置Desired Capabilities参数
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "192.168.0.135:5555",
            "appPackage": "com.ss.android.ugc.aweme.lite",
            "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
            'newCommandTimeout': "36000",
            "noReset": True,
            "noSign": True
        }
        # 指定Appium Server
        self.server = 'http://localhost:4723/wd/hub'
        # 新建一个Session
        self.driver = webdriver.Remote(self.server, self.desired_caps)

        print(self.driver.get_window_size())
        # 设置滑动初始坐标和滑动距离
        self.x = self.driver.get_window_size()['width']
        self.y = self.driver.get_window_size()['height']
        self.start_x = 1/2*self.x
        self.start_y = 1/2*self.y
        self.distance = 120

    def comments(self):
        sleep(3)
        # app开启之后点击一次屏幕，确保页面的展示
        # self.driver.tap([(360, 604)], 500)

    def scroll(self):
        # 无限滑动
        while True:
            # 设置延时等待 5-10秒 随机
            r = random.choice(range(3, 11))
            print("%d秒后再滑屏：%d,%d,%d,%d" % (r, self.start_x, int(1 / 2 * self.y), self.start_x, int(1 / 6 * self.y)))
            sleep(r)

            # 模拟滑动
            self.driver.swipe(self.start_x, int(1/2*self.y), self.start_x, int(1/6*self.y), 300)

    def start(self):
        self.comments()
        self.scroll()


if __name__ == '__main__':
    action = Action()
    action.start()
    pass
