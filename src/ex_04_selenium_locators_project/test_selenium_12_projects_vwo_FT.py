import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import allure

@allure.title("Negative TC- incorrect username and password--->error message")
@allure.description("Verify if incorrect username and password is added you get a error message")
def test_login_vwo_app():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # <a
    # href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class="text-link"
    # data-qa="bericafeqo">
    # Start a free trial
    # </a>

    # Link Text and PARTIAL Text COncept

    # LINK_TEXT == Full Exact Match

    # anchor_tag_element = driver.find_element(By.LINK_TEXT,"Start an free trial")
    # anchor_tag_element.click()

    # PARTIAL_LINK_TEXT - contains
    anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Start")
    anchor_tag_element.click()

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"


    all_links_page = driver.find_elements(By.TAG_NAME, "a")
    print(len(all_links_page))
    for i in all_links_page:
        print(i.text)


    driver.quit()
