# 1. Find the most optimal locators for Create Account (Registration) page elements

'''
amazon_logo = driver.find_element(By.CSS_SELECTOR, '#a-page .a-icon-logo')
create_account_text = driver.find_element(By.XPATH, "//h1[contains(text(), 'Create account')]")
your_name_text_field = driver.find_element(By.ID, 'ap_customer_name')
email_text_field = driver.find_element(By.ID, 'ap_email')
password_text_field = driver.find_element(By.ID, 'ap_password')
passwords_6_chars_text = driver.find_element(By.XPATH, "//div[contains(text(), 'Passwords must be at least 6 characters.')]")
reenter_pass_text_field = driver.find_element(By.ID, 'ap_password_check')
continue_button = driver.find_element(By.ID, 'continue')
conditions_of_use_link = driver.find_element(By.XPATH, "//div[@id='legalTextRow']/*[text()='Conditions of Use']")
privacy_notice_link = driver.find_element(By.XPATH, "//div[@id='legalTextRow']/*[text()='Privacy Notice']")
signin_link = driver.find_element(By.XPATH, "//*[contains(@href, 'signin')]")
create_free_business_acc = driver.find_element(By.ID, 'ab-registration-link')
'''

