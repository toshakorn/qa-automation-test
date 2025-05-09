from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_google_title():
    # เรียกใช้ Chrome browser ผ่าน webdriver-manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get("https://www.google.com")  # เปิดเว็บ Google

    assert "Google" in driver.title  # ตรวจสอบว่า title มีคำว่า Google

    driver.quit()  # ปิด browser
