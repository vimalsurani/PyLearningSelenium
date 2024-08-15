import time

from selenium import webdriver


def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.refresh()
    driver.back()
    driver.forward()
    print(driver.page_source)

    # driver.close()
    # It will close the current window or tab.
    # Session id != null(Invalid)
    # It will not close the other tabs.

    time.sleep(5)
    driver.quit()

    # Close the all tabs
    # Session id == Null

