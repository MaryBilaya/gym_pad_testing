import pytest
from pages.home_page import HomePage
from pages.food_diary_page import FoodDiary
from pages.login_page import LoginPage
import settings

CREDENTIALS = [
    {'product': 'Йогурт', 'choice': 3, 'weight': 150},
    {'product': 'Куриная грудка', 'choice': 1, 'weight': 100},
    {'product': 'Брокколи', 'choice': 4, 'weight': 170}]


@pytest.mark.parametrize('creds', CREDENTIALS)
def test_fill_in_a_food_diary(driver, login, creds):
    # login_page = LoginPage(driver)
    # login_page.open_login_page()
    # login_page.enter_login_details(email=settings.email, password=settings.password)
    # login_page.click_login_button()
    food_diary = FoodDiary(driver)
    food_diary.open_food_diary_page()
    food_diary.fill_in_a_food_diary(product=creds['product'],
                                    choice=creds['choice'],
                                    weight=creds['weight'])
    # assert food_diary.check_that_the_28_of_november_is_chosen()
    assert food_diary.check_that_field_total_calories_are_changed()
    food_diary.click_gym_pad_home()


def test_calendar(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.enter_login_details(email=settings.email, password=settings.password)
    login_page.click_login_button()
    food_diary = FoodDiary(driver)
    food_diary.open_food_diary_page()
    food_diary.check_that_month_name_is_november()


def test_calendar_months(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.enter_login_details(email=settings.email, password=settings.password)
    login_page.click_login_button()
    food_diary = FoodDiary(driver)
    food_diary.open_food_diary_page()
    food_diary.change_month_names()
