from selenium import webdriver


def test():
    browser = webdriver.Chrome()
    browser.get("https://en.wikipedia.org/wiki/Main_Page")
    assert 'Booking' in browser.title
    browser.quit()


