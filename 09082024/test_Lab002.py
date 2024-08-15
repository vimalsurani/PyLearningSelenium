import time

from selenium import webdriver


def test_open_vwologin():

    driver = webdriver.Chrome()
    # driver = webdriver.Edge()
    # driver = webdriver.Firefox()

    # Code -> HTTP REQUEST - POST
    # Request | Create the Session
    # Session is created - Unique ID - 16-digit ID
    # 20f0c4bb64cb76763d62e7ea85297942
    # Code -> HTTP REQUEST -. CHROMEDRIVER -> CHROME (SessionID)

    print(driver.session_id)  # 20f0c4bb64cb76763d62e7ea85297942
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"
    time.sleep(5)  # Python Int - to stop for the 10 seconds
