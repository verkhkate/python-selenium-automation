
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
import time


#AMAZON_ORDERS_LINK = (By.CSS_SELECTOR, '#nav-orders')


@when('Click Amazon Orders link')
def click_orders_link(context):
    #context.driver.find_element(*AMAZON_ORDERS_LINK).click()
    context.app.orders_page.click_orders_link()