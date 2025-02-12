from dataclasses import dataclass

from selenium.webdriver.common.by import By


class MyAccountLocators:
    account_page_form: By = (By.ID, "center_column")
    registration_success_message: By = (By.XPATH, "//p[@class='alert alert-success']")