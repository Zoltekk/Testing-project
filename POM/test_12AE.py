from base_pages import AutomationExercise, AECart
from locators import AutomationExerciseLocators, AEProductsLocators, AECartLocators
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

'''
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Products' button
5. Hover over first product and click 'Add to cart'
6. Click 'Continue Shopping' button
7. Hover over second product and click 'Add to cart'
8. Click 'View Cart' button
9. Verify both products are added to Cart
10. Verify their prices, quantity and total price
'''

addon_path = os.environ.get("adblock_plus")

def test_cart_total(get_driver):
    driver = get_driver
    driver.install_addon(addon_path, temporary=True)
    driver.get(AutomationExercise.base_url)

    assert driver.find_element(By.XPATH, AutomationExerciseLocators.home_icon), "Home page not loaded"

    products_button = driver.find_element(By.XPATH, AutomationExerciseLocators.products_subpage)
    products_button.click()

    product_1 = driver.find_element(By.XPATH, AEProductsLocators.product_bluetop_1)
    product_1.click()

    continue_button = driver.find_element(By.XPATH, AEProductsLocators.continue_button)
    continue_button.click()

    product_2 = driver.find_element(By.XPATH, AEProductsLocators.product_mentshirt_1)
    product_2.click()

    view_cart = driver.find_element(By.XPATH, AEProductsLocators.view_cart)
    view_cart.click()

    assert "Blue Top" in driver.find_element(By.XPATH, AECartLocators.cart_item_1).text, "'Blue Top' not present in cart"
    assert "Men Tshirt" in driver.find_element(By.XPATH, AECartLocators.cart_item_2).text, "'Men Tshirt' not present in cart"

    AECart.cart_verify_price(AECartLocators.item_1_price, AECartLocators.item_1_quantity, AECartLocators.item_1_total, driver)
    AECart.cart_verify_price(AECartLocators.item_2_price, AECartLocators.item_2_quantity, AECartLocators.item_2_total, driver)