from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time
import os

service = Service(executable_path=os.path.join(os.getcwd(), 'chromedriver'))
driver = webdriver.Chrome(service=service)
text = "Formula 1"

driver.get("https://google.com")

accept_btns = driver.find_elements(By.CLASS_NAME, "QS5gu.sy4vM")

btn = accept_btns[1]
btn.click()

input_element = driver.find_element(By.CLASS_NAME, "gLFyf" )
input_element.send_keys("wikipedia " + text)
time.sleep(1)
input_element.send_keys(Keys.ENTER)

time.sleep(1)

link_wikipedia = driver.find_element(By.CLASS_NAME, "LC20lb.MBeuO.DKV0Md");

time.sleep(1)

link_wikipedia.click()

time.sleep(1)

title = driver.find_element(By.CLASS_NAME, "mw-page-title-main");

print(title.text)

first_paragraph = driver.find_element(By.XPATH, "//div[@class='mw-content-ltr mw-parser-output']/p")

second_paragraph = driver.find_element(By.XPATH, "//div[@class='mw-content-ltr mw-parser-output']/p[2]")

print(first_paragraph.text)

time.sleep(3)

print(second_paragraph.text)

time.sleep(20)

driver.quit()