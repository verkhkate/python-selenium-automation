# STEPS FOR AMAZON MAIN PAGE

from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
import time


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')


@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')
    time.sleep(1)


@when('Verify Amazon page is opened')
def verify_amazon_page_opened(context):
    actual_result = context.driver.title
    expected_result = 'Amazon.com. Spend less. Smile more.'
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


# SEARCH
@when('Search for {search_word}')
def search_amazon(context, search_word):
    context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()


# HEADER
@when('Click on Cart')
def click_on_cart(context):
    cart = context.driver.find_element(By.ID, "nav-cart-count-container")
    cart.click()
    time.sleep(2)


# BOTTOM MENU - Let Us Help You - Help
@when('Open Amazon Help page')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Verify Amazon Help page is opened')
def verify_amazon_help_page_opened(context):
    actual_result = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Hello. What can we help you with?')]").text
    expected_result = 'Hello. What can we help you with?'
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'