# STEPS FOR AMAZON SEARCH FROM HELP PAGE

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
import time

# Scenario: User can search for solutions of Canceling an order on Amazon from Help page
@then ('Locate "Search Help Library" field and search for "Cancel order"')
def locate_search_help_field(context):
    search_cancel_order = context.driver.find_element(By.ID, 'helpsearch')
    search_cancel_order.clear()
    search_cancel_order.send_keys('Cancel order')
    search_cancel_order.send_keys(Keys.RETURN)


@then ('Verify that "Cancel Items or Orders" text is displayed')
def verify_cancel_items_or_orders(context):
    expected_result = 'Cancel Items or Orders'
    actual_result = context.driver.find_element(By.XPATH, "//h1").text
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'