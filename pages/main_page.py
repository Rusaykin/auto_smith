from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    url = 'https://www.saucedemo.com/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    cart = "//div[@id='shopping_cart_container']"


    #Getters

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_1)))
    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))


    #Actions

    def click_select_product_1(self):
        self.get_product_1().click()
        print("Product_1 is clicked")

    def click_get_cart(self):
        self.get_cart().click()
        print("Cart is clicked")


    # Methods
    def select_product(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_get_cart()
