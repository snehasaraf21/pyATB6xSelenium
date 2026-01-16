import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException


@allure.title("SVG")
@allure.description("Verify SVG")
def test_SVG_flipkart():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("macmini")

    svg_element = driver.find_elements(By.XPATH,"//*[name()='svg']")
    svg_element[0].click()

    time.sleep(3)

