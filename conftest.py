import pytest
from pytest_bdd.hooks import pytest_bdd_before_scenario

from modules.UserFactory import UserFactory
from modules.selenium_factory import SeleniumFactory


@pytest.fixture(params=["browser"], scope="session")
def driver_init(request):
    browser = request.param.get("browser", "chrome")
    driver = SeleniumFactory.create_driver(browser)
    request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture
def test_user(request):
    user  = UserFactory.build()
    return user
