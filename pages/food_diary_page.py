from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

food_diary_page_title = (By.CLASS_NAME, 'col-lg-12')
november_28 = (By.LINK_TEXT, '28')
name_of_food = (By.ID, 'nutInput')
list_of_yoghurt = (By.CLASS_NAME, 'tt-highlight')
add_food_button = (By.ID, 'nutSubmit')
total_calories_field = (By.ID, 'totalCalories')
day_info = (By.CLASS_NAME, 'col-lg-12')
weight_field = (By.ID, 'nutWeightInput')
gym_pad_home = (By.CSS_SELECTOR, 'img[alt="GymPad"]')
food_diary_title = (By.CLASS_NAME, 'col-lg-12')
month_name_field = (By.CLASS_NAME, 'monthList ')
month_left_btn = (By.ID, 'calendarLeft')
month_right_btn = (By.ID, 'calendarRight')


class FoodDiary(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_food_diary_page(self):
        self.driver.get(self.food_diary_url)

    @property
    def check_food_diary_page_title(self):
        diary_title = self.find_elements(food_diary_title)
        diary_title_text = diary_title[1].text
        return 'Дневник питания' in diary_title_text

    def fill_in_a_food_diary(self, product, weight, choice):
        nov_28 = self.find_element(november_28).click()
        product_name = self.find_element(name_of_food).send_keys(product)
        my_product = self.find_elements(list_of_yoghurt)
        ActionChains(self.driver).move_to_element(my_product[choice]).click().perform()
        sleep(3)  # for demonstration purposes
        self.find_element(weight_field).send_keys(weight)
        self.scroll_the_page_to_the_middle()
        sleep(3)    # for demonstration purposes
        self.find_element(add_food_button).click()

    def check_that_field_total_calories_are_changed(self):
        info = self.find_element(total_calories_field).text
        return info != 0

    def check_that_the_28_of_november_is_chosen(self):
        nov_28 = self.find_element(november_28).click()
        day_info_field = self.find_elements(day_info)
        day_text = day_info_field[1].get_attribute('innerText')
        return 'Дневник питания. Сегодня' in day_text

    def click_gym_pad_home(self):
        self.find_element(gym_pad_home).click()

    def check_that_month_name_is_november(self):
        month_name = self.find_element(month_name_field)
        month_name_text = month_name.get_attribute('innerText')
        return 'ноябрь 2022' in month_name_text

    def change_month_names(self):
        self.find_element(month_left_btn).click()
        sleep(3)    # for demonstration purposes
        self.find_element(month_right_btn).click()
        sleep(3)  # for demonstration purposes






