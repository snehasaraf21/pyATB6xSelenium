from selenium import webdriver
import allure
import pytest

@allure.title("Print page source of the page")
def test_selenium_01():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/ ")
    page_source_html= driver.page_source
    assert "CURA Healthcare Service" in page_source_html
    print(driver.title)
    print(driver.current_url)
    print(driver.page_source)

    driver.quit()

