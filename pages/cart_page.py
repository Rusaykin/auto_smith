from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Cart_page(Base):

    url = 'https://www.saucedemo.com/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    checkout = "//button[@id='checkout']"

    #Getters


    def get_checkout(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout)))


    #Actions

    def click_checkout(self):
        self.get_checkout().click()
        print("Checkout is clicked")


    # Methods
    def select_checkout_button(self):
        self.get_current_url()
        self.click_checkout()
