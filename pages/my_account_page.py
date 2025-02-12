from locators.myaccount_locators import MyAccountLocators
from modules.selenium_actions import SeleniumActions


class MyAccountPage:

    def __init__(self, driver):
        self.action = SeleniumActions(driver)

    def is_page_displayed(self) -> bool:
        return self.action.is_element_displayed(MyAccountLocators.account_page_form)

    def is_registered(self) -> bool:
        return self.action.is_element_displayed(MyAccountLocators.registration_success_message)