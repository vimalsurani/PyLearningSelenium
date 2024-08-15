import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure

@pytest.mark.positive
@allure.title("Verify that URL changes")
@allure.description("Verify the URL changes from the homepage to the login page, and then to the appointment page "
                    "after logging in.")
def test_mini_project4():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigate to the URL
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print("Navigated to the application URL.")

    # Click on the "Make Appointment" button
    make_appointment_btn_web_element = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_btn_web_element.click()
    print("Clicked on 'Make Appointment' button.")

    # Verify that the URL has changed to the login page
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", \
        f"URL did not change as expected. Current URL: {driver.current_url}"
    print("Verified that the URL has changed to the login page.")

    # Pause execution for 3 seconds
    time.sleep(3)

    # Enter the username
    username_web_element = driver.find_element(By.ID, "txt-username")
    username_web_element.send_keys("John Doe")
    print("Entered the username.")

    # Enter the password
    password_web_element = driver.find_element(By.ID, "txt-password")
    password_web_element.send_keys("ThisIsNotAPassword")
    print("Entered the password.")

    # Click on the "Login" button
    login_btn_web_web_element = driver.find_element(By.ID, "btn-login")
    login_btn_web_web_element.click()
    print("Clicked on 'Login' button.")

    # Pause execution for 3 seconds
    time.sleep(3)

    # Verify that the URL has changed to the appointment page
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", \
        f"URL did not change to the appointment page as expected. Current URL: {driver.current_url}"
    print("Verified that the URL has changed to the appointment page.")

    # Pause execution for 5 seconds
    time.sleep(5)

    # Verify that the "Make Appointment" text is present on the page
    make_appointment_element = driver.find_element(By.TAG_NAME, "h2")
    assert make_appointment_element.text == "Make Appointment", \
        f"Expected 'Make Appointment' text not found. Found: {make_appointment_element.text}"
    print("Verified that the 'Make Appointment' text is present on the page.")

    # Attach a screenshot to the Allure report
    allure.attach(driver.get_screenshot_as_png(), name='appointment_screenshot')
    print("Attached screenshot to the Allure report.")

    # Close the browser
    driver.quit()
    print("Closed the browser.")

