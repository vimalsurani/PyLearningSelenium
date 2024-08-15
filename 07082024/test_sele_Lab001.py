from selenium import webdriver
from selenium.webdriver.edge.service import Service


def test_sample():

    # Selenium 3 - Not much used now
    # driver_path = 'C:/Users/ViMS/Downloads/edgedriver_win64/msedgedriver.exe'
    # service = Service(executable_path=driver_path)
    # driver = webdriver.Edge(service=service)
    # driver.get("https://www.google.com/")

    # Selenium 4 ( Selenium manager) - who will download the driver by itself)
    driver = webdriver.Edge()
    driver.get("https://www.google.com/")
    assert driver.current_url == "https://www.google.com/"
