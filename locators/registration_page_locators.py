from dataclasses import dataclass
from selenium.webdriver.common.by import By
@dataclass
class RegistrationLocators:
    form: By = (By.ID, "account-creation_form")
    male_input: By = (By.ID, "id_gender1")
    female_input: By = (By.ID, "id_gender2")
    first_name_input: By = (By.ID, "customer_firstname")
    last_name_input: By = (By.ID, "customer_lastname")
    email_input: By = (By.ID, "email")
    password_input: By = (By.ID, "passwd")
    days_selector: By = (By.ID, "days")
    months_selector: By = (By.ID, "months")
    years_selector: By = (By.ID, "years")
    submit_button: By = (By.ID, "submitAccount")