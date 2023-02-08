from selenium.webdriver.common.by import By


'''
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'Login to your account' is visible
6. Enter incorrect email address and password
7. Click 'login' button
8. Verify error 'Your email or password is incorrect!' is visible
'''


def test_login_failure(get_driver, get_settings, get_xpaths):

    driver = get_driver
    driver.get(get_settings["base_url"])

    assert driver.find_element(By.XPATH, get_xpaths["home"]["home_button"])
    login_button = driver.find_element(By.XPATH, get_xpaths["login"]["login_subpage"])
    login_button.click()

    assert driver.find_element(By.XPATH, get_xpaths["login"]["login_form"])
    login_email = driver.find_element(By.XPATH, get_xpaths["login"]["login_email"])
    login_email.send_keys(get_settings["inc_email"])

    login_password = driver.find_element(By.XPATH, get_xpaths["login"]["login_password"])
    login_password.send_keys(get_settings["inc_password"])

    login_button = driver.find_element(By.XPATH, get_xpaths["login"]["login_button"])
    login_button.click()

    assert driver.find_element(By.XPATH, get_xpaths["login"]["inc_credentials"])
