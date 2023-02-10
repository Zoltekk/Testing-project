from selenium.webdriver.common.by import By


class AutomationExerciseLocators:
    home_icon = "//i[@class='fa fa-home']"
    login_subpage = "//a[@href='/login']"


class AELSLocators(AutomationExerciseLocators):
    login_email_form = "//input[@data-qa='login-email']"
    login_pass_form = "//input[@data-qa='login-password']"
    login_button = "//button[@data-qa='login-button']"
    signup_form = "//div[@class='signup-form']"
    signup_email_form = "//input[@data-qa='signup-email']"
    signup_name_form = "//input[@data-qa='signup-name']"
    signup_button = "//button[@data-qa='signup-button']"
    signup_verify = "//*[contains(text(), 'Email Address already exist!')]"
