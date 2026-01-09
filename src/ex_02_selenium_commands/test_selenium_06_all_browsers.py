from selenium import webdriver
import allure
import pytest
import time

@allure.title("Print page source of the page")
def test_selenium_01():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/ ")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(5)
    driver.quit()

def test_selenium_02():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/ ")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(5)
    driver.quit()

def test_selenium_03():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/ ")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(5)
    driver.quit()



