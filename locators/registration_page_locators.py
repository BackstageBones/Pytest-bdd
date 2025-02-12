from dataclasses import dataclass
from selenium.webdriver.common.by import By
@dataclass
class RegistrationLocators:
    form: By = (By.ID, "account-creation_form")
    male_input: By = (By.ID, "id_gender1")
    female_input: By = (By.ID, "id_gender2")
    first_name_input: By = (By.ID, "customer_firstname")
    last_name_input: By = (By.XPATH, "//input[@id='customer_lastname']")
    email_input: By = (By.XPATH, "//input[@id='email']")
    password_input: By = (By.XPATH, "//input[@id='passwd']")
    days_selector: By = (By.XPATH, "//select[@id='days']")
    months_selector: By = (By.XPATH, "//select[@id='months']")
    years_selector: By = (By.XPATH, "//select[@id='years']")
    submit_button: By = (By.ID, "submitAccount")