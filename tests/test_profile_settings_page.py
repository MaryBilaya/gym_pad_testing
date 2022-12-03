from pages.profile_settings_page import ProfileSettings
from pages.login_page import LoginPage
import settings
from time import sleep
import pytest


def test_the_correct_user_data_is_displayed(driver, login):
    profile_settings_page = ProfileSettings(driver)
    profile_settings_page.open_profile_setting_page()
    assert profile_settings_page.check_that_the_first_name_field_is_filled_in()
    assert profile_settings_page.check_the_last_name_field_is_filled_in()
    assert profile_settings_page.check_the_email_field_is_filled_in()


def test_add_additional_user_info(driver, login):
    profile_settings_page = ProfileSettings(driver)
    profile_settings_page.open_profile_setting_page()
    profile_settings_page.add_additional_user_info()
    profile_settings_page.scroll_the_page_to_the_middle()
    sleep(3)    # for demonstration purposes
    assert profile_settings_page.check_that_font_of_popup_message_has_a_necessary_color()


@pytest.mark.skip('Run only at the end of testing')
def test_change_existing_password(driver, login):
    profile_settings_page = ProfileSettings(driver)
    profile_settings_page.open_profile_setting_page()
    profile_settings_page.change_existing_password()
    assert profile_settings_page.check_that_font_of_popup_message_has_a_necessary_color()


@pytest.mark.skip('Run only at the end of testing')
def test_change_incorrect_password(driver, login):
    profile_settings_page = ProfileSettings(driver)
    profile_settings_page.open_profile_setting_page()
    profile_settings_page.try_to_change_incorrect_password()
    sleep(3)    # for demonstration purposes
    assert profile_settings_page.check_that_help_message_is_appeared()




