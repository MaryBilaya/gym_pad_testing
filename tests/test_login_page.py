import settings
from time import sleep
from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_enter_correct_login_data(driver):  # check
    login_page = LoginPage(driver)
    login_page.open_login_page()
    assert login_page.check_that_remember_me_box_is_selected()
    login_page.enter_login_data(email=settings.email, password=settings.password)
    home_page = HomePage(driver)
    assert home_page.check_that_username_is_displayed_in_the_welcome_block


def test_login_with_incorrect_password(driver):  # check
    login_page = LoginPage(driver)
    login_page.open_login_page()
    assert login_page.check_that_remember_me_box_is_selected()
    login_page.enter_login_data(email=settings.email, password='qwerty')
    assert login_page.check_alert_message_after_login_with_incorrect_password()


def test_login_with_incorrect_email(driver):  # check
    login_page = LoginPage(driver)
    login_page.open_login_page()
    assert login_page.check_that_remember_me_box_is_selected()
    login_page.enter_login_data(email='mistake@mail.ru', password=settings.password)
    login_page.check_alert_message_after_login_with_incorrect_email()


def test_forget_password_link_is_present_on_the_page(driver):  # check
    login_page = LoginPage(driver)
    login_page.open_login_page()
    assert login_page.check_that_forget_password_link_is_present_on_the_login_page()


