from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GooglePage:
    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get("https://www.google.com")

    def search(self, keyword):
        wait = WebDriverWait(self.driver, 10)
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)
