import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_open_vwologin():
    # Options Class - What is the class?
    # Customize the behavior of the browser during automated testing.
    # Chrome -> Headless or UI -> Headless Mode -> No UI
    # Disable GPU, Add extension, Maximize, Set Windows... 100 other options that you can do before starting the Browser
    # Create an instance of ChromeOptions

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--disable-infobars")
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")
    time.sleep(5)
