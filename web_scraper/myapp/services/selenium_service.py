from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys

def setup_selenium_driver():
    options = Options()
    options.headless = True
    chrome_service = Service(executable_path='/home/razvan/Desktop/Nokia/web_scraping/web_scraper/myapp/webdriver/chromedriver-linux64/chromedriver')
    driver = webdriver.Chrome(service=chrome_service, options=options)
    return driver

def search_wikipedia(subject):
    driver = setup_selenium_driver()
    
    try:
        driver.get("https://google.com")

        accept_btns = driver.find_elements(By.CLASS_NAME, "QS5gu.sy4vM")

        btn = accept_btns[1]
        btn.click()

        input_element = driver.find_element(By.CLASS_NAME, "gLFyf" )
        input_element.send_keys("wikipedia " + subject)
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

        print(first_paragraph.text[:200])

        time.sleep(3)

        print(second_paragraph.text[:200])

        time.sleep(5)
        return {
            "title": title.text,
            "paragraph1": first_paragraph.text,
            "paragraph2": second_paragraph.text,
        }

    finally:
        driver.quit()  # Închide browserul

# article = search_wikipedia("Formula 1");
# print("---------")
# print(article)