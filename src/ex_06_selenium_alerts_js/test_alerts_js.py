from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import allure
import time
from selenium.webdriver.support.wait import WebDriverWait

@allure.title("Alerts")
@allure.description("Verify Alerts")
def test_alerts_js_normal():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_promt= driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    element_promt.click()

    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()

    result_message = driver.find_element(By.ID, "result").text
    assert result_message == "You successfully clicked an alert"

    time.sleep(5)

def test_alerts_js_confirm():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_promt = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    element_promt.click()

    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.dismiss()

    result_message = driver.find_element(By.ID, "result").text
    assert result_message == "You clicked: Cancel"

    time.sleep(5)

def test_alerts_js_prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_promt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    element_promt.click()

    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.send_keys("Sneha")
    alert.accept()

    result_message = driver.find_element(By.ID, "result").text
    assert result_message == "You entered: Sneha"


    time.sleep(5)