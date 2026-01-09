"""**Project 1 - Automating by using the Selenium Python. **
1. Navigate to the URL - katalon-demo-cura.herokuapp.com](https://katalon-demo-cura.herokuapp.com/profile.php#login)
2. Find the **Make appointment** Button
3. Click on the **Make appointment **Button
4. Next Page will be loaded
5. **Find and Enter **the details **Username and Password** and **Click** on the Login Button
6. Verify current URL - katalon-demo-cura.herokuapp.com/#appointment](https://katalon-demo-cura.herokuapp.com/#appointment) """

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_project1_katalon_positive():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")


#find the element
#<a - atribute
#id="btn-make-appointment"
#href="./profile.php#login"
#class="btn btn-dark btn-lg">
# Make Appointment
#</a>"""

    make_appointment_button = driver.find_element(By.ID , "btn-make-appointment")
    make_appointment_button.click()

    #< input
    #type = "text"
   # class ="form-control"
    # #id="txt-username"
    #name="username"
    #placeholder="Username"
    #value=""
    #autocomplete="off"
    #fdprocessedid="owcj8" >

    username_input_box= driver.find_element(By.NAME, "username")
    username_input_box.send_keys("John Doe")

    #< input
    #type = "password"
    #class ="form-control"
    # #id="txt-password"
    # name="password"
    # placeholder="Password"
    # value=""
    # autocomplete="off"
    # fdprocessedid="ncixtp" >

    password_input_box = driver.find_element(By.NAME, "password")
    password_input_box.send_keys("ThisIsNotAPassword")

    #< button
    #id = "btn-login"
    #type = "submit"
    #class ="btn btn-default"
    # fdprocessedid="dwt7i" > Login < / button >

    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()

    time.sleep(5)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"


    time.sleep(5)
    driver.quit()

def test_project1_katalon_negative():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")


#find the element
#<a - atribute
#id="btn-make-appointment"
#href="./profile.php#login"
#class="btn btn-dark btn-lg">
# Make Appointment
#</a>"""

    make_appointment_button = driver.find_element(By.ID , "btn-make-appointment")
    make_appointment_button.click()

    #< input
    #type = "text"
   # class ="form-control"
    # #id="txt-username"
    #name="username"
    #placeholder="Username"
    #value=""
    #autocomplete="off"
    #fdprocessedid="owcj8" >

    username_input_box= driver.find_element(By.NAME, "username")
    username_input_box.send_keys("sneha")

    #< input
    #type = "password"
    #class ="form-control"
    # #id="txt-password"
    # name="password"
    # placeholder="Password"
    # value=""
    # autocomplete="off"
    # fdprocessedid="ncixtp" >

    password_input_box = driver.find_element(By.NAME, "password")
    password_input_box.send_keys("sneha123")

    #< button
    #id = "btn-login"
    #type = "submit"
    #class ="btn btn-default"
    # fdprocessedid="dwt7i" > Login < / button >

    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()

    time.sleep(5)

    #< p class ="lead text-danger" > Login failed! Please ensure the username and password are valid.< / p >

    error_message_p_tag = driver.find_element(By.CLASS_NAME ,"text-danger ")
    print(error_message_p_tag.text)

    assert "Login failed! Please ensure the username and password are valid."==error_message_p_tag.text



    time.sleep(5)
    driver.quit()
