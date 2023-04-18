from base_pages import AutomationExercise, AELoginSignup, AECart
from locators import AutomationExerciseLocators, AEProductsLocators, AECartLocators
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

addon_path = os.environ.get("adblock_plus")

test_email = os.environ.get("test_email")
test_password = os.environ.get("test_password")
test_name = os.environ.get("test_name")
test_first_name = os.environ.get("test_first_name")
test_last_name = os.environ.get("test_last_name")
test_company = os.environ.get("test_company")
test_address1 = os.environ.get("test_address1")
test_address2 = os.environ.get("test_address2")
test_state = os.environ.get("test_state")
test_city = os.environ.get("test_city")
test_zipcode = os.environ.get("test_zipcode")
test_mobile = os.environ.get("test_mobile")

card_number = os.environ.get("card_number")
card_cvc = os.environ.get("card_cvc")
card_month = os.environ.get("card_month")
card_year = os.environ.get("card_year")

'''
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Add products to cart
5. Click 'Cart' button
6. Verify that cart page is displayed
7. Click Proceed To Checkout
8. Click 'Register / Login' button
9. Fill all details in Signup and create account
10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
11. Verify ' Logged in as username' at top
12.Click 'Cart' button
13. Click 'Proceed To Checkout' button
14. Verify Address Details and Review Your Order
15. Enter description in comment text area and click 'Place Order'
16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
17. Click 'Pay and Confirm Order' button
18. Verify success message 'Your order has been placed successfully!'
19. Click 'Delete Account' button
20. Verify 'ACCOUNT DELETED!' and click 'Continue' button
'''


def test_register_cart(get_driver):
    driver = get_driver
    driver.install_addon(addon_path, temporary=True)
    driver.get(AutomationExercise.base_url)

    assert driver.find_element(By.XPATH, AutomationExerciseLocators.home_icon), "Home page not loaded"

    product_name = driver.find_element(By.XPATH, AutomationExerciseLocators.product_name_verify).text
    AutomationExercise.click(driver, AutomationExerciseLocators.add_to_cart_button)

    AutomationExercise.click(driver, AEProductsLocators.product_view_cart_center)

    assert "view_cart" in driver.current_url, "Couldn't navigate to cart page"

    AutomationExercise.click(driver, AECartLocators.checkout_button)

    AutomationExercise.click(driver, AECartLocators.register_login_button)

    AELoginSignup.sign_up(test_email, test_name, driver)

    AELoginSignup.sign_up_complete(test_password, test_first_name, test_last_name, test_company, test_address1,
                                   test_address2, test_state, test_city, test_zipcode, test_mobile, driver)

    assert driver.find_element(By.XPATH, AutomationExerciseLocators.logged_in), "User not logged in"

    AutomationExercise.click(driver, AutomationExerciseLocators.cart_button)

    AutomationExercise.click(driver, AECartLocators.checkout_button)

    assert test_name in driver.find_element(By.XPATH, AECartLocators.delivery_verify).text, "Name doesn't match"
    assert product_name in driver.find_element(By.XPATH, AECartLocators.cart_item_1).text, "Product doesn't match"

    AutomationExercise.enter_text(driver, AECartLocators.order_description, "I like it")
    AutomationExercise.click(driver, AECartLocators.place_order_button)

    AECart.card_info(test_name, card_number, card_cvc, card_month, card_year, driver)

    assert driver.find_element(By.XPATH, AECartLocators.purchase_verify), "Message not showing"

    AutomationExercise.click(driver, AutomationExerciseLocators.delete_account)

    assert driver.find_element(By.XPATH, AutomationExerciseLocators.delete_verify), "Message not showing"

    AutomationExercise.click(driver, AutomationExerciseLocators.delete_continue)
