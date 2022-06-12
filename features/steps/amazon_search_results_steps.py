from selenium.webdriver.common.by import By
from behave import *
import time

PRODUCT_QUANTITY = (By.CSS_SELECTOR, "h2 span.a-size-base-plus/*[aria-hidden*='false']")
PRODUCT_QUANTITY_HIDDEN = (By.CSS_SELECTOR, ".a-carousel-card[aria-hidden= 'true']")
PRODUCT_NAME = (By.XPATH, "//h2/a/span[contains(@class, 'a-size-base-plus a-color-base a-text-normal') and contains(text(), '')]")
PRODUCT_IMAGE = (By.CSS_SELECTOR, ".sg-col-inner .s-image-tall-aspect")


@then('Verify search results for {expected_result} are shown')
def verify_search_results(context, expected_result):
    context.app.search_results_page.verify_search_results(expected_result)

@then('Verify that every product on Amazon search results page has product name and image')
def verify_product_name_and_image(context):
    total_product_quantity = len(context.driver.find_elements(*PRODUCT_QUANTITY))
    print("Total products count: ", total_product_quantity)
    actual_product_hidden = len(context.driver.find_elements(*PRODUCT_QUANTITY_HIDDEN))
    print("Hidden products count: ", actual_product_hidden)
    actual_visible_product_quantity = (total_product_quantity - actual_product_hidden)
    print("Actual visible products count: ", actual_visible_product_quantity)
    time.sleep(2)
    actual_visible_product_names_text = context.driver.find_elements(*PRODUCT_NAME)
    actual_visible_product_names = (len(context.driver.find_elements(*PRODUCT_NAME)) - actual_product_hidden)
    print("Actual visible products names: ", actual_visible_product_names)
    actual_visible_product_image = (len(context.driver.find_elements(*PRODUCT_IMAGE)) - actual_product_hidden)
    print("Actual visible products images: ", actual_visible_product_image)

    # i = 0
    # while i < actual_visible_product_quantity:
    #     print(actual_visible_product_names_text[i].text)
    #     i = i + 1

    assert actual_visible_product_quantity == actual_visible_product_names, \
        f'Test case failed! Actual visible product count of: {actual_visible_product_quantity} does not match ' \
        f'actual quantity of product names: {actual_visible_product_names}'
    assert actual_visible_product_quantity == actual_visible_product_image, \
        f'Test case failed! Actual visible product count of: {actual_visible_product_quantity} does not match ' \
        f'actual quantity of product names: {actual_visible_product_image}'


@then('Scroll to the bottom of search results') # SCROLL WITH DELAY
def scroll_to_bottom(context):
    total_height = int(context.driver.execute_script("return document.body.scrollHeight"))
    for i in range(1, total_height, 10):
        context.driver.execute_script("window.scrollTo(0, {});".format(i))


@then('Scroll down')
def scroll_down(context):
    context.app.search_results_page.scroll_down()
    time.sleep(1)