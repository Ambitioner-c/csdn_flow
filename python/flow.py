from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import time
import requests


def get_driver(executable_path):
    # 创建参数设置对象
    chrome_opt = Options()
    # # 无界面化
    # chrome_opt.add_argument('--headless')
    # # 配合上面的无界面化
    # chrome_opt.add_argument('--disable-gpu')

    # # 不加载图片
    # prefs = {"profile.managed_default_content_settings.images": 2}
    # chrome_opt.add_experimental_option("prefs", prefs)

    # 设置窗口大小, 窗口大小会有影响
    chrome_opt.add_argument('--window-size=1366,768')
    # 使用沙盒模式运行
    chrome_opt.add_argument("--no-sandbox")

    # 创建Chrome对象并传入设置信息
    driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_opt)

    return driver


def csdn(driver, url):
    driver.get(url)

    sleep(15)

    driver.get('https://blog-console-api.csdn.net/v1/article/list?pageSize=20')

    sleep(10)

    html = driver.page_source
    # html = BeautifulSoup(html, 'lxml')

    with open('../data/1.html', 'w') as f:
        f.write(html)
    # div = html.findAll('div', attrs={'class': 'review-main commentParentBox'})


if __name__ == '__main__':
    # chrome驱动的可执行路径
    my_executable_path = '/usr/local/bin/chromedriver/chromedriver'

    # 获得driver
    my_driver = get_driver(my_executable_path)

    # url
    my_url = 'https://passport.csdn.net/login'

    # 登录
    csdn(my_driver, my_url)
