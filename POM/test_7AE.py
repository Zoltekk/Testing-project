from base_pages import AutomationExercise
from locators import AutomationExerciseLocators
from selenium.webdriver.common.by import By

'''
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Test Cases' button
5. Verify user is navigated to test cases page successfully
'''


def test_testcase(get_driver):
    driver = get_driver
    driver.get(AutomationExercise.base_url)

    assert driver.find_element(By.XPATH, AutomationExerciseLocators.home_icon)

    test_cases_button = driver.find_element(By.XPATH, AutomationExerciseLocators.test_cases_button)
    test_cases_button.click()

    assert driver.find_element(By.XPATH, AutomationExerciseLocators.test_cases_verify)