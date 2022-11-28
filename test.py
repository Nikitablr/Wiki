from selenium import webdriver


def test():
    browser = webdriver.Chrome()
    browser.get("https://en.wikipedia.org/wiki/Main_Page")
    browser.quit()


