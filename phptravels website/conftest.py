import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

loginenv = os.environ.get("phptravellogin")
passwordenv = os.environ.get("phptravelpass")


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
def get_login(get_driver, get_settings, get_xpaths):
    driver = get_driver
    driver.get(get_settings["base_url"])
    login = driver.find_element(By.XPATH, get_xpaths["login"]["username_input"])
    login.send_keys(loginenv)

    password = driver.find_element(By.XPATH, get_xpaths["login"]["password_input"])
    password.send_keys(passwordenv)

    login_button = driver.find_element(By.XPATH, get_xpaths["login"]["login_button"])
    ActionChains(driver).move_to_element(login_button).click(login_button).perform()
    return driver
