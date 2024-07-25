import time
from lxml import etree

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('./chromedriver.exe')

browser = webdriver.Chrome(service=service)
print("打开浏览器")
browser.get('https://101.qq.com/#/hero')
time.sleep(3) # 非常重要

page_txt = browser.page_source
tree = etree.HTML(page_txt)

li_list = tree.xpath('//*[@class="hero-list"]/li')
for li in li_list:
    name = li.xpath('./div/p')[0].text
    print(name)
time.sleep(3)
browser.quit()
print("结束")
