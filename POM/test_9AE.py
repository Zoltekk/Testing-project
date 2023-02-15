from base_pages import AutomationExercise
from locators import AutomationExerciseLocators, AEProductsLocators
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

'''
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Products' button
5. Verify user is navigated to ALL PRODUCTS page successfully
6. Enter product name in search input and click search button
7. Verify 'SEARCHED PRODUCTS' is visible
8. Verify all the products related to search are visible
'''

addon_path = os.environ.get("adblock_plus")

def test_product_search(get_driver):
    driver = get_driver
    driver.install_addon(addon_path, temporary=True)
    driver.get(AutomationExercise.base_url)

    assert driver.find_element(By.XPATH, AutomationExerciseLocators.home_icon)

    products_button = driver.find_element(By.XPATH, AutomationExerciseLocators.products_subpage)
    products_button.click()

    assert driver.find_element(By.XPATH, AEProductsLocators.products_verify)

    product_search = driver.find_element(By.XPATH, AEProductsLocators.product_search)
    product_search.send_keys("Winter Top")

    product_search_button = driver.find_element(By.XPATH, AEProductsLocators.product_search_button)
    product_search_button.click()

    assert driver.find_element(By.XPATH, AEProductsLocators.product_search_verify)
    assert "Winter Top" in driver.find_element(By.XPATH, "//div[@class='productinfo text-center']/p").text
