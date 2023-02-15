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
6. The products list is visible
7. Click on 'View Product' of first product
8. User is landed to product detail page
9. Verify that detail detail is visible: product name, category, price, availability, condition, brand
'''

addon_path = os.environ.get("adblock_plus")

def test_product_list(get_driver):
    driver = get_driver
    driver.install_addon(addon_path, temporary=True)
    driver.get(AutomationExercise.base_url)

    assert driver.find_element(By.XPATH, AutomationExerciseLocators.home_icon)

    products_button = driver.find_element(By.XPATH, AutomationExerciseLocators.products_subpage)
    products_button.click()

    assert driver.find_element(By.XPATH, AEProductsLocators.products_verify)
    assert driver.find_element(By.XPATH, AEProductsLocators.products_list)

    product_view_1_button = driver.find_element(By.XPATH, AEProductsLocators.product_view_1)
    product_view_1_button.click()

    assert "product_details" in driver.current_url

    product_verify_list = [AEProductsLocators.product_name, AEProductsLocators.product_category, AEProductsLocators.product_price,
                           AEProductsLocators.product_availability, AEProductsLocators.product_condition, AEProductsLocators.product_brand]
    for item in product_verify_list:
        assert driver.find_element(By.XPATH, item)
