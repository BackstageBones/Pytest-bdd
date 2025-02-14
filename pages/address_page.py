from dataclasses import dataclass

from locators.address_page_locators import AddressPageLocators
from modules.selenium_actions import SeleniumActions


class AddressPage:

    def __init__(self, driver):
        self.actions = SeleniumActions(driver)

    def is_page_loaded(self):
        return self.actions.is_element_displayed(AddressPageLocators.address_modal)

    def fill_delivery_details(self, user: dataclass):
        self.actions.send_text(AddressPageLocators.address_field, user.address)
        self.actions.send_text(AddressPageLocators.city_field, user.city)
        self.actions.select_element_by_text(AddressPageLocators.state_selector, user.state)
        self.actions.send_text(AddressPageLocators.postal_code_field, user.postal_code)
        self.actions.send_text(AddressPageLocators.mobile_phone_field, user.mobile_number)
        self.actions.click_element(AddressPageLocators.submit_address_button)


    def click_proceed_to_checkout(self):
        self.actions.scroll_to_element_center(AddressPageLocators.proceed_to_checkout)
        self.actions.click_element(AddressPageLocators.proceed_to_checkout)
