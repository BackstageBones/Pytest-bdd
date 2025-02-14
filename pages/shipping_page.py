from locators.shipping_page_locators import ShippingPageLocators
from modules.selenium_actions import SeleniumActions


class ShippingPage:

    def __init__(self, driver):
        self.actions = SeleniumActions(driver)

    def is_page_loaded(self) -> bool:
        return self.actions.is_element_displayed(ShippingPageLocators.shipping_modal)

    def tick_terms_of_service(self):
        self.actions.click_element(ShippingPageLocators.terms_of_service_checkbox)

    def click_proceed_to_checkout(self):
        self.actions.scroll_to_element_center(ShippingPageLocators.proceed_to_checkout)
        self.actions.click_element(ShippingPageLocators.proceed_to_checkout)
