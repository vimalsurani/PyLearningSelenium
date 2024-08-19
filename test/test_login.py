import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.positive
def test_alianhub_login():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Allow notifications
    prefs = {
        "profile.default_content_setting_values.notifications": 1  # 1 to allow notifications, 2 to block
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the URL
        driver.get("https://demo.alianhub.com/")

        # Example: Add your test steps here

        email_input = driver.find_element(By.ID, "email").clear()
        email_input = driver.find_element(By.ID, "email").send_keys("owner@example.com")
        password_input = driver.find_element(By.ID, "password").clear()
        password_input = driver.find_element(By.ID, "password").send_keys("Abc@1234")

        login_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        login_btn.click()

        WebDriverWait(driver=driver, timeout=15).until(EC.title_contains("Alian Hub | Home"))
        assert driver.title == "Alian Hub | Home"

        WebDriverWait(driver=driver, timeout=5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='cursor-pointer link-item h-100']"))
        )

        projects_menu = driver.find_element(By.XPATH, "//div[@class='cursor-pointer link-item h-100']")
        projects_menu.click()
        WebDriverWait(driver=driver, timeout=15).until(EC.title_contains("Alian Hub | Projects"))
        assert driver.title == "Alian Hub | Projects"

        WebDriverWait(driver=driver, timeout=25).until(
            EC.visibility_of_element_located((By.ID, "createtask_driver"))
        )

        task_btn = driver.find_element(By.ID, "createtask_driver")
        task_btn.click()

        WebDriverWait(driver=driver, timeout=15).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='inputId']"))
        )

        task_input = driver.find_element(By.XPATH, "//input[@id='inputId']")
        task_input.send_keys("Task 789")

        WebDriverWait(driver=driver, timeout=15).until(
            EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
        )
        task_save_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
        task_save_btn.click()

        task_name_element = driver.find_element(By.XPATH, "//span[@class='text-ellipsis d-inline-block edit__taskname' "
                                                          "and" "@title='Task 789']")

        task_name = task_name_element.text

        assert task_name == "Task 789", f"Expected task name 'Task 789' but got '{task_name}'"

        task_name_element.click()
        time.sleep(15)

        task_status = driver.find_element(By.CSS_SELECTOR, ".task-status-name")
        task_status.click()

        time.sleep(15)



    finally:
        # Close the browser
        driver.quit()
