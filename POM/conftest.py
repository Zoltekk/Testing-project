import pytest
from selenium import webdriver


@pytest.fixture
def get_driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    driver.close()


