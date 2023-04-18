from base_pages import AutomationExercise
from locators import AutomationExerciseLocators, AEProductsLocators, AECartLocators
import random
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

'''
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'View Product' for any product on home page
5. Verify product detail is opened
6. Increase quantity to 4
7. Click 'Add to cart' button
8. Click 'View Cart' button
9. Verify that product is displayed in cart page with exact quantity
'''

addon_path = os.environ.get("adblock_plus")


def test_product_quantity(get_driver):
    driver = get_driver
    driver.install_addon(addon_path, temporary=True)
    driver.get(AutomationExercise.base_url)

    assert driver.find_element(By.XPATH, AutomationExerciseLocators.home_icon), "Home page not loaded"

    AutomationExercise.click(driver, AutomationExerciseLocators.view_product_blue_top)

    assert "product_details/1" in driver.current_url, "Couldn't navigate to the product page"

    random_quantity = random.randint(3, 7)
    AutomationExercise.enter_text(driver, AEProductsLocators.product_quantity, str(random_quantity))

    AutomationExercise.click(driver, AEProductsLocators.product_add_to_cart)

    AutomationExercise.click(driver, AEProductsLocators.product_view_cart_center)

    cart_quantity = driver.find_element(By.XPATH, AECartLocators.item_1_quantity)

    assert cart_quantity.text == str(random_quantity), f"Cart quantity does not match input," \
                                                  f"input = {random_quantity}" \
                                                  f"quantity = {cart_quantity.text}"