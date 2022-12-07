from selenium.webdriver.common.by import By
from pages.locators import home_page_locators as hpl
import settings
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

select_welcome_block = (By.CLASS_NAME, 'dropdown-toggle')
training_log_button = (By.CLASS_NAME, 'navLabel ')
save_workout_in_december = (By.CSS_SELECTOR, 'button[onclick="page_workout.save(11)"]')  # check
tables_of_exercise_options = (By.CSS_SELECTOR, 'table[class="table table-condensed"]')
add_exercise_button = (By.CSS_SELECTOR, 'button[class="btn btn-orange btn-item-add"]')
add_an_exercise_approach_btn = (By.CSS_SELECTOR, 'a[class="workoutSet new"]')
kg_field = (By.CSS_SELECTOR, 'input[placeholder="кг"]')
approach_field = (By.CSS_SELECTOR, 'input[placeholder="повторения"]')
all_done_btn = (By.CSS_SELECTOR, 'button[class="btn btn-orange btn-set-save"]')
next_btn = (By.CSS_SELECTOR, 'button[class="btn btn-default btn-set-next"]')
drop_down_exercise_btn = (By.XPATH, '//button[@data-toggle="dropdown" and @aria-expanded="true"]')
#save_drop_down_btn = (By.CSS_SELECTOR, 'a[href="javascript:page_workout.save(5)"]')
profile_menu_settings = (By.CSS_SELECTOR, 'a[href="/settings"]')
displayed_comment = (By.CSS_SELECTOR, 'a[class="comment"]')
add_new_exercise_btn = (By.CSS_SELECTOR, 'i[class="glyphicon glyphicon-plus"]')
# save_btn = (By.CSS_SELECTOR, 'button[data-loading-text="Сохраняем"]')
save_btn = (By.XPATH, '//button[@type="button" and @data-loading-text="Сохраняем"]')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.driver.get(self.base_url)

    def go_to_the_registration_page(self):  # check
        self.find_element(hpl.reg_btn_at_the_top_of_the_page).click()
        self.find_element(hpl.redirecting_reg_btn).click()

    @property
    def check_that_username_is_displayed_in_the_welcome_block(self):  # check
        welcome_phrase = self.find_element(hpl.welcome_block).text
        return settings.first_name in welcome_phrase

    def go_to_the_login_page(self):  # check
        self.find_element(hpl.login_button).click()

    def show_all_days_of_the_month_workout(self):  # check
        self.find_element(hpl.show_only_active_days_box).click()

    def check_that_all_dates_of_the_month_are_displayed(self):  # check
        return self.find_element(hpl.all_days_of_the_month_block).is_displayed()

    def open_the_block_of_exercises(self):  # check
        record_btn = self.find_elements(hpl.rec_workout_in_december)
        record_btn[1].click()
        plus_btn = self.find_element(hpl.plus_workout_in_december).click()
        sleep(3)  # for demonstration purposes

    def check_that_the_window_of_exercises_was_opened(self):  # check
        return self.find_element(hpl.exercise_selection_window).is_displayed()

    def adding_exercise(self):  # check
        self.scroll_the_page_to_the_bottom()
        sleep(3)  # for demonstration purposes
        list_of_exercises = self.find_elements(hpl.list_of_exercises_in_the_selection_window)
        biceps_btn = list_of_exercises[2].click()
        sleep(3)  # for demonstration purposes
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element(hpl.biceps_ex, 'Сгибание рук со штангой'))
        self.find_element(hpl.biceps_ex).click()
        self.find_element(add_exercise_button).click()
        self.scroll_the_page_to_the_middle()
        sleep(3)  # for demonstration purposes

    def check_that_selected_exercise_was_displayed(self):  # check
        return self.find_element(hpl.displayed_exercise).is_displayed()

    def add_an_exercise_approach(self):  # ATTENTION
        self.scroll_the_page_to_the_middle()
        self.find_element(add_an_exercise_approach_btn).click()
        kg = self.find_element(kg_field)
        kg.send_keys('40')
        sleep(3)  # for demonstration purposes
        approach = self.find_element(approach_field)
        approach.send_keys('3')
        sleep(3)  # for demonstration purposes
        self.find_element(next_btn).click()
        kg.clear()
        kg.send_keys('50')
        sleep(3)  # for demonstration purposes
        approach.clear()
        approach.send_keys('2')
        self.find_element(all_done_btn).click()
        sleep(3)  # for demonstration purposes
        # wait = WebDriverWait(self.driver, 20)
        # wait.until(EC.element_to_be_clickable(save_btn))
        self.find_element(save_btn).click()
        # execute = (JavascriptExecutor)self.driver
        # executor.executeScript("arguments[0].click();", save)
        # wait = WebDriverWait(self.driver, 20)
        # wait.until(EC.visibility_of_element_located(save_btn))
        # self.find_element(save_btn).click()
        # wait = WebDriverWait(self.driver, 20)
        # # save_btn = self.find_element(save_workout_in_december)
        # wait.until(EC.element_to_be_clickable(save_workout_in_december))
        # self.find_element(save_workout_in_december).click()

    def check_that_an_exercise_approaches_were_added(self):
        pass

    def add_a_comment_to_the_exercise(self): # check
        self.find_element(hpl.comment_to_the_exercise).click()
        self.find_element(hpl.comment_field).send_keys('Увеличить вес в следующий раз')
        sleep(3)    # for demonstration purposes
        self.find_element(hpl.comment_done).click()

    def check_that_added_comment_was_displayed(self):  # check
        return self.find_element(displayed_comment).is_displayed()

    def remove_the_selected_exercise(self):
        self.find_element(hpl.displayed_exercise).click()
        sleep(3)  # for demonstration purposes
        self.find_element(hpl.remove_an_exercise).click()
        sleep(3)  # for demonstration purposes

    def check_removal_of_exercise(self):
        pass

    def go_to_the_catalog_of_exercises_page(self):  # check
        catalog_of_exercises = self.find_elements(hpl.all_menu)
        catalog_of_exercises[2].click()

    def go_to_the_food_diary_page(self):  # check
        food_diary = self.find_elements(hpl.all_menu)
        food_diary[4].click()

    def go_to_the_body_param_page(self):  # check
        food_diary = self.find_elements(hpl.all_menu)
        food_diary[5].click()

    def check_that_jump_to_the_body_param_page_was_completed(self):
        body_param_url = self.driver.current_url
        return 'https://www.gympad.ru/bodyparams' == body_param_url

    def go_to_the_notes_page(self):  # check
        food_diary = self.find_elements(hpl.all_menu)
        food_diary[8].click()

    def check_that_jump_to_the_notes_page_was_completed(self):  # check
        notes_url = self.driver.current_url
        return 'https://www.gympad.ru/notes' == notes_url

    def profile_dropdown_settings(self):
        profile = self.find_element(hpl.profile_block).click()
        sleep(3)  # for demonstration purposes
        menu_settings = self.find_element(hpl.profile_menu_settings).click()
        sleep(3)  # for demonstration purposes

    def profile_dropdown_exit(self):
        profile = self.find_element(hpl.profile_block).click()
        sleep(3)  # for demonstration purposes
        menu_exit = self.find_element(hpl.profile_menu_exit).click()
        sleep(3)  # for demonstration purposes

    def check_that_login_button_is_displayed(self):
        return self.find_element(hpl.login_button).is_displayed()


























