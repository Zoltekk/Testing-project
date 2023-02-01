from selenium.webdriver.common.by import By
import pytest

# 1. Login with all combinations of credentials (correct,incorrect,empty,illegal character, too long/short)

@pytest.mark.parametrize("username,passwd,expected_result", [
    ("standard_user", "secret_sauce", "correct"),
    ("locked_out_user", "secret_sauce", "locked_out"),
    ("problem_user", "secret_sauce", "problem"),
    ("performance_glitch_user", "secret_sauce", "slow"),
    ("wrong_username", "secret_sauce", "incorrect"),
    ("standard_user", "wrong_password", "incorrect"),
    ("$%\"$&$", "£%^*\"£%\"^*", "incorrect"),
    ("", "", "incorrect"),
    ("a"*900, "a"*900, "incorrect")
])


def test_login_correct(get_settings, get_driver, get_xpaths, username, passwd, expected_result):
    driver = get_driver
    driver.get(get_settings["base_url"])

    login = driver.find_element(By.XPATH, get_xpaths["login"]["username_input"])
    password = driver.find_element(By.XPATH, get_xpaths["login"]["password_input"])
    login_button = driver.find_element(By.XPATH, get_xpaths["login"]["login_button"])

    login.send_keys(username)
    password.send_keys(passwd)
    login_button.click()

    if expected_result == "correct" or expected_result == "slow":
        print(f"current url: {driver.current_url}")
        assert "/inventory.html" in driver.current_url # Main page url

    elif expected_result == "incorrect" or expected_result == "locked_out":
        item = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert "Epic sadface" in item # Error message shown

    elif expected_result == "problem":
        pics = driver.find_elements(By.XPATH, "//img[@class='inventory_item_img']")
        urls = [e.get_attribute('src') for e in pics]
        assert len(set(urls)) == 1 # Known bug
    else:
        raise("Case not covered!")
