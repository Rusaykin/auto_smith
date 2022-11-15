
class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url " + get_url)


    """Method assert word"""

    def assert_word(self, word, result):

# text_products = driver.find_element(By.XPATH, "//*[@class='title']")
# value_text_products = text_products.text
# assert value_text_products == "PRODUCTS"
# print("Good")
        value_word = word.text
        assert value_word == result
