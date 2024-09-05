from django.http import JsonResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os



def scrape_wikipedia(request, query):
    service = Service(executable_path=os.path.join(os.getcwd(), 'chromedriver'))
    driver = webdriver.Chrome(service=service)
    if not query:
        return JsonResponse({'error': 'No query provided'}, status=400)

    try:
        driver.get("https://google.com")

        accept_btns = driver.find_elements(By.CLASS_NAME, "QS5gu.sy4vM")

        btn = accept_btns[1]
        btn.click()

        input_element = driver.find_element(By.CLASS_NAME, "gLFyf" )
        input_element.send_keys("wikipedia " + query)
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

        # Returnează datele ca JSON
        return JsonResponse({
            'title': title.text,
            'first_paragraph': first_paragraph.text,
            'second_paragraph': second_paragraph.text
        })

    except Exception as e:
        print(f"Eroare capturată: {e}")
        return JsonResponse({'error': str(e)}, status=500)

    finally:
        # Închide driver-ul Chrome, chiar dacă apare o eroare
        driver.quit()
