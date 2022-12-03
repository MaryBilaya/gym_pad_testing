from pages.exercise_page import ExercisePage
import pytest
import settings
from time import sleep

CREDENTIALS = [
    {'exercise_name': 'Ходьба на улице', 'type': 'Расстояние (км)'},
    {'exercise_name': 'HIIT', 'type': 'Кардио (мин)'}]


def test_open_description_of_a_specific_exercise(driver, login):  # check
    exercise_page = ExercisePage(driver)
    exercise_page.open_an_exercise_page()
    exercise_page.open_description_of_a_specific_exercise()
    assert exercise_page.check_that_exercise_description_is_displayed()


def test_open_statistics_of_exercise(driver, login):  # check (ATTENTION)
    exercise_page = ExercisePage(driver)
    exercise_page.open_an_exercise_page()
    exercise_page.open_description_of_a_specific_exercise()
    exercise_page.open_statistics_of_exercise()


def test_open_history_of_exercise(driver, login):  # check (ATTENTION)
    exercise_page = ExercisePage(driver)
    exercise_page.open_an_exercise_page()
    exercise_page.open_description_of_a_specific_exercise()
    exercise_page.open_history_of_exercise()


@pytest.mark.parametrize('creds', CREDENTIALS)
def test_add_a_personal_exercise(driver, login, creds):
    exercise_page = ExercisePage(driver)
    exercise_page.open_an_exercise_page()
    exercise_page.add_a_personal_exercise(personal_ex=creds['exercise_name'])
    assert exercise_page.check_pop_up_message_that_a_personal_exercise_was_added()


@pytest.mark.parametrize('creds', CREDENTIALS)
def test_setting_a_personal_exercise(driver, login, creds):
    exercise_page = ExercisePage(driver)
    exercise_page.open_an_exercise_page()
    exercise_page.add_a_personal_exercise(personal_ex=creds['exercise_name'])
    exercise_page.setting_a_personal_exercise(type_of_ex=creds['type'])
    assert exercise_page.check_pop_up_message_that_a_personal_exercise_was_saved()


def test_delete_a_personal_exercise(driver, login):
    exercise_page = ExercisePage(driver)
    exercise_page.open_an_exercise_page()
    exercise_page.add_a_personal_exercise()
    exercise_page.delete_a_personal_exercise()


def test_cancel_deletion_of_a_personal_exercise(driver, login):
    exercise_page = ExercisePage(driver)
    exercise_page.open_an_exercise_page()
    exercise_page.add_a_personal_exercise()
    exercise_page.cancel_deletion_of_a_personal_exercise()





