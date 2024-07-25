import time
from lxml import etree

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://101.qq.com/#/hero')
time.sleep(5)

input = browser.find_element(by=By.XPATH, value='//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/input')
input.send_keys("离群之刺")

btn = browser.find_element(by=By.XPATH, value='//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/a')
btn.click()

# 浏览器窗口必须存在滚动条才能进行滚动
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

time.sleep(3)
browser.quit()

