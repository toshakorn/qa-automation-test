from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.parametrize("keyword", ["Selenium", "Python", "ChatGPT"])
def test_search_wikipedia(keyword):
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org/")

    driver.find_element(By.ID, "searchInput").send_keys(keyword)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "content"))
    )

    # ✅ ตรวจใน HTML แทน title
    assert keyword.lower() in driver.page_source.lower()

    driver.quit()
