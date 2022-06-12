from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class ProductDetails(Page):
    NEW_ARRIVALS = (By.XPATH, '//span[@class="nav-a-content" and contains(text(), "New Arrivals")]')
    NEW_ARRIVALS_DEALS_WOMEN = (By.XPATH, '//h3[contains(text(), "Women")]')
    NEW_ARRIVALS_DEALS_MEN = (By.XPATH, '//h3[contains(text(), "Men")]')
    NEW_ARRIVALS_DEALS_GIRLS = (By.XPATH, '//h3[contains(text(), "Girls")]')
    NEW_ARRIVALS_DEALS_BOYS = (By.XPATH, '//h3[contains(text(), "Boys")]')
    NEW_ARRIVALS_DEALS_BABY = (By.XPATH, '//h3[contains(text(), "Baby")]')
    NEW_ARRIVALS_DEALS_LUGGAGE = (By.XPATH, '//h3[contains(text(), "Luggage")]')

    def hover_new_arrivals(self):
        actions = ActionChains(self.driver)
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_new_arrivals_deals(self):
        self.wait_for_element_appear(*self.NEW_ARRIVALS_DEALS_WOMEN)
        self.wait_for_element_appear(*self.NEW_ARRIVALS_DEALS_MEN)
        self.wait_for_element_appear(*self.NEW_ARRIVALS_DEALS_GIRLS)
        self.wait_for_element_appear(*self.NEW_ARRIVALS_DEALS_BOYS)
        self.wait_for_element_appear(*self.NEW_ARRIVALS_DEALS_BABY)
        self.wait_for_element_appear(*self.NEW_ARRIVALS_DEALS_LUGGAGE)
