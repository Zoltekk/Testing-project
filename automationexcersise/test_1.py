from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''
Registering a user
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'New User Signup!' is visible
6. Enter name and email address
7. Click 'Signup' button
8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
9. Fill details: Title, Name, Email, Password, Date of birth
10. Select checkbox 'Sign up for our newsletter!'
11. Select checkbox 'Receive special offers from our partners!'
12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
13. Click 'Create Account button'
14. Verify that 'ACCOUNT CREATED!' is visible
15. Click 'Continue' button
16. Verify that 'Logged in as username' is visible
17. Click 'Delete Account' button
18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
'''


def test_register(get_driver, get_settings, get_xpaths):
    driver = get_driver
    driver.get(get_settings["base_url"])

    assert WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-home']")))
    login_button = driver.find_element(By.XPATH, (get_xpaths["login"]["login_subpage"]))
    login_button.click()

    assert WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='signup-form']")))
    signup_name = driver.find_element(By.XPATH, "//input[@data-qa='signup-name']")
    signup_email = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
    signup_button = driver.find_element(By.XPATH, "//button[@data-qa='signup-button']")

    signup_name.send_keys("John Smith")
    signup_email.send_keys(get_settings["email"])
    signup_button.click()

    assert WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Enter Account "
                                                                             "Information')]")))
    title = driver.find_element(By.XPATH, "//input[@id='id_gender1']")
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    days = driver.find_element(By.XPATH, "//select[@id='days']/option[@value='1']")
    months= driver.find_element(By.XPATH, "//select[@id='months']/option[@value='1']")
    years = driver.find_element(By.XPATH, "//select[@id='years']/option[@value='2000']")
    newsletter = driver.find_element(By.XPATH, "//input[@id='newsletter']")
    optin = driver.find_element(By.XPATH, "//input[@id='optin']")

    title.click()
    password.send_keys(get_settings["password"])
    days.click()
    months.click()
    years.click()
    newsletter.click()
    optin.click()

    firstname = driver.find_element(By.XPATH, "//input[@id='first_name']")
    lastname = driver.find_element(By.XPATH, "//input[@id='last_name']")
    company = driver.find_element(By.XPATH, "//input[@id='company']")
    address1 = driver.find_element(By.XPATH, "//input[@id='address1']")
    address2 = driver.find_element(By.XPATH, "//input[@id='address2']")
    close_ad = driver.find_element(By.XPATH, "//div[@class='grippy-host']")
    country = driver.find_element(By.XPATH, "//select[@id='country']/option[@value='United States']")
    state = driver.find_element(By.XPATH, "//input[@id='state']")
    city = driver.find_element(By.XPATH, "//input[@id='city']")
    zipcode = driver.find_element(By.XPATH, "//input[@id='zipcode']")
    mobile = driver.find_element(By.XPATH, "//input[@id='mobile_number']")
    create_account = driver.find_element(By.XPATH, "//button[@data-qa='create-account']")

    firstname.send_keys("John")
    lastname.send_keys("Smith")
    company.send_keys("The Smith Company")
    address1.send_keys("123 Some Street")
    address2.send_keys("Some District")
    close_ad.click()
    time.sleep(2)
    country.click()
    state.send_keys("Michigan")
    city.send_keys("Detroit")
    zipcode.send_keys("48126")
    mobile.send_keys("(555) 555-1234")
    create_account.click()

    assert WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h2[@class='title text-center']")))
    continue_button = driver.find_element(By.XPATH, "//a[@class='btn btn-primary']")
    continue_button.click()

    assert WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]")))
    delete_account = driver.find_element(By.XPATH, "//a[@href='/delete_account']")
    delete_account.click()

    assert WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h2[@class='title text-center']")))
    continue_button2 = driver.find_element(By.XPATH, "//a[@class='btn btn-primary']")
    continue_button2.click()