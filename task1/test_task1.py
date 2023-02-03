from selenium.webdriver.common.by import By


def test_pricecheck(get_xpaths, get_settings, get_driver):
    """
    1. Log into website.
    2. Add 3 random items into the cart.
    3. Proceeds to checkout
    4. Check the sum of the value of the added items against the sum calculated by the website.
    """
    driver = get_driver
    driver.get(get_settings["baseurl"])

    login = driver.find_element(By.XPATH, get_xpaths["login"]["username_input"])
    login.send_keys('standard_user')

    passw = driver.find_element(By.XPATH, get_xpaths["login"]["password_input"])
    passw.send_keys('secret_sauce')

    loginbtn = driver.find_element(By.XPATH, get_xpaths["login"]["login_button"])
    loginbtn.click()

    for i in range(3):
        button = driver.find_element(By.XPATH, get_xpaths["shop"]["add_cart_button"])
        button.click()

    cart = driver.find_element(By.XPATH, get_xpaths["cart"]["go_to_cart_button"])
    cart.click()

    checkout = driver.find_element(By.XPATH, get_xpaths["cart"]["checkout_button"])
    checkout.click()

    input_list = driver.find_elements(By.XPATH, get_xpaths["cart"]["form_input"])

    for il in input_list:
        il.send_keys('abc123')

    cont = driver.find_element(By.XPATH, get_xpaths["cart"]["continue_button"])
    cont.click()

    cart_total = driver.find_elements(By.XPATH, get_xpaths["cart"]["displayed_price"])
    cart_sources = []
    calculated_value = 0

    for c in cart_total:
        cart_sources.append(float(c.text[1:]))

    for p in cart_sources:
        calculated_value += p

    total_web = float(driver.find_element(By.XPATH, get_xpaths["cart"]["item_total"]).text.split('$')[1])

    assert total_web == calculated_value, f"Total value of the items in the cart {calculated_value} does not match " \
                                          f"the value given by the website {total_web}"
    print(f'Total value of items in the cart :{calculated_value}\n'
          f'Total value calculated by the website :{total_web}')