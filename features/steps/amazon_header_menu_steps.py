# STEPS FOR AMAZON HEADER MENU

from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
import time


@when('Click on "New Releases"')
def click_on_new_releases(context):
        new_releases = context.driver.find_element(By.CSS_SELECTOR, "[href*='new-releases']")
        new_releases.click()
        time.sleep(1)


@then('Verify that "New Releases" page is opened')
def verify_new_releases_opened(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "#zg_banner_text").text
    expected_result = 'Amazon Hot New Releases'
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


@when('Click on "Movers & Shakers"')
def click_on_movers_and_shakers(context):
        movers_and_shakers = context.driver.find_element(By.CSS_SELECTOR, "[href*='movers-and-shakers']")
        movers_and_shakers.click()
        time.sleep(1)


@then('Verify that "Movers & Shakers" page is opened')
def verify_movers_and_shakers_opened(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "#zg_banner_text").text
    expected_result = 'Amazon Movers & Shakers'
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


@when('Click on "Most Wished For"')
def click_on_most_wished_for(context):
        most_wished_for = context.driver.find_element(By.CSS_SELECTOR, "[href*='most-wished-for']")
        most_wished_for.click()
        time.sleep(1)


@then('Verify that "Most Wished For" page is opened')
def verify_most_wished_for_opened(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "#zg_banner_text").text
    expected_result = 'Amazon Most Wished For'
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'


@when('Click on "Gift Ideas"')
def click_on_gift_ideas(context):
        gift_ideas = context.driver.find_element(By.CSS_SELECTOR, "[href*='most-gifted']")
        gift_ideas.click()
        time.sleep(1)


@then('Verify that "Gift Ideas" page is opened')
def verify_gift_ideas_opened(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "#zg_banner_text").text
    expected_result = 'Amazon Gift Ideas'
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'

