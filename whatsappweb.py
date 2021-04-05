from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import seed
from random import randint

def randomn_number() :
 value = randint(1000, 9999)
 return value



contact = 'rohit'
username = 'YOUR TINDER OTP IS: '
enter = '\n'

driver = webdriver.Firefox(executable_path="C:\\Users\\NITIN ARUL\\Pictures\\geckodriver.exe")


url='https://web.whatsapp.com/'

driver.get(url)
time.sleep(20)

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(contact)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(enter)

#driver.find_element_by_link_text(contact).click()
#driver.find_element_by_xpath('//*[@title="'+ contact + '"]').click()


for i in range(0,100) :
 time.sleep(1)
 #driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(username + str(randomn_number()))
 driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys('nigger')
 #driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(Keys.TAB)
 driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(enter)







