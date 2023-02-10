from selenium.webdriver.common.by import By

'''
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'Login to your account' is visible
6. Enter correct email address and password
7. Click 'login' button
8. Verify that 'Logged in as username' is visible
9. Click 'Logout' button
10. Verify that user is navigated to login page
'''


def test_logout(get_driver, get_settings, get_xpaths, get_login, get_logout):

    driver = get_logout
    assert driver.find_element(By.XPATH, get_xpaths["login"]["login_form"])
