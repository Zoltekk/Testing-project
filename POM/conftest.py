import pytest
from selenium import webdriver


@pytest.fixture
def get_driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    driver.close()


def install_addon(self, path, temporary=None):
    payload = {"path": path}
    if temporary:
        payload["temporary"] = temporary
    return self.execute("INSTALL_ADDON", payload)["value"]