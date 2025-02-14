import random

from selenium.common import NoSuchElementException, TimeoutException

from locators.automation_main_page import MainPageLocators
from modules.selenium_actions import SeleniumActions


class MainPage(object):
    URL = "http://www.automationpractice.pl/index.php"

    def __init__(self, driver):
        self.actions = SeleniumActions(driver)

    def open_main_page(self):
        self.actions.driver.delete_all_cookies()
        return self.actions.driver.get(MainPage.URL)

    def click_sign_in(self):
        self.actions.wait_for_element_visible(MainPageLocators.sing_in_btn)
        self.actions.click_element(MainPageLocators.sing_in_btn)

    def search_for(self, item):
        self.actions.wait_for_element_visible(MainPageLocators.search_bar)
        self.actions.send_text(MainPageLocators.search_bar, item)
        self.actions.click_element(MainPageLocators.submit_search)

    def are_products_displayed(self) -> bool:
        try:
            self.actions.are_any_elements_visible(MainPageLocators.products)
        except (NoSuchElementException, TimeoutException):
            return False
        return True

    def filter_products_by(self, param):
        try:
            self.actions.select_element_text(MainPageLocators.sort_by_selector, param)
        except NoSuchElementException:
            return ValueError("This type of sorting is not supported.")
        else:
            self.actions.wait_for_elements_visible(MainPageLocators.products)

    def get_products_availability_labels(self) -> list:
        return [element.text.strip() for element in
                self.actions.are_any_elements_visible(MainPageLocators.products_availability_label) if
                element.text.strip != "out of stock"]

    def get_available_products(self) -> list:
        return [element.find_element(*MainPageLocators.product_label_ancestor) for element
                in self.actions.are_any_elements_visible(MainPageLocators.products_availability_label) if
                element.text.strip != "out of stock"]

    def open_random_product(self, product_list: list) -> None:
        product = random.choice(product_list)
        self.actions.scroll_to_element_center(product)
        self.actions.click_element(product)

    def add_product_to_basket(self):
        self.actions.wait_for_element_visible(MainPageLocators.form)
        if not self.actions.is_displayed_persistent(MainPageLocators.add_to_cart_button, timeout=3):
            available = False
            for size in self.actions.get_selector_options(MainPageLocators.sizes_selector):
                for color in self.actions.find_elements(MainPageLocators.changeable_colors):
                    self.actions.select_element_by_text(MainPageLocators.sizes_selector, size.text)
                    self.actions.click_element(color)
                    if not self.actions.is_element_displayed(MainPageLocators.add_to_cart_button, timeout=3):
                        continue
                    else:
                        available = True
                        break
                if available:
                    break
        self.actions.click_element(MainPageLocators.add_to_cart_button)

    def is_product_added(self) -> bool:
        return self.actions.is_element_displayed(MainPageLocators.successfully_added)

    def click_add_to_basket(self):
        self.actions.click_element(MainPageLocators.successfully_added)