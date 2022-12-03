import settings
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

email_field = (By.CSS_SELECTOR, 'input[name="email"]')  # check
first_name_field = (By.NAME, 'first_name')  # check
last_name_field = (By.NAME, 'last_name')  # check
password_field = (By.NAME, 'new_password')  # check
repeat_password_field = (By.NAME, 'new_repeat_password')  # check
registration_and_enter_button = (By.ID, 'registration-submit')  # check
alert_message = (By.CLASS_NAME, 'alert-login')  # check


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_registration_page(self):  # check
        self.driver.get(self.registration_url)

    @property
    def check_that_jump_to_the_registration_page_was_completed(self):  # check
        registration_btn_text = self.find_element(registration_and_enter_button).text
        return 'Зарегистрироваться и войти' in registration_btn_text

    def enter_correct_registration_data(self, email, first_name, last_name, password):  # check
        self.find_element(email_field).send_keys(email)
        self.find_element(first_name_field).send_keys(first_name)
        self.find_element(last_name_field).send_keys(last_name)
        self.find_element(password_field).send_keys(password)
        self.find_element(repeat_password_field).send_keys(password)
        self.find_element(registration_and_enter_button).click()

    def check_alert_message_after_registration_with_the_same_email(self):  # check
        alert_text = self.find_element(alert_message).text
        return f'Емейл "{settings.email}" уже занят.' in alert_text



