from dataclasses import dataclass
from selenium.webdriver.common.by import By
@dataclass
class MainPageLocators:
    sing_in_btn: By = (By.XPATH, "//a[@class='login']")