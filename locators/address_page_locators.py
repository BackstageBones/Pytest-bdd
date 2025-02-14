

from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class AddressPageLocators:
    proceed_to_checkout: By = (By.XPATH, "//button[@name='processAddress']")
    address_modal: By = (By.ID, "center_column")
    address_field: By = (By.ID, "address1")
    city_field: By = (By.ID, "city")
    state_selector: By = (By.ID, "id_state")
    postal_code_field: By = (By.ID, "postcode")
    mobile_phone_field: By = (By.ID, "phone_mobile")
    submit_address_button: By = (By.ID, "submitAddress")