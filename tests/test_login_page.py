import settings
import pytest
import allure
from pages.login_page import LoginPage
from pages.home_page import HomePage


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Login')
@allure.story('Testing the login page')
@pytest.mark.login
def test_enter_correct_login_data(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    assert login_page.check_that_remember_me_box_is_selected()
    login_page.enter_login_data(email=settings.email, password=settings.password)
    home_page = HomePage(driver)
    assert home_page.check_that_username_is_displayed_in_the_welcome_block


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Login')
@allure.story('Testing the login page')
@pytest.mark.login
def test_login_with_incorrect_password(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    assert login_page.check_that_remember_me_box_is_selected()
    login_page.enter_login_data(email=settings.email, password='qwerty')
    assert login_page.check_alert_message_after_login_with_incorrect_password()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Login')
@allure.story('Testing the login page')
@pytest.mark.login
def test_login_with_incorrect_email(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    assert login_page.check_that_remember_me_box_is_selected()
    login_page.enter_login_data(email='mistake@mail.ru', password=settings.password)
    login_page.check_alert_message_after_login_with_incorrect_email()


@allure.severity(allure.severity_level.MINOR)
@allure.feature('Login')
@allure.story('Testing the login page')
@pytest.mark.login
def test_forget_password_link_presents_on_the_page(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    assert login_page.check_that_forget_password_link_presents_on_the_login_page()


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Login')
@allure.story('Testing the login page')
@pytest.mark.enter_with_a_new_password
# @pytest.mark.skip('Run only at the end of testing')
def test_try_to_enter_with_a_new_password(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    assert login_page.check_that_remember_me_box_is_selected()
    login_page.enter_login_data(email=settings.email, password=settings.new_password)
    home_page = HomePage(driver)
    assert home_page.check_that_username_is_displayed_in_the_welcome_block


