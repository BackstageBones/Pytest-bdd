from modules.selenium_actions import SeleniumActions
from locators.automation_main_page import MainPageLocators


class MainPage(object):
    URL = "http://www.automationpractice.pl/index.php"

    def __init__(self, driver):
        self.actions = SeleniumActions(driver)

    def open_main_page(self):
        self.actions.driver.delete_all_cookies()
        return self.actions.driver.get(MainPage.URL)

    def click_sign_in(self):
        self.actions.wait_for_element_visible(MainPageLocators.sing_in_btn)
        self.actions.click_element(MainPageLocators.sing_in_btn)
