from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_xpath_dynamic():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.wikipedia.org/")

    # ใช้ XPath ที่มี contains()
    title = driver.find_element(By.XPATH, "//strong[contains(text(), 'Encyclopedia')]")
    assert title.text == "The Free Encyclopedia"
    time.sleep(200)
    driver.quit()
