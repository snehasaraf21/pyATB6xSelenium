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
    driver.get("https://awesomeqa.com/practice.html")

    #<select id="dropdown">
    #<select class="input-xlarge" id="continents" name="continents" style="-webkit-appearance: none; appearance: none; background-color: #fcfcfc; background-position: 50% 50%; background-repeat: no-repeat; border-color: rgba(173, 176, 182, 0.3); color: #787d85; font-family: verdana, helvetica, arial, verdana, sans-serif; font-size: 13px; height: 38px; line-height: 22px; margin: 0px; outline: 0px; padding: 5px 15px; vertical-align: baseline;" fdprocessedid="ubuifv"><option style="margin: 0px; padding-bottom: 0px; padding-left: 0px; padding-right: 0px;">Asia</option><option style="margin: 0px; padding-bottom: 0px; padding-left: 0px; padding-right: 0px;">Europe</option><option style="margin: 0px; padding-bottom: 0px; padding-left: 0px; padding-right: 0px;">Africa</option><option style="margin: 0px; padding-bottom: 0px; padding-left: 0px; padding-right: 0px;">Australia</option><option style="margin: 0px; padding-bottom: 0px; padding-left: 0px; padding-right: 0px;">South America</option><option style="margin: 0px; padding-bottom: 0px; padding-left: 0px; padding-right: 0px;">North America</option><option style="margin: 0px; padding-bottom: 0px; padding-left: 0px; padding-right: 0px;">Antartica</option></select>


    select_html_tag = driver.find_element(By.ID, "continents")
    select = Select(select_html_tag)
    select.select_by_visible_text("South America")
    time.sleep(5)
    driver.quit()
