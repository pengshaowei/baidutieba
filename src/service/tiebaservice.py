# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from superdao import superdao
import time

class tiebaservice:
	def __init__(self):
		self.invitationItem = {}
		self.itemList = []
		pass
	def crawl_homepage_info(self):
		browser = webdriver.Chrome()
		browser.get('http://tieba.baidu.com/%E6%BB%81%E5%B7%9E%E5%AD%A6%E9%99%A2')
		time.sleep(0.1)
		print browser.title
		#browser.maximize_window()
		for i in range(1,5):
			browser.find_element_by_class_name('skin_normal').send_keys(Keys.END)
			browser.find_element_by_class_name('skin_normal').send_keys(Keys.PAGE_UP)
			time.sleep(0.1)
			divlist = browser.find_elements_by_xpath("//div[@class='threadlist_lz clearfix']")
			for l in divlist:
				try:
					self.invitationItem = {}
					title = l.find_element_by_xpath(".//a[@class='j_th_tit ']")
					self.invitationItem['title'] = title.get_attribute('title').encode('utf-8', 'ignore')
					username = l.find_element_by_xpath(".//a[@class='frs-author-name j_user_card ']")
					self.invitationItem['username'] = username.text.encode('utf-8', 'ignore')
					self.itemList.append(self.invitationItem)
					pass
				except:
					print 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
			print u'爬取第'+str(i)+u'页面的内容' + browser.current_url
			browser.find_element_by_class_name('skin_normal').send_keys(Keys.END)
			browser.find_element_by_class_name('skin_normal').send_keys(Keys.PAGE_UP)
			browser.find_element_by_link_text('下一页>').click()
		print '爬取完成'
		#time.sleep(999)
		#browser.quit()

	def save_invitation_info(self):
		dao = superdao(host='localhost',db='test',user='root',password='1234')
		dao.save_records('tb_baidutieba',self.itemList)
		pass

if __name__ == "__main__":
	tieba = tiebaservice()
	tieba.crawl_homepage_info()
	print tieba.itemList
	tieba.save_invitation_info()




