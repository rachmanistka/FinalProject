from .base_page import BasePage
from .locators import ProductPageLocators
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def should_be_in_basket(self):
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_match_with_title()
        self.should_match_with_cost()
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
    def should_match_with_title(self):
        title_in_message = self.browser.find_element(*ProductPageLocators.TITLE_IN_MESSAGE).text
        real_title = self.browser.find_element(*ProductPageLocators.REAL_TITLE).text
        assert title_in_message==real_title, "Title doesn't match"
    def should_match_with_cost(self):
        cost_in_message = self.browser.find_element(*ProductPageLocators.COST_IN_MESSAGE).text
        real_cost = self.browser.find_element(*ProductPageLocators.REAL_COST).text
        assert cost_in_message==real_cost, "Cost doesn't match"
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should disappear"