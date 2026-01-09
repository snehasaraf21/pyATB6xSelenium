"""Mini project idrive360.com
// Locators - Find the Web elements
// Open the URL www.idrive360.com/enterprise/account?upgradenow=true](https://www.idrive360.com/enterprise/account?upgradenow=true)
// Find the Email id** and enter the email as augtest_040823@idrive.com
// Find the Password inputbox** and enter passwrod as 123456
// Find and Click on the sign In button
// Verify that the error message is shown "_**Your free trail has expired!"**_"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_idrive360_login_negative():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.idrive360.com/enterprise/login")

    time.sleep(5)

    # <input _ngcontent-mdy-c171="" type="email" id="username" name="username" autofocus="" class="id-form-ctrl ng-pristine ng-valid ng-touched" fdprocessedid="j8r3th">

    email_input_box = driver.find_element(By.ID, "username")
    email_input_box.send_keys("augtest_040823@idrive.com")

    # <input _ngcontent-mdy-c171="" id="password" name="password" tabindex="0" maxlength="20" class="id-form-ctrl ng-untouched ng-pristine ng-valid" type="password" fdprocessedid="khcpnm">
    password_input_box = driver.find_element(By.ID, "password")
    password_input_box.send_keys("123456")
    time.sleep(5)

    # <button _ngcontent-mdy-c171="" type="submit" id="frm-btn" class="id-btn id-info-btn-frm" fdprocessedid="ic6w5p">Sign in</button>
    sign_in_button = driver.find_element(By.ID, "frm-btn")
    sign_in_button.click()
    time.sleep(10)


    #<h5 _ngcontent-lpj-c141="" class="id-card-title">Your free trial has expired!</h5>
    error_message_p_tag = driver.find_element(By.CLASS_NAME, "id-card-title")
    print(error_message_p_tag.text)
    time.sleep(5)

    assert "Your free trial has expired!" == error_message_p_tag.text
    time.sleep(5)
    driver.quit()
