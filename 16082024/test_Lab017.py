import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.positive
def test_amcharts_svg_demo():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()
    cookie_accept = driver.find_element(By.XPATH,"//input[@value='I agree']")
    cookie_accept.click()

    states = driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name("
                                           ")='path']")

    for state in states:
        print(state.get_attribute("aria-label"))
        if "Gujarat" in state.get_attribute("aria-label"):
            state.click()
            break

    time.sleep(5)




