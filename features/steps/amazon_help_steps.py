# STEPS FOR AMAZON HELP PAGE

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import *
import time


# Scenario: User can search for solutions of Canceling an order on Amazon from Help page
@then('Locate "Search Help Library" field and search for "Cancel order"')
def locate_search_help_field(context):
    search_cancel_order = context.driver.find_element(By.ID,'helpsearch')
    search_cancel_order.clear()
    search_cancel_order.send_keys('Cancel order')
    search_cancel_order.send_keys(Keys.RETURN)


@then('Verify that "Cancel Items or Orders" text is displayed')
def verify_cancel_items_or_orders(context):
    expected_result = 'Cancel Items or Orders'
    actual_result = context.driver.find_element(By.XPATH,"//h1").text
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


# Scenario: Verify that Amazon Help page UI elements are present on the page
@then('Verify that Some things you can do here text result is displayed')
def verify_some_things(context):
    expected_result = 'Some things you can do here'
    actual_result = context.driver.find_element(By.CSS_SELECTOR,"div.a-section h2").text
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


@then('Verify that "Search the help library" text is displayed')
def search_help_library(context):
    expected_result = 'Search the help library'
    actual_result = context.driver.find_element(By.XPATH, "//label[@id='help-search-label']//span[contains(text(), 'Search the help library')]").text
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


@then('Verify that "Type something like, question about a charge" text result is displayed')
def type_smth_like(context):
    expected_result = 'Type something like, "question about a charge"'
    actual_result = context.driver.find_element(By.XPATH, "//label[@id='help-search-label']//span[contains(text(), 'Type something like')]").text
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


@then('Scroll down to "Browse Help Topics"')
def scroll_to_browse_help(context):
    element = context.driver.find_element(By.XPATH, "//*[contains(@class, 'help-content')]//*[contains(text(), 'Browse Help')]")
    context.driver.execute_script("arguments[0].scrollIntoView();", element)


@then('Verify that Browse Help Topics text is displayed')
def browse_help_topics(context):
    expected_result = 'Browse Help Topics'
    actual_result = context.driver.find_element(By.XPATH, "//*[contains(@class,'help-content')]//*[contains(text(),'Browse Help')]").text
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


@then('Verify that Where is My Stuff text is properly displayed')
def where_is_my_stuff(context):
    expected_result = "Where's My Stuff?"
    actual_result = context.driver.find_element(By.XPATH, "//*[contains(@rel, 'help-gateway-category') and contains(text(),'My Stuff?')]").text
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


@then('Verify that {find_text} text is displayed')
def find_text_1(context, find_text):
    expected_result = find_text
    actual_result = context.driver.find_element(By.XPATH, f"//*[contains(@class , 'a-column')]//*[ contains(text(), '{find_text}')]").text
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


@then('Verifying that "{find_text2}" text is displayed')
def find_text_2(context, find_text2):
    expected_result = find_text2
    actual_result = context.driver.find_element(By.XPATH, f"//*[contains(@rel, 'help-gateway-category') and contains(text(),'{find_text2}')]").text
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


@then('Verify that "Wrenches icon" is displayed')
def wrenches_icon(context):
    wrenches_pic = context.driver.find_element(By.CSS_SELECTOR, "#help-gateway-category-0 img.csg-hb-promo")