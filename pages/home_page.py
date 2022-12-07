from selenium.common.exceptions import NoSuchElementException
from pages.locators import home_page_locators as hpl
import settings
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.driver.get(self.base_url)

    def go_to_the_registration_page(self):
        self.find_element(hpl.reg_btn_at_the_top_of_the_page).click()
        self.find_element(hpl.redirecting_reg_btn).click()

    @property
    def check_that_username_is_displayed_in_the_welcome_block(self):
        welcome_phrase = self.find_element(hpl.welcome_block).text
        return settings.first_name in welcome_phrase

    def go_to_the_login_page(self):
        self.find_element(hpl.login_button).click()

    def show_all_days_of_the_month_workout(self):
        self.find_element(hpl.show_only_active_days_box).click()

    def check_that_all_dates_of_the_month_are_displayed(self):
        return self.find_element(hpl.all_days_of_the_month_block).is_displayed()

    def open_the_block_of_exercises(self):
        record_btn = self.find_elements(hpl.rec_workout_2_december)
        record_btn[1].click()
        plus_btn = self.find_element(hpl.plus_workout_in_december).click()
        sleep(3)  # for demonstration purposes

    def check_that_the_window_of_exercises_was_opened(self):
        return self.find_element(hpl.exercise_selection_window).is_displayed()

    def adding_an_exercise_to_the_workout(self):
        self.scroll_the_page_to_the_bottom()
        sleep(3)  # for demonstration purposes
        list_of_exercises = self.find_elements(hpl.list_of_exercises_in_the_selection_window)
        biceps_btn = list_of_exercises[2].click()
        sleep(3)  # for demonstration purposes
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element(hpl.biceps_ex, 'Сгибание рук со штангой'))
        self.find_element(hpl.biceps_ex).click()
        self.find_element(hpl.add_exercise_button).click()
        self.scroll_the_page_to_the_bottom()
        sleep(3)  # for demonstration purposes

    def check_that_selected_exercise_was_displayed(self):
        return self.find_element(hpl.displayed_exercise_biceps).is_displayed()

    def add_an_exercise_approach(self):
        self.find_element(hpl.add_an_exercise_approach_btn).click()
        kg = self.find_element(hpl.kg_field)
        kg.send_keys('40')
        approach = self.find_element(hpl.approach_field)
        approach.send_keys('3')
        sleep(3)  # for demonstration purposes
        self.find_element(hpl.next_btn).click()
        kg.clear()
        kg.send_keys('50')
        approach.clear()
        approach.send_keys('2')
        self.find_element(hpl.all_done_btn).click()
        sleep(3)  # for demonstration purposes
        self.driver.execute_script('javascript:page_workout.save(2)')

    def check_that_an_exercise_approaches_were_added(self):
        text_message = self.find_element(hpl.training_tonnage_message).text
        return 'Тоннаж тренировки:' in text_message

    def add_a_comment_to_the_exercise(self):
        record_btn = self.find_elements(hpl.rec_workout_3_december)
        record_btn[1].click()
        plus_btn = self.find_element(hpl.plus_workout_in_december).click()
        list_of_exercises = self.find_elements(hpl.list_of_exercises_in_the_selection_window)
        biceps_btn = list_of_exercises[2].click()
        wait = WebDriverWait(self.driver, 40)
        wait.until(EC.text_to_be_present_in_element(hpl.biceps_ex, 'Сгибание рук со штангой'))
        self.find_element(hpl.biceps_ex).click()
        self.find_element(hpl.add_exercise_button).click()
        sleep(3)  # for demonstration purposes
        self.find_element(hpl.comment_to_the_exercise).click()
        self.find_element(hpl.comment_field).send_keys('Увеличить вес в следующий раз')
        sleep(3)    # for demonstration purposes
        self.find_element(hpl.comment_done).click()

    def check_that_added_comment_was_displayed(self):
        return self.find_element(hpl.displayed_comment).is_displayed()

    def remove_the_selected_exercise(self):
        record_btn = self.find_elements(hpl.rec_workout_4_december)
        record_btn[1].click()
        plus_btn = self.find_element(hpl.plus_workout_in_december).click()
        list_of_exercises = self.find_elements(hpl.list_of_exercises_in_the_selection_window)
        biceps_btn = list_of_exercises[2].click()
        wait = WebDriverWait(self.driver, 40)
        wait.until(EC.text_to_be_present_in_element(hpl.biceps_ex, 'Сгибание рук со штангой'))
        self.find_element(hpl.biceps_ex).click()
        self.find_element(hpl.add_exercise_button).click()
        sleep(3)  # for demonstration purposes
        self.find_element(hpl.displayed_exercise_biceps).click()
        sleep(3)  # for demonstration purposes
        wait = WebDriverWait(self.driver, 40)
        wait.until(EC.text_to_be_present_in_element(hpl.remove_an_exercise, 'Убрать упражнение из тренировки'))
        self.find_element(hpl.remove_an_exercise).click()

    def check_removal_of_exercise(self):
        try:
            self.find_element(hpl.displayed_exercise_biceps)
        except NoSuchElementException:
            return True

    def go_to_the_catalog_of_exercises_page(self):
        catalog_of_exercises = self.find_elements(hpl.all_menu)
        catalog_of_exercises[2].click()

    def go_to_the_food_diary_page(self):
        food_diary = self.find_elements(hpl.all_menu)
        food_diary[4].click()

    def go_to_the_body_param_page(self):
        food_diary = self.find_elements(hpl.all_menu)
        food_diary[5].click()

    def check_that_jump_to_the_body_param_page_was_completed(self):
        body_param_url = self.driver.current_url
        return 'https://www.gympad.ru/bodyparams' == body_param_url

    def go_to_the_notes_page(self):
        food_diary = self.find_elements(hpl.all_menu)
        food_diary[8].click()

    def check_that_jump_to_the_notes_page_was_completed(self):
        notes_url = self.driver.current_url
        return 'https://www.gympad.ru/notes' == notes_url

    def profile_dropdown_settings(self):
        profile = self.find_element(hpl.profile_block).click()
        menu_settings = self.find_element(hpl.profile_menu_settings).click()
        sleep(3)  # for demonstration purposes

    def check_that_profile_settings_were_opened(self):
        settings_title = self.find_element(hpl.profile_settings_title).text
        return 'Настройки' in settings_title

    def profile_dropdown_exit(self):
        profile = self.find_element(hpl.profile_block).click()
        menu_exit = self.find_element(hpl.profile_menu_exit).click()
        sleep(3)  # for demonstration purposes

    def check_that_login_button_is_displayed(self):
        return self.find_element(hpl.login_button).is_displayed()


























