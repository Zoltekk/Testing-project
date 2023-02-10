from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from locators import AELSLocators
from pprint import pprint


class AutomationExercise:
    """The BasePage class holds all common functionality across the website.
    Also provides a nice wrapper when dealing with selenium functions that may
    not be easy to understand.
    """
    base_url = "http://automationexercise.com"

    @staticmethod
    def click(driver, by_locator):
        """ Performs click on web element whose locator is passed to it"""
        driver.find_element(By.XPATH, by_locator).click()

    @staticmethod
    def enter_text(driver, by_locator, text):
        """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        driver.find_element(By.XPATH, by_locator).send_keys(text)

    @staticmethod
    def get_title(driver, title) -> str:
        """Returns the title of the page"""
        WebDriverWait(driver, 10).until(EC.title_is(title))
        return driver.title


class AELoginSignup(AutomationExercise):
    base_url = "https://automationexercise.com/login"

    @staticmethod
    def sign_up(email, name, driver):
        driver.get(AELoginSignup.base_url)
        pprint(AELSLocators.signup_email_form)
        pprint(email)
        AELoginSignup.enter_text(driver, AELSLocators.signup_email_form, email)
        AELoginSignup.enter_text(driver, AELSLocators.signup_name_form, name)
        AELoginSignup.click(driver, AELSLocators.signup_button)

    @staticmethod
    def login(email, password, driver):
        driver.get(AELoginSignup.base_url)
        AELoginSignup.enter_text(driver, AELSLocators.login_email_form, email)
        AELoginSignup.enter_text(driver, AELSLocators.login_pass_form, password)
        AELoginSignup.click(driver, AELSLocators.login_button)
