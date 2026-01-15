from selenium import webdriver
from selenium.webdriver.common.by import By
def test_web_tables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()

    #find the no of rows and col
    #rows
    #//tables



