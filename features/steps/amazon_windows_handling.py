# STEPS FOR WINDOWS HANDLING

from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import *
from selenium.webdriver.support import expected_conditions as EC
import time


PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR, "[href*='www.amazon.com/privacy']")


@given('Open Amazon Terms & Conditions page')
def open_terms_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html'
                       '/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
    context.driver.wait.until(
        EC.visibility_of_element_located(PRIVACY_NOTICE_LINK),
        'Privacy Notice link is not visible')


@when('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    context.old_windows = context.driver.window_handles


@when('Click on Amazon Privacy Notice link')
def click_on_privacy_notice(context):
    context.driver.find_element(*PRIVACY_NOTICE_LINK).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])


@then('Close Amazon Privacy Notice window')
def close_privacy_notice_window(context):
    context.driver.close()


@then('Return to Amazon Terms & Conditions window')
def return_to_terms_window(context):
    context.driver.switch_to.window(context.original_window)
