import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_applitools_demo():
    driver = webdriver.Chrome()
    driver.get("https://demo.applitools.com")

    username_input_textbox = driver.find_element(By.XPATH, "//input[@id='username']")
    username_input_textbox.send_keys("Admin")

    password_input_textbox = driver.find_element(By.XPATH, "//input[@id='password']")
    password_input_textbox.send_keys("Password@123")

    sign_in_btn = driver.find_element(By.XPATH, "//a[@id='log-in']")
    sign_in_btn.click()

    time.sleep(5)

    assert "app.html" in driver.current_url, "Not on the app.html page!"

    # table = driver.find_element(By.XPATH, '//div[@class="table-responsive"]//table')

    rows = driver.find_elements(By.XPATH, './/tbody/tr')

    total_amount = 0.0

    for row in rows:
        amount_text = row.find_element(By.XPATH, './td[5]').text

        # Remove currency symbol, commas, and spaces, then convert to float

        amount_text = amount_text.replace('USD', '').replace(',', '').replace(' ', '')
        amount = float(amount_text)
        total_amount += amount

    assert total_amount == 1996.22
