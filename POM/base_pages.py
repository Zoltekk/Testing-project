from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from locators import AELSLocators, AEContactLocators, AutomationExerciseLocators, AESignup, AECartLocators
import time
import re


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
        driver.find_element(By.XPATH, by_locator).clear()
        driver.find_element(By.XPATH, by_locator).send_keys(text)

    @staticmethod
    def get_title(driver, title) -> str:
        """Returns the title of the page"""
        WebDriverWait(driver, 10).until(EC.title_is(title))
        return driver.title


class AELoginSignup(AutomationExercise):

    @staticmethod
    def sign_up(email, name, driver):
        AELoginSignup.enter_text(driver, AELSLocators.signup_email_form, email)
        AELoginSignup.enter_text(driver, AELSLocators.signup_name_form, name)
        AELoginSignup.click(driver, AELSLocators.signup_button)

    @staticmethod
    def sign_up_complete(password, firstname, lastname, company, address1, address2, state, city, zipcode, mobile, driver):
        assert driver.find_element(By.XPATH, AESignup.signup2_verify)

        AELoginSignup.enter_text(driver, AESignup.signup2_password, password)

        signup_list = [AESignup.signup2_title, AESignup.signup2_days, AESignup.signup2_months, AESignup.signup2_years,
                       AESignup.signup2_newsletter, AESignup.signup2_optin]
        for option in signup_list:
            AELoginSignup.click(driver, option)

        # time.sleep(1)
        # AELoginSignup.click(driver, AESignup.signup2_close_ad)
        # time.sleep(2)
        AELoginSignup.click(driver, AESignup.signup2_country)

        signup_list2 = {AESignup.signup2_firstname: firstname, AESignup.signup2_lastname: lastname,
                        AESignup.signup2_company: company, AESignup.signup2_address1: address1,
                        AESignup.signup2_address2: address2, AESignup.signup2_state: state,
                        AESignup.signup2_city: city, AESignup.signup2_zipcode: zipcode, AESignup.signup2_mobile: mobile}
        for key, value in signup_list2.items():
            AELoginSignup.enter_text(driver, key, value)

        AELoginSignup.click(driver, AESignup.signup2_create_account)

        assert driver.find_element(By.XPATH, AESignup.signup2_verify2)
        AELoginSignup.click(driver, AESignup.signup2_continue_button)

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

        assert float(price[0]) * float(quantity[0]) == float(total[0]), f"Total price does not match input values. " \
                                                                  f"Price:{price}, Quantity:{quantity}, Total:{total}"


    @staticmethod
    def card_info(name, number, cvc, month, year, driver):
        AECart.enter_text(driver, AECartLocators.card_name, name)
        AECart.enter_text(driver, AECartLocators.card_number, number)
        AECart.enter_text(driver, AECartLocators.card_cvc, cvc)
        AECart.enter_text(driver, AECartLocators.card_month, month)
        AECart.enter_text(driver, AECartLocators.card_year, year)
        AECart.click(driver, AECartLocators.pay_button)
