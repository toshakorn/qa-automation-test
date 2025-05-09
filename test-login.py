import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# อ่าน username/password จาก login_data.json
def read_login_data(file_path):
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
        return [(item["username"], item["password"]) for item in data]

@pytest.mark.parametrize("username, password", read_login_data("login_data.json"))
def test_login_check_logout_button(username, password):
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/logout']"))
        )
        result = "✅ SUCCESS"
        print(f"{result}: {username} / {password}")
    except:
        result = "❌ FAILED"
        print(f"{result}: {username} / {password}")

    # 📝 บันทึกผลลัพธ์ลงไฟล์
    with open("login_result.txt", "a", encoding="utf-8") as f:
        f.write(f"{username} / {password} : {result}\n")

    driver.quit()
