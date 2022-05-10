# STEPS FOR AMAZON HEADER MENU

from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
import time


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

