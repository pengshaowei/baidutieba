# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class weiboservice:
	def __init__(self):
		pass
	def login(self):
		driver =webdriver.Chrome()
		driver.maximize_window()
		driver.get('http://weibo.com')
		time.sleep(1)
		div = driver.find_element_by_xpath("//div[@class='tab clearfix']")
		a = div.find_elements_by_xpath(".//a")
		for i in a:
			i.click()
		driver.find_element_by_name('username').send_keys("18356133839")
		driver.find_element_by_name('password').send_keys('73647626934p')
		driver.find_element_by_name('password').send_keys(Keys.ENTER)


		time.sleep(5)

if __name__ == '__main__':
	weibo = weiboservice()
	weibo.login()

