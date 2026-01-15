import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException ,StaleElementReferenceException

@allure.title("stale_element")
@allure.description("stale_element")
def test_stale_element_exp_demo():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    time.sleep(5)
    try:


       textarea= driver.find_element(By.NAME,"q")
       driver.refresh()
       textarea.send_keys("The Testing Academy")
       print("end of Test case")
    except StaleElementReferenceException as see:
        print(see.msg)
    time.sleep(5)

    # response = {'status': 404, 'value': '{"value":{"error":"stale element reference","message":"stale element reference: stale element
    #if page is refreshed or dom structure changes it gives stale exception,mostly happens in modern application

