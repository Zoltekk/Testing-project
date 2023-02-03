import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# 1. Log in
# 2. Navigate to "Hotels" subpage
# 3. Test different boundary values in the search element


def room_fillout(driver, get_xpaths, options):
    room_choice = driver.find_element(By.XPATH, get_xpaths["subpages"]["room_choice"])
    room_choice.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, get_xpaths["subpages"]["room_inc"])))

    for key, value in options.items():
        room_elem = driver.find_element(By.XPATH, get_xpaths["subpages"]["room_elem"] % (key))

        room_elem.clear()
        room_elem.send_keys(options[key])


@pytest.mark.parametrize("rooms", [-1, "abc", 0, 2, 20])
@pytest.mark.parametrize("adults", [-1, "abc", 0, 2, 5000])
@pytest.mark.parametrize("childs", [-1, "abc", 2, 5000])
def test_boundary(get_login, get_settings, get_xpaths, rooms, adults, childs):

    driver = get_login

    hotels_sub = driver.find_element(By.XPATH, get_xpaths["subpages"]["hotels_sub"])
    hotels_sub.click()

    city_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, get_xpaths["subpages"]["city_box"])))
    ActionChains(driver).move_to_element(city_box).click(city_box).send_keys("Lon").perform()

    time.sleep(3)
    city_choice = driver.find_element(By.XPATH, get_xpaths["subpages"]["city_choice"])
    ActionChains(driver).move_to_element(city_choice).send_keys(Keys.RETURN).perform()

    options = {"rooms": rooms, "adults": adults, "childs": childs}
    room_fillout(driver, get_xpaths, options)

    submit_button = driver.find_element(By.XPATH, get_xpaths["subpages"]["submit_button"])
    submit_button.click()

    for key, value in options.items():
        if value <= 0:
            assert "usd" not in driver.current_url, f"Value is zero or negative, {key} is {value}"  # Checking for incorrect inputs and asserting the URL of the proceeding subpage
        elif rooms > 10:
            assert "usd" not in driver.current_url, f"Too many rooms, rooms : {rooms}"
        elif adults+childs < rooms:
            assert "usd" not in driver.current_url, f"Too few guests, adults :{adults}, children :{childs}"
        elif value != int(value):
            assert "usd" not in driver.current_url, f"Value is not an integer, value : {value}"
        else:                                                                                       # Checking for correct inputs and asserting the URL of the proceeding subpage
            assert "usd" in driver.current_url, f"Website didn't proceed, rooms:{rooms}, adults:{adults}, children{childs}"
