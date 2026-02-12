import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_svg():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    # time.sleep(2)

    driver.find_element(By.XPATH, "//button[contains(text(),'I understand and agree')]").click()
    time.sleep(1)
    state_list = driver.find_elements(By.XPATH,
                                      "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")

    no_state = "ABCState"
    #target_state = "Maharashtra "
    state_found = False
    for state in state_list:
        try:
            state.get_attribute("aria-label")
            print(state.get_attribute("aria-label"))
            # time.sleep(2)
            if no_state in state.get_attribute("aria-label"):
                state.click()
                state_found = True
                break
        except Exception as e:
            print(f"Skip this state due to: {e}")
        continue
    if not state_found:
        raise NoSuchElementException(f"State '{no_state.strip()}' was not available")

    time.sleep(5)