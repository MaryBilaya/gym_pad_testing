import settings
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

first_name_field = (By.NAME, 'User[first_name]')
last_name_field = (By.NAME, 'User[last_name]')
email_field = (By.NAME, 'User[email]')
femail_box = (By.CSS_SELECTOR, 'label[for="female"]')
birth_date = (By.NAME, 'User[birthday]')
save_info_btn = (By.CSS_SELECTOR, 'button[class="btn btn-orange ml10"]')
popup_saved_message = (By.ID, 'back-top')
old_password_field = (By.NAME, 'User[old_password]')
new_password_field = (By.NAME, 'User[new_password]')
new_repeat_password = (By.NAME, 'User[new_repeat_password]')
help_block_message = (By.CSS_SELECTOR, 'span[class="help-block red"]')


class ProfileSettings(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_profile_setting_page(self):
        self.driver.get(self.profile_settings_url)

    def check_that_the_first_name_field_is_filled_in(self):
        first_name = self.find_element(first_name_field)
        first_name_value = first_name.get_attribute('value')
        return f'{settings.name}' in first_name_value

    def check_the_last_name_field_is_filled_in(self):
        last_name = self.find_element(last_name_field)
        last_name_value = last_name.get_attribute('value')
        return f'{settings.last_name}' in last_name_value

    def check_the_email_field_is_filled_in(self):
        email = self.find_element(email_field)
        email_value = email.get_attribute('value')
        return f'{settings.email}' in email_value

    def add_additional_user_info(self):
        femail = self.find_element(femail_box).click()
        birthday = self.find_element(birth_date)
        birthday.send_keys('03071989')
        self.find_element(save_info_btn).click()

    def check_that_font_of_popup_message_has_a_necessary_color(self):
        message_color = self.find_element(popup_saved_message)
        message_color.value_of_css_property('color')
        return message_color == '#707a7e', 'Invalid font color in popup message'

    def change_existing_password(self):
        old_passwd = self.find_element(old_password_field)
        old_passwd.send_keys(settings.password)
        new_passwd = self.find_element(new_password_field)
        new_passwd.send_keys(settings.new_password)
        new_repeat_passwd = self.find_element(new_repeat_password)
        new_repeat_passwd.send_keys(settings.new_password)
        self.find_element(save_info_btn).click()

    def try_to_change_incorrect_password(self):
        old_passwd = self.find_element(old_password_field)
        old_passwd.send_keys('mistake')
        new_passwd = self.find_element(new_password_field)
        new_passwd.send_keys(settings.new_password)
        new_repeat_passwd = self.find_element(new_repeat_password)
        new_repeat_passwd.send_keys(settings.new_password)
        self.find_element(save_info_btn).click()

    def check_that_help_message_is_appeared(self):
        help_message_text = self.find_element(help_block_message).text
        return 'Неправильный пароль.' in help_message_text










