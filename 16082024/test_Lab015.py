import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.mark.positive
def test_select_demo():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    element_select = driver.find_element(By.ID, "dropdown")
    select = Select(element_select)
    select.select_by_visible_text("Option 2")

    time.sleep(10)
