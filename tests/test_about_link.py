import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import urllib3
from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page

import allure
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
urllib3.disable_warnings()
driver = None
@allure.description("Test About Link")
def test_about_link(browser):
    global driver
    driver = browser
    # s = Service('C:\\chromedriver\\chromedriver.exe')
    # driver = webdriver.Chrome(service=s)
    # Install chrome driver from local path
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


    # chrome_options = webdriver.ChromeOptions()
    # driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
    #                           desired_capabilities=DesiredCapabilities.CHROME,
    #                           options=chrome_options)
    #
    # capabilities = {
    #     "browserName": "chrome",
    #     "browserVersion": "108.0",
    #     "enableVNC": True,
    #     "selenoid:options": {
    #         "enableVideo": False,
    #         "enableVNC ": True}}
    # chrome_options = webdriver.ChromeOptions()
    # driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
    #                           desired_capabilities=capabilities,
    #                           options=chrome_options)

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)  # mp = main page
    mp.select_menu_about()

    driver.quit()
