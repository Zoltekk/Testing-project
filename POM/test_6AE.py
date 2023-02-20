from base_pages import AutomationExercise, AEContactUs
from locators import AutomationExerciseLocators, AEContactLocators
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

'''
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Contact Us' button
5. Verify 'GET IN TOUCH' is visible
6. Enter name, email, subject and message
7. Upload file
8. Click 'Submit' button
9. Click OK button
10. Verify success message 'Success! Your details have been submitted successfully.' is visible
11. Click 'Home' button and verify that landed to home page successfully
'''


def test_contact_form(get_driver):
    email = os.environ.get("email")
    name = os.environ.get("name")
    filepath = os.environ.get("test6uploadfile")

    driver = get_driver
    driver.get(AutomationExercise.base_url)

    assert driver.find_element(By.XPATH, AutomationExerciseLocators.home_icon)

    contact_button = driver.find_element(By.XPATH, AutomationExerciseLocators.contact_button)
    contact_button.click()

    assert driver.find_element(By.XPATH, AEContactLocators.contact_verify)

    AEContactUs.fill_out(name, email, "This is a subject", "This is a message", driver)

    AEContactUs.upload_and_submit(filepath, driver)

    driver.switch_to.alert.accept()

    assert driver.find_element(By.XPATH, AEContactLocators.contact_success)

    contact_home_button = driver.find_element(By.XPATH, AEContactLocators.contact_home)
    contact_home_button.click()

    assert driver.find_element(By.XPATH, AutomationExerciseLocators.home_icon)
