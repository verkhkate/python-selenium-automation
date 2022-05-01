from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
import time

@then('Verify that Cart is empty')
def verify_empty_cart(context):
    actual_result = context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Your Amazon Cart is empty')]").text
    expected_result = 'Your Amazon Cart is empty'
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


@then('Click on any item')
def click_on_item(context):
    context.item = context.driver.find_element(By.XPATH, "//*[@data-index=2]//*[contains(@class,'a-size-mini')]//*[contains(@class,'a-size')]").text
    item2 = context.driver.find_element(By.XPATH, "//*[@data-index=2]//*[contains(@class,'a-size-mini')]//*[contains(@class,'a-size')]").click()
    time.sleep(1)


@then('Verify item is opened')
def click_on_item(context):
    item_opened = context.driver.find_element(By.ID, "productTitle").text
    actual_result = item_opened
    expected_result = context.item
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'
    time.sleep(1)


@then('Add item to the Cart')
def add_item_to_cart(context):
    add_to_cart = context.driver.find_element(By.ID, "add-to-cart-button").click()
    time.sleep(1)


@then('Verify that item was added to the Cart')
def verify_item_added_to_cart(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[contains(text(), 'Added to Cart')]").text
    expected_result = 'Added to Cart'
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


@then('Verify that item is in the Cart')
def verify_item_in_cart(context):
    item_in_cart = context.driver.find_element(By.XPATH, "//span[@class='a-truncate-cut']").text
    actual_result = item_in_cart
    expected_result = context.item
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'