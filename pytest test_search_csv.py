import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

def read_keywords_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row["keyword"] for row in reader]

@pytest.mark.parametrize("keyword", read_keywords_from_csv("search_data.csv"))
def test_search_wikipedia_csv(keyword):
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org/")

    driver.find_element(By.ID, "searchInput").send_keys(keyword)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "content"))
    )

    assert keyword.lower() in driver.page_source.lower()

    driver.quit()
