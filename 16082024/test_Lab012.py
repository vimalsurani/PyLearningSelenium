import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.positive
def test_vwo_login_invalid():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    email_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")

    email_input.send_keys("admin@gmail.com")
    pass_input.send_keys("admin")

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    # time.sleep(5) # This is Python Int who is waiting, Python Execution Halt.

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.ID, 'js-notification-box-msg'))
    )

    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"
