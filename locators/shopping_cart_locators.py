from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class ShoppingCartLocators:
    cart_title: By = (By.ID, "cart_title")
    proceed_to_checkout_btn: By = (By.XPATH, "//p//a[@title='Proceed to checkout']")
