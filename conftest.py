import pytest
import settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


login_button_home = (By.XPATH, '//a[@class="btn" and @style="font-size: 12px"]')
login_button_login = (By.ID, 'login-submit')
all_fields = (By.CLASS_NAME, 'form-control')


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('start-maximized')
    options.add_argument(r'user-data-dir=C:\Users\Masha\PycharmProjects\gym_pad_testing\info_session')
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    driver.get('https://www.gympad.ru/')
    if driver.find_element(By.CSS_SELECTOR, 'span[class="hidden-xs"]').text != settings.first_name:
        login_btn = driver.find_element(By.XPATH, '//a[@class="btn" and @style="font-size: 12px"]')
        login_btn.click()
        email_field = driver.find_elements(By.CLASS_NAME, 'form-control')[0]
        email_field.send_keys(settings.email)
        password_field = driver.find_elements(By.CLASS_NAME, 'form-control')[1]
        password_field.send_keys(settings.password)
        password_field.send_keys(Keys.ENTER)





