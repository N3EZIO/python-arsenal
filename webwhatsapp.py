from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




contact = '' #your contact
message = '' #your message
enter = '\n'

driver = webdriver.Firefox(executable_path="") #insert path of your webdriver


url='https://web.whatsapp.com/'

driver.get(url)
time.sleep(20)

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(contact)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(enter)




driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(message)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(enter)







