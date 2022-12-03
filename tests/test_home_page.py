from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from pages.food_diary_page import FoodDiary
from pages.exercise_page import ExercisePage
import settings
from time import sleep


def test_go_to_the_registration_page(driver):  # check
    home_page = HomePage(driver)
    home_page.open_home_page()
    sleep(3)  # for demonstration purposes
    home_page.go_to_the_registration_page()
    registration_page = RegistrationPage(driver)
    assert registration_page.check_that_jump_to_the_registration_page_was_completed


def test_go_to_the_login_page(driver):  # check
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.go_to_the_login_page()
    login_page = LoginPage(driver)
    assert login_page.check_that_jump_to_the_login_page_was_completed


def test_all_days_of_the_month_workout_are_displayed(driver, login):  # check
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.show_all_days_of_the_month_workout()
    sleep(3)  # for demonstration purposes
    assert home_page.check_that_all_dates_of_the_month_are_displayed()


def test_open_the_block_of_exercises(driver, login):  # check
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.show_all_days_of_the_month_workout()
    home_page.scroll_the_page_to_the_bottom()
    home_page.open_the_block_of_exercises()
    assert home_page.check_that_the_window_of_exercises_were_opened()


# def test_adding_exercises(driver, login):  # check
#     home_page = HomePage(driver)
#     home_page.open_home_page()
#     home_page.show_all_days_of_the_month_workout()
#     home_page.adding_exercises()


def test_go_to_the_catalog_of_exercises_page(driver, login):  # check
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.go_to_the_catalog_of_exercises_page()
    sleep(3)  # for demonstration purposes
    exercise_page = ExercisePage(driver)
    assert exercise_page.check_exercise_page_title


def test_a_food_diary(driver, login):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.click_a_food_diary_link()
    sleep(3)    # for demonstration purposes
    food_diary = FoodDiary(driver)
    assert food_diary.check_food_diary_page_title


def test_notes_link(driver, login):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.click_notes_link()
    sleep(3)  # for demonstration purposes
    notes_page = NotesPage(driver)
    assert notes_page.check_notes_page_title


def test_profile_dropdown_settings(driver, login):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.profile_dropdown_settings()


def test_profile_dropdown_exit(driver, login):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.profile_dropdown_exit()
    assert home_page.check_that_login_button_is_displayed()







