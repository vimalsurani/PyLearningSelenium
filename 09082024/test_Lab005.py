from selenium import webdriver


def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.page_source)
