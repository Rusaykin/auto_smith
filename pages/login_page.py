from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_page():
    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):
        user_name = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))  # data test Xpath
        user_name.send_keys(login_name)

        password = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))  # password CSS selector
        password.send_keys(login_password)

        button_login = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id ='login-button']")))
        button_login.click()
