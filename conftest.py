import os
from datetime import datetime
import allure
import pytest

from modules.UserFactory import UserFactory
from modules.selenium_factory import SeleniumFactory


@pytest.fixture
def test_user(request):
    user = UserFactory.build()
    return user


@pytest.hookimpl
def pytest_bdd_before_scenario(request, feature, scenario):
    driver = SeleniumFactory.create_driver("chrome")
    request.node.driver = driver
    driver.delete_all_cookies()
    driver.execute_cdp_cmd('Storage.clearDataForOrigin', {
        "origin": '*',
        "storageTypes": 'all',
    })

    def cleanup():
        driver.close()
        driver.quit()

    request.addfinalizer(cleanup)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_exception_interact(node, call, report):
    if report.failed:
        if not os.path.exists("screenshots"):
            os.mkdir("screenshots")
        screenshot_name = "screenshot_{}.png".format(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
        screenshot_path = os.path.abspath("screenshots/" + screenshot_name)
        node.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name=screenshot_name, attachment_type=allure.attachment_type.PNG)
    yield
