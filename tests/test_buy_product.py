import time
from selenium import webdriver
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


def test_buy_product():
    s = Service('C:\\chromedriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver) #mp = main page
    mp.select_product()

    cp = Cart_page(driver) # Cp = cart page
    cp.select_checkout_button()

    cip = Client_info_page(driver) # cip = client information page
    cip.input_information()

    ovp = Payment_page(driver) #ovp = Over view screen / Payment page
    ovp.tap_finish_button()

    f = Finish_page(driver) # f = finish
    f.get_screenshot() # Doing screen



    time.sleep(5)

    driver.quit()
