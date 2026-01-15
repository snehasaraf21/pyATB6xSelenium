#import time
from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support.wait import WebDriverWait



@allure.title("VWO app implicit wait")
@allure.description("Verify if VWo app login is working correctly with implicit wait")
def test_login_vwo_app_implicit_wait():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    email_element = driver.find_element(By.XPATH, "//input[@data-qa='hocewoqisi']")
    email_element.send_keys("wrong@vwo.com")

    password_web_element = driver.find_element(By.XPATH, "//input[@name='password']")
    password_web_element.send_keys("wrong@1234")

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    #wait for the error message
    #as per logic we need to add condition to make it wait till the error message appears
    #wait until this error message is visible "Your email, password, IP address or location did not match"
    #which takes around 2-4 secs

    ignore_list = [ElementNotVisibleException,ElementNotSelectableException]

    WebDriverWait(driver=driver,poll_frequency=1,timeout=3,ignored_exceptions=ignore_list).until(EC.visibility_of_element_located((By.CLASS_NAME, "notification-box-description")))

    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"