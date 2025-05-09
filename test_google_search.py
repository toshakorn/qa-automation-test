from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google_search():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")

    # ค้นหาช่อง search
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("ChatGPT")     # พิมพ์คำค้น
    search_box.send_keys(Keys.RETURN)   # กด Enter

    time.sleep(2)  # รอให้โหลดผลลัพธ์ (แนะนำใช้ WebDriverWait ภายหลัง)

    assert "ChatGPT" in driver.title  # ตรวจสอบว่า title มี ChatGPT
    driver.quit()
