from locators.shopping_cart_locators import ShoppingCartLocators
from modules.selenium_actions import SeleniumActions


class ShoppingCartPage:

    def __init__(self, driver):
        self.actions = SeleniumActions(driver)

    def is_page_loaded(self) -> bool:
        return self.actions.is_element_displayed(ShoppingCartLocators.cart_title)

    def click_proceed_to_checkout(self):
        self.actions.click_element(ShoppingCartLocators.proceed_to_checkout_btn)
