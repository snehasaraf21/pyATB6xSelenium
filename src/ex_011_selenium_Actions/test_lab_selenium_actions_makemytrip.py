import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


@allure.title("Actions P3")
@allure.description("Verify Click and Hold")
def test_verify_action_makemytrip():
    # ChromeOptions - --incognito
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.global/flights/?lang=eng&_uCurrency=GBP&cc=uk&cmp=SEM%7CD%7CIF%7CA2A%7CG%7CBrand%7CIF_Brand_Exact-UK%7CBrand_Exact_UK-DT%7CRSA%7CRegular%7CUKFunnel&gad_source=1&gad_campaignid=22331108146&gbraid=0AAAAA-8w7HFFdfNw_sLyxae9Soo23eIzI&gclid=CjwKCAiAkbbMBhB2EiwANbxtbeoQzy1h2dyRkW9fx3qSLmc7VJSE_Lx0IJtavoqSDGk0ue5OQSgZOhoC6xoQAvD_BwE")
    driver.maximize_window()
    time.sleep(10)

    fromCity = driver.find_element(By.ID, "fromCity")

    # move mouse to our to fromcity
    # click on it
    # enter the blr or del
    # release up
    # enter.

    actions = ActionChains(driver)
    (actions.
     move_to_element(fromCity)
     .click().send_keys_to_element(fromCity, "lhr")
     .perform())

    time.sleep(2)

    (actions.move_to_element(fromCity)
     .key_down(Keys.ARROW_DOWN)
     .key_down(Keys.ENTER).perform())

    toCity = driver.find_element(By.ID, "toCity")
    actions = ActionChains(driver)
    (actions.
     move_to_element(fromCity)
     .click().send_keys_to_element(toCity, "bom")
     .perform())

    time.sleep(2)

    (actions.move_to_element(fromCity)
     .key_down(Keys.ARROW_DOWN)
     .key_down(Keys.ENTER).perform())


    time.sleep(5)
    driver.quit()