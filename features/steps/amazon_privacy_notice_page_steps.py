# STEPS FOR PRIVACY NOTICE PAGE

from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import *
from selenium.webdriver.support import expected_conditions as EC
import time


PRIVACY_NOTICE_PAGE_HEADER = (By.CSS_SELECTOR, "h1")


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_opened(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "h1").text
    expected_result = 'Amazon.com Privacy Notice'
    assert expected_result == actual_result, f'Test case failed! ' \
                                             f'Actual text {actual_result} does not match expected {expected_result}'
