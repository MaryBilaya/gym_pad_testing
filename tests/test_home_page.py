from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.food_diary_page import FoodDiary
from pages.exercise_page import ExercisePage
import pytest
import allure
from time import sleep


@allure.feature('Registration')
@pytest.mark.registration
def test_go_to_the_registration_page(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.go_to_the_registration_page()
    registration_page = RegistrationPage(driver)
    assert registration_page.check_that_jump_to_the_registration_page_was_completed


@allure.feature('Login')
@pytest.mark.login
def test_go_to_the_login_page(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.go_to_the_login_page()
    login_page = LoginPage(driver)
    assert login_page.check_that_jump_to_the_login_page_was_completed


@allure.feature('Home')
@pytest.mark.home
def test_all_days_of_the_month_workout_are_displayed(driver, login):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.show_all_days_of_the_month_workout()
    sleep(3)    # for demonstration purposes
    assert home_page.check_that_all_dates_of_the_month_are_displayed()


@allure.feature('Home')
@pytest.mark.home
def test_open_the_block_of_exercises(driver, login):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.show_all_days_of_the_month_workout()
    home_page.scroll_the_page_to_the_bottom()
    home_page.open_the_block_of_exercises()
    assert home_page.check_that_the_window_of_exercises_was_opened()


@allure.feature('Home')
@pytest.mark.home
def test_adding_exercise(driver, login):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.show_all_days_of_the_month_workout()
    home_page.open_the_block_of_exercises()
    home_page.adding_exercise()
    assert home_page.check_that_selected_exercise_was_displayed()


@allure.feature('Home')
def test_add_an_exercise_approach(driver, login):  # ATTENTION
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.show_all_days_of_the_month_workout()
    home_page.adding_exercise()
    home_page.add_an_exercise_approach()


@allure.feature('Home')
@pytest.mark.home
def test_add_a_comment_to_the_exercise(driver, login):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.show_all_days_of_the_month_workout()
    home_page.open_the_block_of_exercises()
    home_page.adding_exercise()
    home_page.add_a_comment_to_the_exercise()
    assert home_page.check_that_added_comment_was_displayed()


@allure.feature('Home')
def test_remove_the_selected_exercise(driver, login):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.show_all_days_of_the_month_workout()
    home_page.open_the_block_of_exercises()
    home_page.adding_exercise()
    home_page.remove_the_selected_exercise()
    assert home_page.check_removal_of_exercise()


@allure.feature('Home')
def test_go_to_the_catalog_of_exercises_page(driver, login):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.go_to_the_catalog_of_exercises_page()
    sleep(3)  # for demonstration purposes
    exercise_page = ExercisePage(driver)
    assert exercise_page.check_exercise_page_title


@allure.feature('Home')
def test_go_to_the_food_diary_page(driver, login):  # check
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.go_to_the_food_diary_page()
    sleep(3)    # for demonstration purposes
    food_diary = FoodDiary(driver)
    assert food_diary.check_food_diary_page_title


@allure.feature('Home')
def test_go_to_the_body_param_page(driver, login):  # check
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.go_to_the_body_param_page()
    sleep(3)  # for demonstration purposes
    assert home_page.check_that_jump_to_the_body_param_page_was_completed()


@allure.feature('Home')
def test_go_to_the_notes_page(driver, login):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.go_to_the_notes_page()
    sleep(3)  # for demonstration purposes
    assert home_page.check_that_jump_to_the_notes_page_was_completed()


@allure.feature('Home')
def test_profile_dropdown_settings(driver, login):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.profile_dropdown_settings()


@allure.feature('Home')
@pytest.mark.logout
# @pytest.mark.skip('Run only at the end of testing')
def test_profile_dropdown_exit(driver, login):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.profile_dropdown_exit()
    assert home_page.check_that_login_button_is_displayed()







