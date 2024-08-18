import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.positive
def test_katalon_demo():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # make_appointnment_btn = driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
    # make_appointnment_btn = driver.find_element(By.XPATH, "//a[@href='./profile.php#login']")
    make_appointnment_btn = driver.find_element(By.XPATH,"//a[text()='Make Appointment' and contains(@id,"
                                                "'btn-make-appointment')]")
    make_appointnment_btn = driver.find_element(By.CSS_SELECTOR, "#btn-make-appointment")
    make_appointnment_btn.click()

    time.sleep(5)
    driver.quit()
