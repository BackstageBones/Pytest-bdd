from dataclasses import replace

from assertpy import assert_that
from pytest_bdd import given, when, then, parsers, scenarios, step

from modules.UsersEnum import UsersEnum
from pages.authentication_page import AuthenticationPage
from pages.automation_practice_main_page import MainPage
from pages.my_account_page import MyAccountPage
from pages.registration_page import RegistrationPage

scenarios("register.feature", "login.feature")


def adopt_test_user(test_user, user):
    if user in UsersEnum.__members__:
        updated_user = replace(test_user, **UsersEnum[user].value)
        return updated_user
    return test_user


@when("User chooses to sign in")
def step_impl(request):
    main_page = MainPage(request.node.driver)
    main_page.click_sign_in()


@given("User opens automation practice website")
def step_impl(request):
    main_page = MainPage(request.node.driver)
    main_page.open_main_page()


@step(parsers.parse("Selects option to register as new user by filling e-mail field with user {user} data"),
      target_fixture="test_user")
def step_impl(request, user, test_user):
    user = adopt_test_user(test_user, user)
    authentication_page = AuthenticationPage(request.node.driver)
    authentication_page.create_account(user.email)
    return user


@step("User fills registration form with personal data")
def step_impl(request, test_user):
    registration_page = RegistrationPage(request.node.driver)
    registration_page.fill_registration_form(test_user)


@then("User is successfully registered")
def step_impl(request):
    account_page = MyAccountPage(request.node.driver)
    assert_that(account_page.is_page_displayed(), "Account page not visible").is_true()
    assert_that(account_page.is_registered(), "User not registered successfully").is_true()


@step(parsers.parse("User fills login fields with users {user} credentials"))
def step_impl(request, user, test_user):
    user = adopt_test_user(test_user, user)
    authentication_page = AuthenticationPage(request.node.driver)
    authentication_page.sign_in(user.email, user.password)
    return user


@step("Clicks sign in button")
def step_impl(request):
    authentication_page = AuthenticationPage(request.node.driver)
    authentication_page.click_sign_in_button()


@then("User is logged in")
def step_impl(request):
    account_page = MyAccountPage(request.node.driver)
    assert_that(account_page.is_page_displayed(), "Account page not visible").is_true()
