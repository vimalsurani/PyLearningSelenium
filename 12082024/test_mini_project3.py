# Selenium Mini Project #3

# Open the URL - https://www.idrive360.com/enterprise/login
# Enter the username, password
# Verify that Trial is finished and current URL also
# Add a logic to add Allure Screen for the Trail end

# username : augtest_040823@idrive.com
# password : 123456

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure


@allure.title("Mini Project# 3")
@allure.description("Verify if the trial period has expired and prompt the user to upgrade.")
def test_mini_project3():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("Browser window maximized.")

    # Open the target URL
    driver.get("https://www.idrive360.com/enterprise/login")
    print("Navigated to the login page.")

    # Enter the username
    email_web_element = driver.find_element(By.ID, "username")
    email_web_element.send_keys("augtest_040823@idrive.com")
    print("Entered the username.")

    # Enter the password
    password_web_element = driver.find_element(By.ID, "password")
    password_web_element.send_keys("123456")
    print("Entered the password.")

    # Click the Sign In button
    sign_in_btn_web_element = driver.find_element(By.ID, "frm-btn")
    sign_in_btn_web_element.click()
    print("Clicked on the 'Sign In' button.")

    # Wait for the page to load
    time.sleep(20)
    print("Waited for the page to load.")

    # Verify that the current URL is the upgrade page
    expected_url = "https://www.idrive360.com/enterprise/account?upgradenow=true"
    assert driver.current_url == expected_url, \
        f"URL verification failed. Expected: {expected_url}, but got: {driver.current_url}"
    print("Verified that the URL has changed to the upgrade page.")

    # Verify that the upgrade prompt is displayed
    upgrade_now_btn_web_element = driver.find_element(By.CLASS_NAME, "id-card-title")
    assert upgrade_now_btn_web_element.is_displayed(), "Upgrade prompt is not displayed as expected."
    print("Verified that the upgrade prompt is displayed.")

    # Attach a screenshot to the Allure report
    allure.attach(driver.get_screenshot_as_png(), name='upgrade_screenshot')
    print("Attached screenshot to the Allure report.")

    # Close the browser
    driver.quit()
    print("Closed the browser.")
