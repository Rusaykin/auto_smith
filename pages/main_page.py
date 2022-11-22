from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    url = 'https://www.saucedemo.com/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    select_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//div[@id='shopping_cart_container']"
    menu_button = "//button[@id='react-burger-menu-btn']"
    about_link = "//a[@id='about_sidebar_link']"

    #Getters

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_product_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_product_3(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))
    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.menu_button)))
    def get_about_ink(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.about_link)))


    #Actions

    def click_select_product_1(self):
        self.get_product_1().click()
        print("Product_1 is clicked")

    def click_select_product_2(self):
        self.get_product_2().click()
        print("Product_1 is clicked")

    def click_select_product_3(self):
        self.get_product_3().click()
        print("Product_1 is clicked")

    def click_get_cart(self):
        self.get_cart().click()
        print("Cart is clicked")

    def click_menu_button(self):
        self.get_menu().click()
        print("Menu button is clicked")
    def click_about_link(self):
        self.get_about_ink().click()
        print("About link is clicked")


    # Methods
    def select_products_1(self):
        Logger.add_start_step(method="select_products_1")
        self.get_current_url()
        self.click_select_product_1()
        self.click_get_cart()
        Logger.add_end_step(url=self.driver.current_url, method="select_products_1")

    def select_products_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_get_cart()

    def select_products_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_get_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu_button()
        self.click_about_link()
        self.assert_url("https://saucelabs.com/")
