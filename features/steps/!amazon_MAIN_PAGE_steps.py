# STEPS FOR AMAZON MAIN PAGE

from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import *
from selenium.webdriver.support import expected_conditions as EC
import time

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
HAM_MENU_BTN = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'td.navFooterDescItem a')
SIGN_IN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")
CART_EMPTY = (By.XPATH, "//h2[contains(text(), 'Your Amazon Cart is empty')]")


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
    time.sleep(3)


# TOP HEADER
@when('Click on Cart')
def click_on_cart(context):
    cart = context.driver.find_element(By.ID, "nav-cart-count-container")
    cart.click()
    cart_is_empty = context.driver.wait.until(
        EC.visibility_of_element_located(CART_EMPTY), '"Your Amazon Cart is empty" text is not visible'
    )


@when('Click on button from SignIn popup')
def click_sign_in_btn(context):
    sign_in_btn = context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn not clickable'
    )
    sign_in_btn.click()


# HEADER MENU
@when('Click on Best Sellers')
def click_on_best_sellers(context):
    best_sellers = context.driver.find_element(By.CSS_SELECTOR, "#nav-xshop-container [data-csa-c-content-id='nav_cs_bestsellers']")
    best_sellers.click()
    time.sleep(1)


@then('Verify that Best Sellers page is opened')
def verify_best_sellers_opened(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "#zg_banner_text").text
    expected_result = 'Amazon Best Sellers'
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


# BOTTOM MENU - Let Us Help You - Help
@when('Scroll down to the bottom menu')
def scroll_to_bottom_menu(context):
    element = context.driver.find_element(By.XPATH, "//*[contains(@class, 'navFooter') and contains(text(), 'Let Us')]")
    context.driver.execute_script("arguments[0].scrollIntoView();", element)


@when('Open Amazon Help page')
def open_amazon_help_page(context):
    help_page = context.driver.find_element(By.CSS_SELECTOR, "[href*='footer_gw_m_b_he']")
    help_page.click()
    time.sleep(1)


@then('Verify Amazon Help page is opened')
def verify_amazon_help_page_opened(context):
    expected_result = "Hello. What can we help you with?"
    expected_result2 = "Welcome to Amazon Customer Service"
    actual_result = context.driver.find_element(By.XPATH, "//h1[contains(text(), '')]").text
    if actual_result == expected_result:
        assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'
    elif actual_result == expected_result2:
        assert expected_result2 == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'
