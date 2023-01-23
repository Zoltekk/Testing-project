import pytest
import json
from selenium import webdriver

@pytest.fixture()
def get_driver(get_settings):
    driver = webdriver.Firefox()
    driver.implicitly_wait(get_settings["settings"]["implicit_wait_duration"])
    return driver

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