from locators.shopping_locators import ShoppingLocators
from modules.selenium_actions import SeleniumActions


class PaymentPage:

    def __init__(self, driver):
        self.actions = SeleniumActions(driver)

    def is_page_loaded(self) -> bool:
        return self.actions.is_element_displayed(ShoppingLocators.payment_container)

    def click_pay_by_wire(self) -> None:
        self.actions.click_element(ShoppingLocators.pay_by_wire)

    def submit_payment(self) -> None:
        self.actions.click_element(ShoppingLocators.submit_payment)

    def is_payment_completed(self) -> bool:
        return self.actions.is_element_displayed(ShoppingLocators.payment_success_message_alert)

