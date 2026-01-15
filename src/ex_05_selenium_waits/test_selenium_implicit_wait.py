import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import allure

@allure.title("VWO app implicit wait")
@allure.description("Verify if VWo app login is working correctly with implicit wait")
def test_login_vwo_app_implicit_wait():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    driver.implicitly_wait(5) # its not used anymore

    email_element = driver.find_element(By.XPATH, "//input[@data-qa='hocewoqisi']")
    email_element.send_keys("wrong@vwo.com")

    password_web_element = driver.find_element(By.XPATH, "//input[@name='password']")
    password_web_element.send_keys("wrong@1234")

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()



    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"


