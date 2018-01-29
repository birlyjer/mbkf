#coding=utf-8
from selenium import webdriver
from time import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from resource.resource import *
from resource.page_elements import *
from resource.logger import *



browser = webdriver.Chrome()

browser.implicitly_wait(30)

browser.get(login_url_ui)

# browser_xp(login().username).send_keys('admin88')
#
# browser_xp(login().pwd).send_keys('123123')
#
# browser_xp(login().submit).click()


browser.find_element_by_xpath(login('username')).send_keys('admin88')

browser.find_element_by_xpath(login('pwd')).send_keys('123123')

browser.find_element_by_xpath(login('submit')).click()

browser.maximize_window()
browser.find_element_by_xpath(jxcgl('jxcgl')).click()
sleep(1)
browser.find_element_by_xpath(jxcgl('jxc_rs')).click()
sleep(1)
browser.find_element_by_xpath(jxcgl('drugin')).click()
sleep(1)
browser.find_element_by_xpath(jxcgl('drugout')).click()

browser.switch_to.frame('iframe4')
sleep(2)

s=browser.find_element_by_xpath('//*[@id="table_info"]').text
l=s[17:-2]
l=l.replace(',','')
print(s,l)
i=1
while i <= int(int(l)/20):

    browser.find_element_by_css_selector('#table_next > a').click()
    logger.info('当前是第%d页' % (i+1))

    sleep(1)
    i+=1




