"""Mini project VWO.com
// Locators - Find the Web elements
// Open the URL https://app.vwo.com/#/login
// Find the Email id** and enter the email as admin@admin.com
// Find the Pass inputbox** and enter passwrod as admin.
// Find and Click on the submit button
// Verify that the error message is shown "_**Your email, password, IP address or location did not match"**_"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_vwo_login_negative():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com/#/login")

#<input type="email" class="text-input W(100%)" name="username" vwo-html-translate-attr="placeholder" vwo-html-translate-placeholder="login:enterEmailID" id="login-username" data-qa="hocewoqisi" placeholder="Enter email ID" fdprocessedid="12x6s0c" data-gtm-form-interact-field-id="0">

    username_input_box = driver.find_element(By.ID, "login-username")
    username_input_box.send_keys("admin@admin.com")

#<input type="password" class="text-input W(100%)" vwo-html-translate-attr="placeholder" vwo-html-translate-placeholder="login:enterPassword" name="password" id="login-password" data-qa="jobodapuxe" placeholder="Enter password" fdprocessedid="06c8b7" data-gtm-form-interact-field-id="1">

    password_input_box = driver.find_element(By.ID, "login-password")

    password_input_box.send_keys("admin")


    #<button type="submit" id="js-login-btn" class="btn btn--primary btn--inverted W(100%) Mb(8px) Mb(0):lc" onclick="login.login(event)" data-qa="sibequkica" fdprocessedid="9csphi"> <span class="icon loader hidden" data-qa="zuyezasugu"></span> <span data-qa="ezazsuguuy" vwo-html-translate="login:signIn">Sign in</span> </button>

    sign_in_button= driver.find_element(By.ID, "js-login-btn")
    sign_in_button.click()

    time.sleep(5)

    ##<div class="notification-box-description" id="js-notification-box-msg" data-qa="rixawilomi">Your email, password, IP address or location did not match</div>

    error_message_p_tag = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_p_tag.text)


#<div class="notification-box-description" id="js-notification-box-msg" data-qa="rixawilomi">Your email, password, IP address or location did not match</div>
    assert "Your email, password, IP address or location did not match" == error_message_p_tag.text
    time.sleep(5)
    driver.quit()




