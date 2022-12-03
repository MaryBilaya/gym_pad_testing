from pages.registration_page import RegistrationPage
from pages.home_page import HomePage
import settings
from time import sleep


def test_with_correct_registration_data(driver):  # check
    reg_page = RegistrationPage(driver)
    reg_page.open_registration_page()
    reg_page.enter_correct_registration_data(email=settings.email,
                                             first_name=settings.first_name,
                                             password=settings.password,
                                             last_name=settings.last_name)
    sleep(3)    # for demonstration purposes
    home_page = HomePage(driver)
    assert home_page.check_that_username_is_displayed_in_the_welcome_block


def test_alert_message_after_registration_with_the_same_email(driver):  # check
    reg_page = RegistrationPage(driver)
    reg_page.open_registration_page()
    reg_page.enter_correct_registration_data(email=settings.email,
                                             first_name=settings.first_name,
                                             password=settings.password,
                                             last_name=settings.last_name)
    sleep(3)    # for demonstration purposes
    assert reg_page.check_alert_message_after_registration_with_the_same_email()

