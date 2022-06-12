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
CART_EMPTY = (By.XPATH, "//h2[contains(text(), 'Your Amazon Cart is empty')]")
SUB_LINKS_UNDER_BEST_SELLERS = (By.CSS_SELECTOR, 'div ul li a[href*="/ref=zg_"]')
SIGN_IN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")
SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")


@given('Open Amazon page')
def open_amazon_page(context):
    context.app.main_page.open_main_page()
    time.sleep(1)


@when('Verify Amazon page is opened')
def verify_amazon_page_opened(context):
    actual_result = context.driver.title
    expected_result = 'Amazon.com. Spend less. Smile more.'
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


@when('Wait for {seconds} seconds')
def wait_sec(context, seconds):
    time.sleep(int(seconds))


# SEARCH
@when('Search for {search_word}')
def search_amazon(context, search_word):
    context.app.header.search_amazon(search_word)
    time.sleep(3)


@then('Verify {department} department is selected')
def verify_department(context, department):
    context.app.header.verify_department(department)


# HEADER
@given('Open Amazon Bestsellers')
def open_amazon_bestsellers(context):
    context.app.bestsellers_page.open_bestsellers()


@then('Verify there are {expected_amount} sub-links under Best Sellers tab')
def verify_sub_links_under_best_sellers(context, expected_amount):
    context.app.bestsellers_page.verify_links_preset(expected_amount)


@when('Click on New Releases page')
def click_on_new_releases(context):
        new_releases = context.driver.find_element(By.CSS_SELECTOR, "[href*='new-releases']")
        new_releases.click()
        time.sleep(1)


@when('Click on Movers & Shakers page')
def click_on_movers_and_shakers(context):
        movers_and_shakers = context.driver.find_element(By.CSS_SELECTOR, "[href*='movers-and-shakers']")
        movers_and_shakers.click()
        time.sleep(1)


@when('Click on Most Wished For page')
def click_on_most_wished_for(context):
        most_wished_for = context.driver.find_element(By.CSS_SELECTOR, "[href*='most-wished-for']")
        most_wished_for.click()
        time.sleep(1)


@when('Click on Gift Ideas page')
def click_on_gift_ideas(context):
        gift_ideas = context.driver.find_element(By.CSS_SELECTOR, "[href*='most-gifted']")
        gift_ideas.click()
        time.sleep(1)


@then('Verify that {page_name} page is opened')
def find_text_1(context, page_name):
    expected_result = page_name
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "#zg_banner_text").text
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


@when('Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()


@then('Verify Spanish option present')
def verify_spanish_lang(context):
    context.app.header.verify_spanish_lang()


@when('Click on Best Sellers')
def click_on_best_sellers(context):
    best_sellers = context.driver.find_element(By.CSS_SELECTOR, "#nav-xshop-container [data-csa-c-content-id='nav_cs_bestsellers']")
    best_sellers.click()
    time.sleep(1)


@when('Click on cart')
def click_on_cart(context):
    context.app.main_page.click_on_cart()


@when('Click on button from SignIn popup')
def click_sign_in_btn(context):
    sign_in_btn = context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn not clickable'
    )
    sign_in_btn.click()


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Error! Title should not be blank'
        product.find_element(*PRODUCT_IMG)


@then('SignIn popup is present')
def verify_signin_popup_present(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn not clickable')


@then('SignIn popup disappears')
def verify_signin_popup_not_present(context):
    context.driver.wait.until_not(EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn did not disappear')


@when('Select department by {alias}')
def select_dep(context, alias):
    context.app.header.select_dep(alias)


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











































