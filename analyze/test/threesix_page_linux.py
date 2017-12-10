from selenium import webdriver
import time
from bs4 import BeautifulSoup
from data.spider_tool.proxy import *
from selenium.webdriver.common.proxy import Proxy
import datetime
from common_tool.mysql_tool.mysql_tool import *
import traceback
from pyvirtualdisplay import Display

#display = Display(visible=0, size=(800,600))
#display.start()


browser = webdriver.Firefox()
browser.get('https://www.bet365.com/')
print(browser.page_source)
#browser.find_element_by_css_selector("a[class=\"lpdgl\"]").click()
#browser.find_element_by_link_text('简体中文').click()

browser.find_element_by_css_selector('a[href=\"https://www.bet365.com/zh-CHS/\"').click()
#browser.find_element_by_css_selector('a[href=\"https://www.bet365.com/home/?lng=10\"').click()
browser.find_element_by_css_selector("a[class=\"lpdgl\"]").click()


time.sleep(5)
print(browser.page_source)
browser.close()
#display.stop()