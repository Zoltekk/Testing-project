import pytest
import json
from selenium import webdriver

@pytest.fixture()
def get_driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
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