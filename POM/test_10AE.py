from base_pages import AutomationExercise, AESubscribe
from locators import AutomationExerciseLocators
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

'''
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Scroll down to footer
5. Verify text 'SUBSCRIPTION'
6. Enter email address in input and click arrow button
7. Verify success message 'You have been successfully subscribed!' is visible
'''

addon_path = os.environ.get("adblock_plus")

def test_subscription(get_driver):
    driver = get_driver
    driver.install_addon(addon_path, temporary=True)
    driver.get(AutomationExercise.base_url)

    assert driver.find_element(By.XPATH, AutomationExerciseLocators.home_icon), "Home page not loaded"

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    assert driver.find_element(By.XPATH, AutomationExerciseLocators.subscribe_verify), "SUBSCRIPTION text not visible"

    AESubscribe.subscribe_fill_out(driver)

    AESubscribe.subscribe_click(driver)

    assert driver.find_element(By.XPATH, AutomationExerciseLocators.subscribe_success), "'Subscribe success' message not " \
                                                                                        "visible"



