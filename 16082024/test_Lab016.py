import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.positive
def test_flipkart_search_svg_demo():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()

    search_input = driver.find_element(By.NAME,"q")
    search_input.send_keys("AC")

    # search_icon = driver.find_element(By.XPATH,"//*[local-name()='svg']/*[contains(text(),'Search Icon'')]")
    svg_list = driver.find_elements(By.XPATH,"//*[local-name()='svg']")
    svg_list[0].click()



