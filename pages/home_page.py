import settings
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

reg_btn_at_the_top_of_the_page = (By.XPATH, '//a[@id="btn-reg" and @class="btn"]')  # check
redirecting_reg_btn = (By.XPATH, '//a[@class="cta priceBg4" and @data-action="pulse"]')  # check
welcome_block = (By.CSS_SELECTOR, 'span[class="hidden-xs"]')  # check
select_welcome_block = (By.CLASS_NAME, 'dropdown-toggle')
login_button = (By.XPATH, '//a[@class="btn" and @style="font-size: 12px"]')  # check
training_log_button = (By.CLASS_NAME, 'navLabel ')
all_menu = (By.CLASS_NAME, 'navLabel ')  # check
rec_workout_2_december = (By.CSS_SELECTOR, 'button[onclick="page_workout.create(2)"]')  # check
plus_workout_2_december = (By.CSS_SELECTOR, 'a[class="exerciseName new hint--right hint--always"]')  # check
save_workout_2_december = (By.CSS_SELECTOR, 'button[onclick="page_workout.save(2)"]')  # check
exercise_selection_window = (By.ID, 'modalExercisesContent')  # check
list_of_exercises_in_the_selection_window = (By.CLASS_NAME, 'panel-heading')  # check
show_only_active_days_box = (By.CSS_SELECTOR, 'label[for="showOnlyActive"]')  # check
all_days_of_the_month_block = (By.CSS_SELECTOR, 'div[class="main-box-body clearfix"]')  # check
tables_of_exercise_options = (By.CSS_SELECTOR, 'table[class="table table-condensed"]')
press_ex_1 = (By.XPATH, '//input[@id="checkbox3b3517c4e2b05ed02a5898aff988e529" and @type="checkbox"]')

profile_block = (By.CLASS_NAME, 'profile-dropdown')
profile_menu_settings = (By.CSS_SELECTOR, 'a[href="/settings"]')
profile_menu_exit = (By.CSS_SELECTOR, 'a[href="/logout"]')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):  # check
        self.driver.get(self.base_url)

    def go_to_the_registration_page(self):  # check
        self.find_element(reg_btn_at_the_top_of_the_page).click()
        self.find_element(redirecting_reg_btn).click()
        sleep(3)    # for demonstration purposes

    @property
    def check_that_username_is_displayed_in_the_welcome_block(self):  # check
        welcome_phrase = self.find_element(welcome_block).text
        return settings.first_name in welcome_phrase

    def go_to_the_login_page(self):  # check
        self.find_element(login_button).click()
        sleep(3)  # for demonstration purposes

    def show_all_days_of_the_month_workout(self):  # check
        self.find_element(show_only_active_days_box).click()

    def check_that_all_dates_of_the_month_are_displayed(self):  # check
        return self.find_element(all_days_of_the_month_block).is_displayed()

    def open_the_block_of_exercises(self):  # check
        record_btn = self.find_elements(rec_workout_2_december)
        record_btn[1].click()
        plus_btn = self.find_element(plus_workout_2_december).click()
        sleep(3)  # for demonstration purposes

    def check_that_the_window_of_exercises_were_opened(self):  # check
        return self.find_element(exercise_selection_window).is_displayed()

    # def adding_exercises(self):
    #     record_btn = self.find_elements(rec_workout_2_december)
    #     record_btn[1].click()
    #     plus_btn = self.find_element(plus_workout_2_december).click()
    #     list_of_exercises = self.find_elements(list_of_exercises_in_the_selection_window)
    #     press_btn = list_of_exercises[8].click()
    #     sleep(5)  # for demonstration purposes

    def go_to_the_catalog_of_exercises_page(self):  # check
        catalog_of_exercises = self.find_elements(all_menu)
        catalog_of_exercises[2].click()

    def click_a_food_diary_link(self):
        food_diary = self.find_elements(all_menu)
        food_diary[4].click()

    def click_notes_link(self):
        food_diary = self.find_elements(all_menu)
        food_diary[8].click()

    def profile_dropdown_settings(self):
        profile = self.find_element(profile_block).click()
        sleep(3)  # for demonstration purposes
        menu_settings = self.find_element(profile_menu_settings).click()
        sleep(3)  # for demonstration purposes

    def profile_dropdown_exit(self):
        profile = self.find_element(profile_block).click()
        sleep(3)  # for demonstration purposes
        menu_exit = self.find_element(profile_menu_exit).click()
        sleep(3)  # for demonstration purposes

    def check_that_login_button_is_displayed(self):
        return self.find_element(login_button).is_displayed()


























