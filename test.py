from selenium import webdriver
import pytest

def test():
    browser = webdriver.Chrome()
    browser.get("https://en.wikipedia.org/wiki/Main_Page")


