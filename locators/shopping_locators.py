
from dataclasses import dataclass

from selenium.webdriver.common.by import By

@dataclass
class ShoppingLocators:
    payment_container: By = (By.ID, "HOOK_PAYMENT")
    pay_by_wire: By = (By.XPATH, "//a[@class='bankwire']")
    submit_payment: By = (By.XPATH, "//button[@class='button btn btn-default button-medium']")
    payment_success_message_alert : By = (By.XPATH, "//p[@class='alert alert-success']")