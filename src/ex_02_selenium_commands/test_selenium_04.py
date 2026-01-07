from selenium import webdriver
import allure
import pytest

@allure.title("Print page source of the page")
def test_selenium_01():
    driver = webdriver.Chrome()
    driver.get("https://thetestingacademy.com")
    print(driver.page_source) 