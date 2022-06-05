from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    CART_LINK = (By.ID, "nav-cart-count-container")
    EMPTY_CART = (By.XPATH, "//h2[contains(text(), 'Your Amazon Cart is empty')]")
    def open_main_page(self):
        self.open_page()

    def click_on_cart(self, *locator):
        self.click(*self.CART_LINK)

    def verify_empty_cart(self):
        self.verify_text('Your Amazon Cart is empty', *self.EMPTY_CART)

