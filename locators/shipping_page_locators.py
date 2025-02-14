from dataclasses import dataclass

from selenium.webdriver.common.by import By

@dataclass
class ShippingPageLocators:
    proceed_to_checkout: By = (By.XPATH, "//button[@name='processCarrier']")
    shipping_modal: By = (By.ID, "carrier_area")
    terms_of_service_checkbox: By = (By.ID, "uniform-cgv")
