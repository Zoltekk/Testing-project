import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture()
def get_driver(get_settings):
    driver = webdriver.Firefox()
    driver.implicitly_wait(get_settings["wait_duration"])
    yield driver
    driver.quit()


@pytest.fixture()
def get_settings():
    with open("config.json") as f:
        data = json.load(f)
    return data["settings"]

@pytest.fixture()
def get_xpaths():
    with open("config.json") as f:
        data = json.load(f)
    return data["xpaths"]


@pytest.fixture()
def get_signup(get_xpaths, get_driver, get_settings):
    driver = get_driver
    driver.get(get_settings["base_url"])

    assert driver.find_element(By.XPATH, get_xpaths["home"]["home_button"])
    login_button = driver.find_element(By.XPATH, get_xpaths["login"]["login_subpage"])
    login_button.click()

    assert driver.find_element(By.XPATH, "//div[@class='signup-form']")
    signup_name = driver.find_element(By.XPATH, "//input[@data-qa='signup-name']")
    signup_name.send_keys("John Smith")

    signup_email = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
    signup_email.send_keys(get_settings["email"])

    signup_button = driver.find_element(By.XPATH, "//button[@data-qa='signup-button']")
    signup_button.click()

    assert driver.find_element(By.XPATH, "//*[contains(text(), 'Enter Account Information')]")
    title = "//input[@id='id_gender1']"
    days = "//select[@id='days']/option[@value='1']"
    months = "//select[@id='months']/option[@value='1']"
    years = "//select[@id='years']/option[@value='2000']"
    newsletter = "//input[@id='newsletter']"
    optin = "//input[@id='optin']"

    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys(get_settings["password"])

    signup_list = [title, days, months, years, newsletter, optin]
    for option in signup_list:
        option_v = driver.find_element(By.XPATH, option)
        option_v.click()

    firstname = "//input[@id='first_name']"
    lastname = "//input[@id='last_name']"
    company = "//input[@id='company']"
    address1 = "//input[@id='address1']"
    address2 = "//input[@id='address2']"
    state = "//input[@id='state']"
    city = "//input[@id='city']"
    zipcode = "//input[@id='zipcode']"
    mobile = "//input[@id='mobile_number']"

    time.sleep(1)
    close_ad = driver.find_element(By.XPATH, "//div[@class='grippy-host']")
    close_ad.click()
    time.sleep(2)
    country = driver.find_element(By.XPATH, "//select[@id='country']/option[@value='United States']")
    country.click()

    signup_list2 = {firstname: "John", lastname: "Smith", company: "The Smith Company", address1: "123 Some Street",
                    address2: "Some District", state: "Michigan", city: "Detroit", zipcode: "48126",
                    mobile: "(555) 555-1234"}
    for key, value in signup_list2.items():
        input_box = driver.find_element(By.XPATH, key)
        input_box.send_keys(value)

    create_account = driver.find_element(By.XPATH, "//button[@data-qa='create-account']")
    create_account.click()

    assert driver.find_element(By.XPATH, "//h2[@class='title text-center']")
    continue_button = driver.find_element(By.XPATH, "//a[@class='btn btn-primary']")
    continue_button.click()
    return driver


@pytest.fixture()
def get_logout(get_driver, get_settings, get_xpaths):
    driver = get_driver
    driver.get(get_settings["base_url"])

    assert driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]")
    logout = driver.find_element(By.XPATH, get_xpaths["login"]["logout"])
    logout.click()
    return driver


@pytest.fixture()
def get_login(get_driver, get_settings, get_xpaths):
    driver = get_driver
    driver.get(get_settings["base_url"])

    assert driver.find_element(By.XPATH, get_xpaths["home"]["home_button"])
    login_button = driver.find_element(By.XPATH, get_xpaths["login"]["login_subpage"])
    login_button.click()

    assert driver.find_element(By.XPATH, get_xpaths["login"]["login_form"])
    login_email = driver.find_element(By.XPATH, get_xpaths["login"]["login_email"])
    login_email.send_keys(get_settings["email"])

    login_password = driver.find_element(By.XPATH, get_xpaths["login"]["login_password"])
    login_password.send_keys(get_settings["password"])

    login_button = driver.find_element(By.XPATH, get_xpaths["login"]["login_button"])
    login_button.click()
    return driver


@pytest.fixture()
def get_delete(get_settings, get_driver):
    driver = get_driver
    driver.get(get_settings["base_url"])

    assert driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]")
    delete_account = driver.find_element(By.XPATH, "//a[@href='/delete_account']")
    delete_account.click()

    assert driver.find_element(By.XPATH, "//h2[@class='title text-center']")
    continue_button2 = driver.find_element(By.XPATH, "//a[@class='btn btn-primary']")
    continue_button2.click()
    return driver
