import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import time
# from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def get_driver(get_settings):
    driver = webdriver.Firefox()
    driver.implicitly_wait(get_settings["implicit_wait_duration"])
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
def get_cred():
    with open("config.json") as f:
        data = json.load(f)
    return data["credentials"]


@pytest.fixture()
def get_login(get_driver, get_settings, get_xpaths, get_cred):
    driver = get_driver
    driver.get(get_settings["base_url"])
    login = driver.find_element(By.XPATH, get_xpaths["login"]["username_input"])
    login.send_keys(get_cred["login"])

    password = driver.find_element(By.XPATH, get_xpaths["login"]["password_input"])
    password.send_keys(get_cred["password"])

    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, get_xpaths["login"]["login_button"])))
    ActionChains(driver).move_to_element(login_button).click(login_button).perform()
    return driver


# @pytest.fixture()
# def get_city(get_driver, get_xpaths):
#     driver = get_driver
#     city_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, get_xpaths["subpages"]["city_box"])))
#     ActionChains(driver).move_to_element(city_box).click(city_box).send_keys("Lon").perform()
#
#     time.sleep(3)
#     city_choice = driver.find_element(By.XPATH, get_xpaths["subpages"]["city_choice"])
#     ActionChains(driver).move_to_element(city_choice).send_keys(Keys.RETURN).perform()
#     return driver
