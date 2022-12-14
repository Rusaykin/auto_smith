import time
import allure

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


@allure.description("Test buy product_1")
@pytest.mark.smoke
def test_buy_product_1(set_group):
    # s = Service('C:\\chromedriver\\chromedriver.exe')
    # driver = webdriver.Chrome(service=s)
    # Install chrome driver from local path

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    print("Start test 1")
    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)  # mp = main page
    mp.select_products_1()

    cp = Cart_page(driver)  # Cp = cart page
    cp.select_checkout_button()

    cip = Client_info_page(driver)  # cip = client information page
    cip.input_information()

    ovp = Payment_page(driver)  # ovp = Over view screen / Payment page
    ovp.tap_finish_button()

    f = Finish_page(driver)  # f = finish
    f.finish()  # Doing screen

    time.sleep(2)

    driver.quit()


# @pytest.mark.regression
# @pytest.mark.run(order=1)
# def test_buy_product_2():
#     s = Service('C:\\chromedriver\\chromedriver.exe')
#     driver = webdriver.Chrome(service=s)
#     print("Start test 2")
#     login = Login_page(driver)
#     login.authorization()
#
#     mp = Main_page(driver)  # mp = main page
#     mp.select_products_2()
#
#     cp = Cart_page(driver)  # Cp = cart page
#     cp.select_checkout_button()
#
#     time.sleep(2)
#
#     driver.quit()
#
#
# def test_buy_product_3():
#     s = Service('C:\\chromedriver\\chromedriver.exe')
#     driver = webdriver.Chrome(service=s)
#     print("Start test 3")
#     login = Login_page(driver)
#     login.authorization()
#
#     mp = Main_page(driver)  # mp = main page
#     mp.select_products_3()
#
#     cp = Cart_page(driver)  # Cp = cart page
#     cp.select_checkout_button()
#
#     time.sleep(2)
#
#     driver.quit()
