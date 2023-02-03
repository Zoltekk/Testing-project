import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture()
def get_driver(get_settings):
    driver = webdriver.Firefox()
    driver.implicitly_wait(get_settings["wait_duration"])
    return driver
    # yield driver
    # driver.quit()


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

    assert WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, get_xpaths["home"]["home_button"])))
    login_button = driver.find_element(By.XPATH, get_xpaths["login"]["login_subpage"])
    login_button.click()

    assert WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='signup-form']")))
    signup_name = driver.find_element(By.XPATH, "//input[@data-qa='signup-name']")
    signup_email = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
    signup_button = driver.find_element(By.XPATH, "//button[@data-qa='signup-button']")

    signup_name.send_keys("John Smith")
    signup_email.send_keys(get_settings["email"])
    signup_button.click()

    assert WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Enter Account "
                                                  "Information')]")))
    title = driver.find_element(By.XPATH, "//input[@id='id_gender1']")
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    days = driver.find_element(By.XPATH, "//select[@id='days']/option[@value='1']")
    months = driver.find_element(By.XPATH, "//select[@id='months']/option[@value='1']")
    years = driver.find_element(By.XPATH, "//select[@id='years']/option[@value='2000']")
    newsletter = driver.find_element(By.XPATH, "//input[@id='newsletter']")
    optin = driver.find_element(By.XPATH, "//input[@id='optin']")

    password.send_keys(get_settings["password"])

    signup_list = [title, days, months, years, newsletter, optin]
    for option in signup_list:
        option.click()

    firstname = driver.find_element(By.XPATH, "//input[@id='first_name']")
    lastname = driver.find_element(By.XPATH, "//input[@id='last_name']")
    company = driver.find_element(By.XPATH, "//input[@id='company']")
    address1 = driver.find_element(By.XPATH, "//input[@id='address1']")
    address2 = driver.find_element(By.XPATH, "//input[@id='address2']")
    close_ad = driver.find_element(By.XPATH, "//div[@class='grippy-host']")
    country = driver.find_element(By.XPATH, "//select[@id='country']/option[@value='United States']")
    state = driver.find_element(By.XPATH, "//input[@id='state']")
    city = driver.find_element(By.XPATH, "//input[@id='city']")
    zipcode = driver.find_element(By.XPATH, "//input[@id='zipcode']")
    mobile = driver.find_element(By.XPATH, "//input[@id='mobile_number']")
    create_account = driver.find_element(By.XPATH, "//button[@data-qa='create-account']")

    time.sleep(1)
    close_ad.click()
    time.sleep(2)
    country.click()

    signup_list2 = {firstname: "John", lastname: "Smith", company: "The Smith Company", address1: "123 Some Street",
                    address2: "Some District", state: "Michigan", city: "Detroit", zipcode: "48126",
                    mobile: "(555) 555-1234"}
    for key, value in signup_list2.items():
        key.send_keys(value)

    create_account.click()

    assert WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//h2[@class='title text-center']")))
    continue_button = driver.find_element(By.XPATH, "//a[@class='btn btn-primary']")
    continue_button.click()
    return driver


@pytest.fixture()
def get_logout(get_driver, get_settings, get_xpaths):
    driver = get_driver
    driver.get(get_settings["base_url"])

    assert WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]")))
    logout = driver.find_element(By.XPATH, get_xpaths["login"]["logout"])
    logout.click()
    return driver


@pytest.fixture()
def get_login(get_driver, get_settings, get_xpaths):
    driver = get_driver
    driver.get(get_settings["base_url"])

    assert WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, get_xpaths["home"]["home_button"])))
    login_button = driver.find_element(By.XPATH, get_xpaths["login"]["login_subpage"])
    login_button.click()

    assert WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, get_xpaths["login"]["login_form"])))
    login_email = driver.find_element(By.XPATH, get_xpaths["login"]["login_email"])
    login_password = driver.find_element(By.XPATH, get_xpaths["login"]["login_password"])
    login_button = driver.find_element(By.XPATH, get_xpaths["login"]["login_button"])

    login_email.send_keys(get_settings["email"])
    login_password.send_keys(get_settings["password"])
    login_button.click()
    return driver


@pytest.fixture()
def get_delete(get_settings, get_driver):
    driver = get_driver
    driver.get(get_settings["base_url"])

    assert WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]")))
    delete_account = driver.find_element(By.XPATH, "//a[@href='/delete_account']")
    delete_account.click()

    assert WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h2[@class='title text-center']")))
    continue_button2 = driver.find_element(By.XPATH, "//a[@class='btn btn-primary']")
    continue_button2.click()
    return driver
