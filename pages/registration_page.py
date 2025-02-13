import time
from dataclasses import dataclass

from locators.registration_page_locators import RegistrationLocators
from modules.selenium_actions import SeleniumActions


class RegistrationPage:

    def __init__(self, driver):
        self.actions = SeleniumActions(driver)

    def fill_registration_form(self, test_user: dataclass):
        self.actions.wait_for_element_visible(RegistrationLocators.form)
        self.actions.scroll_to_element_center(RegistrationLocators.form)
        if test_user.gender == "M":
            self.actions.click_element(RegistrationLocators.male_input)
        else:
            self.actions.click_element(RegistrationLocators.female_input)
        self.actions.send_text(RegistrationLocators.first_name_input, test_user.name)
        self.actions.send_text(RegistrationLocators.last_name_input, test_user.surname)
        self.actions.send_text(RegistrationLocators.password_input, test_user.password)
        self.actions.select_element_value(RegistrationLocators.days_selector, test_user.date_of_birth.day)
        self.actions.select_element_value(RegistrationLocators.months_selector, test_user.date_of_birth.month)
        self.actions.select_element_value(RegistrationLocators.years_selector, test_user.date_of_birth.year)
        self.actions.click_element(RegistrationLocators.submit_button)
