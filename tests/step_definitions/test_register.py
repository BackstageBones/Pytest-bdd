from dataclasses import replace

from assertpy import assert_that
from pytest_bdd import given, when, then, parsers, scenarios, step

from modules.UsersEnum import UsersEnum
from pages.authentication_page import AuthenticationPage
from pages.automation_practice_main_page import MainPage
from pages.my_account_page import MyAccountPage
from pages.registration_page import RegistrationPage
from pages.shopping_cart_page import ShoppingCartPage

scenarios("register.feature", "login.feature", "shopping flow.feature")


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


@when(parsers.parse("User searches for {param} in product search bar"))
def step_impl(request, param):
    main_page = MainPage(request.node.driver)
    main_page.search_for(param.lower())


@step("product results are displayed")
def step_impl(request):
    main_page = MainPage(request.node.driver)
    assert_that(main_page.are_products_displayed(), "At least one product is expected to be present").is_true()


@step(parsers.parse("User sorts displayed results by {param} param"))
def step_impl(request, param):
    main_page = MainPage(request.node.driver)
    main_page.filter_products_by(param.lower())


@step(parsers.parse("Products are sorted by {param} param"))
def step_impl(request, param):
    main_page = MainPage(request.node.driver)
    assert_that(main_page.are_products_displayed(), "At least one product is expected to be present").is_true()
    match param:
        case "in stock":
            assert_that(len(main_page.get_products_availability_labels()),
                        "At least one product is expected to be in stock, but none were").is_greater_than_or_equal_to(1)
        case _:
            raise NotImplementedError


@step("User is able to add product to basket")
def step_impl(request):
    main_page = MainPage(request.node.driver)
    product_list = main_page.get_available_products()
    main_page.open_random_product(product_list)
    main_page.add_product_to_basket()
    assert_that(main_page.is_product_added(), "Product couldn't be added to basket for some reason").is_true()
    main_page.click_add_to_basket()


@given("User can proceed with product to checkout")
def step_impl(request):
    sh_page = ShoppingCartPage(request.node.driver)
    assert_that(sh_page.is_page_loaded(), "Shopping cart page not visible").is_true()
    sh_page.click_proceed_to_checkout()