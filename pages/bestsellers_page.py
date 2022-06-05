from pages.base_page import Page

from selenium.webdriver.common.by import By

class BestsellersPage(Page):
    SUB_LINKS_UNDER_BEST_SELLERS = (By.CSS_SELECTOR, 'div ul li a[href*="/ref=zg_"]')

    def open_bestsellers(self):
        self.open_page('/gp/bestsellers/')

    def verify_links_preset(self, expected_amount):
        expected_amount = int(expected_amount)
        sub_links_under_best_sellers = self.driver.find_elements(*self.SUB_LINKS_UNDER_BEST_SELLERS)
        assert len(
            sub_links_under_best_sellers) == expected_amount, f'Error! Expected {expected_amount} of sub-links under Best Sellers tab, but got {len(sub_links_under_best_sellers)}'


