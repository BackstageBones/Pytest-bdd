from dataclasses import dataclass
from selenium.webdriver.common.by import By
@dataclass
class AuthenticationPageLocators:
    create_ac_email_input: By = (By.ID, "email-create")
    sing_in_email_input: By = (By.ID, "email")
    password_input: By = (By.ID, "passwd")
    create_account_button:By = (By.ID, "SubmitCreate")
    sign_in_button:By = (By.ID, "SubmitLogin")