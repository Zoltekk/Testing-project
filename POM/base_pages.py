from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from locators import AELSLocators, AEContactLocators, AutomationExerciseLocators, AECartLocators
import os
from dotenv import load_dotenv, find_dotenv
import re

load_dotenv(find_dotenv())

email = os.environ.get("email")

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
        AELoginSignup.enter_text(driver, AELSLocators.signup_email_form, email)
        AELoginSignup.enter_text(driver, AELSLocators.signup_name_form, name)
        AELoginSignup.click(driver, AELSLocators.signup_button)

    @staticmethod
    def login(email, password, driver):
        driver.get(AELoginSignup.base_url)
        AELoginSignup.enter_text(driver, AELSLocators.login_email_form, email)
        AELoginSignup.enter_text(driver, AELSLocators.login_pass_form, password)
        AELoginSignup.click(driver, AELSLocators.login_button)


class AEContactUs(AutomationExercise):

    @staticmethod
    def fill_out(name, email, subject, message, driver):
        AEContactUs.enter_text(driver, AEContactLocators.contact_name, name)
        AEContactUs.enter_text(driver, AEContactLocators.contact_email, email)
        AEContactUs.enter_text(driver, AEContactLocators.contact_subject, subject)
        AEContactUs.enter_text(driver, AEContactLocators.contact_message, message)

    @staticmethod
    def upload_and_submit(path, driver):
        AEContactUs.enter_text(driver, AEContactLocators.contact_upload, path)
        AEContactUs.click(driver, AEContactLocators.contact_submit)


class AESubscribe(AutomationExercise):

    @staticmethod
    def subscribe_fill_out(driver):
        AESubscribe.enter_text(driver, AutomationExerciseLocators.subscribe_input, email)

    @staticmethod
    def subscribe_click(driver):
        AESubscribe.click(driver, AutomationExerciseLocators.subscribe_button)


class AECart(AutomationExercise):

    @staticmethod
    def cart_verify_price(price_locator, quantity_locator, total_locator, driver):
        cart_num_regex = re.compile(r'\d+')

        price = cart_num_regex.findall(driver.find_element(By.XPATH, price_locator).text)
        quantity = cart_num_regex.findall(driver.find_element(By.XPATH, quantity_locator).text)
        total = cart_num_regex.findall(driver.find_element(By.XPATH, total_locator).text)

        assert int(price[0]) * int(quantity[0]) == int(total[0])
