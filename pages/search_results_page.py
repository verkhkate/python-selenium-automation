from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultsPage(Page):
    SEARCH_RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    CLICK_ANY_ITEM = (By.XPATH, "//*[@data-index=9]//*[contains(@class,'a-size-mini')]//*[contains(@class,'a-size')]")
    ADD_TO_CART = (By.ID, "add-to-cart-button")
    ACTUAL_RESULT1 = (By.ID, "productTitle")
    ACTUAL_RESULT2 = (By.XPATH, "//span[contains(text(), 'Added to Cart')]")
    ACTUAL_RESULT3 = (By.XPATH, "//span[@class='a-truncate-cut']")
    def verify_search_results(self, expected_result):
        self.verify_text(expected_result, *self.SEARCH_RESULT_TEXT)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, 300)")

    def click_on_item(self):
        self.item = self.driver.find_element(By.XPATH, "//*[@data-index=9]//*[contains(@class,'a-size-mini')]//*[contains(@class,'a-size')]").text
        self.click(*self.CLICK_ANY_ITEM)

    def click_verify_item(self):
        self.verify_text(self.item, *self.ACTUAL_RESULT1)

    def add_item_to_cart(self):
        self.click(*self.ADD_TO_CART)

    def verify_item_added_to_cart(self):
        self.verify_text('Added to Cart', *self.ACTUAL_RESULT2)

    def verify_item_in_cart(self):
        self.verify_text(self.item, *self.ACTUAL_RESULT3)
