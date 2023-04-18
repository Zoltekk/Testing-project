import pytest
from selenium import webdriver


@pytest.fixture
def get_driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def install_addon(driver, path, temporary=None):
    payload = {"path": path}
    if temporary:
        payload["temporary"] = temporary
    return driver.execute("INSTALL_ADDON", payload)["value"]