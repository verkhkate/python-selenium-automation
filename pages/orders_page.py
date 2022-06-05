from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(Page):
    AMAZON_ORDERS_LINK = (By.CSS_SELECTOR, '#nav-orders')
    def click_orders_link(self, *locator):
        self.click(*self.AMAZON_ORDERS_LINK)

    def verify_sign_in_page_opened(self):
        self.driver.wait.until(
            EC.url_contains('https://www.amazon.com/ap/signin'),
            message='Sign in page never opened'
        )