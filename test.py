from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import  time

def test():
    chrome_options = Options()
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    browser.get("https://en.wikipedia.org/wiki/Main_Page")
    browser.quit()


