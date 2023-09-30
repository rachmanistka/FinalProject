from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8", 
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_in_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # гость не видит товаров в корзине, переход€ в корзину со страницы товара
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.should_be_empty_basket_confirm_message()

@pytest.mark.user_test
class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser): #self т.к. в классе
        self.browser = browser
        # не€вное ожидание
        self.browser.implicitly_wait(10)
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser,link)
        login_page.open()
        email, password = login_page.make_user_data()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_match_with_title()
        page.should_match_with_cost()
    
    def test_user_cant_see_success_message(self,browser):
        page=ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message()