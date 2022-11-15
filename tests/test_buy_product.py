import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.login_page import Login_page


def test_buy_product():
    s = Service('C:\\chromedriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    login = Login_page(driver)
    login.authorization()

    enter_shopping_cart = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
    enter_shopping_cart.click()

    time.sleep(5)
