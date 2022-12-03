from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

exercise_page_title = (By.CLASS_NAME, 'col-lg-12')  # check
exercise_catalog = (By.CLASS_NAME, 'panel-title')  # check
press_ex1 = (By.PARTIAL_LINK_TEXT, 'Подъемы коленей в висе')  # check
press_description = (By.CSS_SELECTOR, 'div[id="exerciseDetails"]')  # check
description_statistics_btn = (By.LINK_TEXT, 'Статистика')  # check
description_history_btn = (By.LINK_TEXT, 'История')  # check
oneself_exercises = (By.PARTIAL_LINK_TEXT, 'Мои')  # check
new_exercise_field = (By.CSS_SELECTOR, 'input[placeholder="Новое упражнение"]')  # check
add_new_exercise_button = (By.CSS_SELECTOR, 'button[class="btn btn-orange btn-block"]')  # check
# new_exercise_details = (By.CSS_SELECTOR, 'div[class="main-box clearfix"]')
type_of_exercise_field = (By.CSS_SELECTOR, 'select[class="form-control"]')  # check
# name_of_exercise_field = (By.CSS_SELECTOR, 'input[class="form-control"]')
save_exercise_details = (By.CSS_SELECTOR, 'button[class="btn btn-orange pull-right"]')  # check
delete_exercise = (By.ID, 'removeExercise')
yes_delete_exercise = (By.CSS_SELECTOR, 'button[class="btn btn-default"]')
no_delete_exercise = (By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
pop_up_message = (By.CSS_SELECTOR, 'div[class="sticky-queue top-right"]')  # check


class ExercisePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_an_exercise_page(self):
        self.driver.get(self.exercise_url)

    @property
    def check_exercise_page_title(self):  # check
        exercise_title = self.find_elements(exercise_page_title)
        exercise_title_text = exercise_title[1].text
        return 'Упражнения' in exercise_title_text

    def open_description_of_a_specific_exercise(self):  # check
        catalog_of_exercises = self.find_elements(exercise_catalog)
        press_btn = catalog_of_exercises[8].click()
        self.scroll_the_page_to_the_middle()
        ex = self.find_element(press_ex1).click()
        sleep(3)  # for demonstration purposes

    def check_that_exercise_description_is_displayed(self):  # check
        return self.find_element(press_description).is_displayed()

    def open_statistics_of_exercise(self):  # check
        statistics_btn = self.find_elements(description_statistics_btn)
        statistics_btn[1].click()
        sleep(3)  # for demonstration purposes

    def open_history_of_exercise(self):  # check
        history_btn = self.find_element(description_history_btn).click()
        sleep(3)  # for demonstration purposes

    def add_a_personal_exercise(self, personal_ex):  # check
        self.find_element(oneself_exercises).click()
        self.find_element(new_exercise_field).send_keys(personal_ex)
        self.find_element(add_new_exercise_button).click()

    def check_pop_up_message_that_a_personal_exercise_was_added(self):  # check
        wait = WebDriverWait(self.driver, 10)
        wait.until((EC.invisibility_of_element_located(pop_up_message)),
                   message='pop-up message "exercise added" did not appear')
        return True

    def setting_a_personal_exercise(self, type_of_ex):  # check
        select = Select(self.find_element(type_of_exercise_field))
        select.select_by_visible_text(type_of_ex)
        sleep(3)  # for demonstration purposes
        save = self.find_element(save_exercise_details).click()

    # def check_that_field_of_personal_exercise_name_is_filled_in(self):  # check
    #     name = self.find_elements(name_of_exercise_field)
    #     name_value = name[1].get_attribute('value')
    #     return 'Ходьба на улице' in name_value

    def check_pop_up_message_that_a_personal_exercise_was_saved(self):  # check
        wait = WebDriverWait(self.driver, 10)
        wait.until((EC.invisibility_of_element_located(pop_up_message)),
                   message='pop-up message "saved" did not appear')
        return True

    def delete_a_personal_exercise(self):
        delete_btn = self.find_element(delete_exercise).click()
        self.find_element(yes_delete_exercise).click()

    def cancel_deletion_of_a_personal_exercise(self):
        delete_btn = self.find_element(delete_exercise).click()
        self.find_element(no_delete_exercise).click()






