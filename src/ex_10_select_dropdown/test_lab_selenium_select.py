import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException

@allure.title("Dropdown")
@allure.description("Verify dropdown")
def test_dropdown_list():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    #<select id="dropdown">


    select_html_tag = driver.find_element(By.ID, "dropdown")
    select = Select(select_html_tag)
    select.select_by_visible_text("Option 2")
    time.sleep(5)
    driver.quit()






