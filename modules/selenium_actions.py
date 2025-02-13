from typing import Any

from selenium.common import StaleElementReferenceException, ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumActions:
    DEFAULT_TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: Any) -> WebElement:
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple) -> list:
        return self.driver.find_elements(*locator)

    def wait_for_elements_visible(self, locator: any) -> list:
        return WebDriverWait(self.driver, timeout=SeleniumActions.DEFAULT_TIMEOUT).until(
            ec.visibility_of_any_elements_located(locator)
        )

    def _wait_for_element_clickable(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.driver, poll_frequency=0.5, timeout=SeleniumActions.DEFAULT_TIMEOUT,
                             ignored_exceptions=(
                                 StaleElementReferenceException, ElementClickInterceptedException)).until(
            ec.element_to_be_clickable(locator)
        )

    def click_element(self, locator: Any) -> None:
        element = self._wait_for_element_clickable(locator)
        element.click()

    def wait_for_element_visible(self, locator: Any, timeout=DEFAULT_TIMEOUT) -> WebElement:
        return WebDriverWait(self.driver, timeout=timeout).until(
            ec.visibility_of_element_located(locator)
        )

    def wait_for_element_presence(self, locator: Any, timeout=DEFAULT_TIMEOUT) -> WebElement:
        return WebDriverWait(self.driver, timeout=timeout).until(
            ec.presence_of_element_located(locator)
        )

    def is_element_displayed(self, locator: tuple[str, str], timeout=DEFAULT_TIMEOUT) -> bool:
        try:
            element = self.wait_for_element_visible(locator, timeout=timeout)
        except TimeoutException:
            return False
        else:
            return element.is_displayed()

    def send_text(self, locator: Any, text: str) -> None:
        element = self._wait_for_element_clickable(locator)
        element.send_keys(text)

    def are_any_elements_visible(self, locator: tuple, timeout=DEFAULT_TIMEOUT) -> list[WebElement]:
        return WebDriverWait(self.driver, timeout=timeout).until(
            ec.visibility_of_any_elements_located(locator)
        )

    def scroll_to_element(self, locator: any) -> None:
        if not isinstance(locator, WebElement):
            locator = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    def scroll_to_element_center(self, locator: any) -> None:
        if not isinstance(locator, WebElement):
            locator = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", locator)

    def select_element_by_text(self, locator, text: str) -> None:
        if not isinstance(locator, WebElement):
            locator = self.find_element(locator)
        select_object = Select(locator)
        return select_object.select_by_visible_text(text)

    def set_element_text(self, dropdown, option_value) -> None:
        if not isinstance(dropdown, WebElement):
            dropdown = self.find_element(dropdown)
        return self.driver.execute_script(
            "var select = arguments[0];"
            "for (var i = 0; i < select.options.length; i++) {"
            "  if (select.options[i].value === arguments[1]) {"
            "    select.selectedIndex = i;"
            "    select.dispatchEvent(new Event('change', { bubbles: true }));"
            "    break;"
            "  }"
            "}",
            dropdown, option_value
        )

    def select_element_value(self, dropdown, value) -> None:
        if not isinstance(dropdown, WebElement):
            dropdown = self.find_element(dropdown)
        select = Select(dropdown)
        select.select_by_value(str(value))

    def move_to_element(self, locator):
        actions = ActionChains(self.driver)
        if not isinstance(locator, WebElement):
            locator = self.wait_for_element_presence(locator)
        return actions.move_to_element(locator)
