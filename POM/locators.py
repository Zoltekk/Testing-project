class AutomationExerciseLocators:
    home_icon = "//i[@class='fa fa-home']"
    login_subpage = "//a[@href='/login']"
    contact_button = "//a[@href='/contact_us']"


class AELSLocators(AutomationExerciseLocators):
    login_email_form = "//input[@data-qa='login-email']"
    login_pass_form = "//input[@data-qa='login-password']"
    login_button = "//button[@data-qa='login-button']"
    signup_form = "//div[@class='signup-form']"
    signup_email_form = "//input[@data-qa='signup-email']"
    signup_name_form = "//input[@data-qa='signup-name']"
    signup_button = "//button[@data-qa='signup-button']"
    signup_verify = "//*[contains(text(), 'Email Address already exist!')]"


class AEContactLocators(AutomationExerciseLocators):
    contact_verify = "//*[contains(text(), 'Get In Touch')]"
    contact_name = "//input[@name='name']"
    contact_email = "//input[@name='email']"
    contact_subject = "//input[@name='subject']"
    contact_message = "//textarea[@id='message']"
    contact_upload = "//input[@name='upload_file']"
    contact_submit = "//input[@type='submit']"
    contact_success = "//div[contains(text(), 'Success! Your details have been submitted successfully.')]"
    contact_home = "//a[@class='btn btn-success']"