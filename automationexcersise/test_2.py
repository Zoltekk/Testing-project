'''
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'Login to your account' is visible
6. Enter correct email address and password
7. Click 'login' button
8. Verify that 'Logged in as username' is visible
9. Click 'Delete Account' button
10. Verify that 'ACCOUNT DELETED!' is visible
'''


def test_login_success(get_settings, get_driver, get_xpaths, get_signup, get_logout, get_login, get_delete):
    driver = get_driver
    driver.get(get_settings["base_url"])

    driver = get_signup

    driver = get_logout

    driver = get_login

    driver = get_delete
