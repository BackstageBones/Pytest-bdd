from modules.selenium_actions import SeleniumActions
from locators.authentication_page_locators import AuthenticationPageLocators

class AuthenticationPage:

    def __init__(self, driver):
        self.actions = SeleniumActions(driver)

    def create_account(self, email):
        self.actions.wait_for_element_visible(AuthenticationPageLocators.create_account_button)
        self.actions.send_text(AuthenticationPageLocators.create_ac_email_input, email)
        self.actions.click_element(AuthenticationPageLocators.create_account_button)

    def sign_in(self, email, password):
        self.actions.wait_for_element_visible(AuthenticationPageLocators.sign_in_button)
        self.actions.send_text(AuthenticationPageLocators.sing_in_email_input, email)
        self.actions.send_text(AuthenticationPageLocators.password_input, password)
        self.actions.click_element(AuthenticationPageLocators.sign_in_button)
