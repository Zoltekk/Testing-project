from base_pages import AutomationExercise, AELoginSignup
from locators import AutomationExerciseLocators, AELSLocators
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


'''
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'New User Signup!' is visible
6. Enter name and already registered email address
7. Click 'Signup' button
8. Verify error 'Email Address already exist!' is visible
'''


def test_already_exist(get_driver):
    email = os.environ.get("email")
    name = os.environ.get("name")

    driver = get_driver
    driver.get(AutomationExercise.base_url)

    assert driver.find_element(By.XPATH, AutomationExerciseLocators.home_icon), "Home page not loaded"

    login_button = driver.find_element(By.XPATH, AutomationExerciseLocators.login_subpage)
    login_button.click()

    assert driver.find_element(By.XPATH, AELSLocators.signup_form), "'New User Signup!' is not visible"

    AELoginSignup.sign_up(email, name, driver)

    assert driver.find_element(By.XPATH, AELSLocators.signup_verify), "'Email Address already exists!' is not visible"
