from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

all_login_fields = (By.CLASS_NAME, 'form-control')  # check
login_button = (By.ID, 'login-submit')  # check
remember_me_box = (By.ID, 'remember-me')  # check
forget_password_link = (By.ID, 'login-forget-link')  # check
alert_message = (By.CLASS_NAME, 'alert-danger')  # check


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):  # check
        self.driver.get(self.login_url)

    @property
    def check_that_jump_to_the_login_page_was_completed(self):  # check
        login_btn_text = self.find_element(login_button).text
        return 'Войти' in login_btn_text

    def enter_login_data(self, email, password):  # check
        self.find_elements(all_login_fields)[0].send_keys(email)
        self.find_elements(all_login_fields)[1].send_keys(password)
        sleep(3)    # for demonstration purposes
        self.find_element(login_button).click()

    def check_alert_message_after_login_with_incorrect_password(self):  # check
        alert_text = self.find_element(alert_message).text
        return 'Неправильный пароль' in alert_text

    def check_alert_message_after_login_with_incorrect_email(self):  # check
        alert_text = self.find_element(alert_message).text
        return 'Пользователь не найден' in alert_text

    def check_that_remember_me_box_is_selected(self):  # check
        return self.find_element(remember_me_box).is_selected()

    def check_that_forget_password_link_is_present_on_the_login_page(self):  # check
        return self.find_element(forget_password_link).is_enabled()



