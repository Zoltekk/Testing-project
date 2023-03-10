class AutomationExerciseLocators:
    home_icon = "//i[@class='fa fa-home']"
    login_subpage = "//a[@href='/login']"
    contact_button = "//a[@href='/contact_us']"
    test_cases_button = "//a[contains(text(), 'Test Cases')]"
    test_cases_verify = "//b[contains(text(), 'Test Cases')]"
    products_subpage = "//a[@href='/products']"
    subscribe_verify = "//div[@class='single-widget']/h2"
    subscribe_input = "//input[@id='susbscribe_email']"
    subscribe_button = "//button[@id='subscribe']"
    subscribe_success = "//div[@class='alert-success alert']"
    cart_button = "//a[@href='/products']/following::a[1]"

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


class AEProductsLocators(AutomationExerciseLocators):
    products_verify = "//h2[@class='title text-center']"
    products_list = "//div[@class='features_items']"
    product_view_1 = "//a[@href='/product_details/1']"
    product_name = "//div[@class='product-information']/h2"
    product_category = "//div[@class='product-information']/p"
    product_price = "//div[@class='product-information']/span/span"
    product_availability = "//*[contains(text(), 'Availability')]"
    product_condition = "//*[contains(text(), 'Condition')]"
    product_brand = "//b[contains(text(), 'Brand')]"
    product_search = "//input[@id='search_product']"
    product_search_button = "//button[@id='submit_search']"
    product_search_verify = "//h2[@class='title text-center']"
    product_bluetop_1 = "//section[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a"
    product_mentshirt_1 = "//section[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/a"
    products_search_verify_2 = "//div[@class='productinfo text-center']/p"
    continue_button = "//button[@class='btn btn-success close-modal btn-block']"
    view_cart = "//u"


class AECartLocators(AutomationExerciseLocators):
    cart_item_1 = "//a[@href='/product_details/1']"
    cart_item_2 = "//a[@href='/product_details/2']"
    item_1_price = "//tr[@id='product-1']/td[@class='cart_price']//p"
    item_2_price = "//tr[@id='product-2']/td[@class='cart_price']//p"
    item_1_quantity = "//tr[@id='product-1']//button[@class='disabled']"
    item_2_quantity = "//tr[@id='product-2']//button[@class='disabled']"
    item_1_total = "//tr[@id='product-1']//p[@class='cart_total_price']"
    item_2_total = "//tr[@id='product-2']//p[@class='cart_total_price']"
