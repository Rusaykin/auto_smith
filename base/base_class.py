import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url " + get_url)


    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result


    """Method svreenshot"""

    def get_screenshot(self):
        # Создаем скриншот
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screen = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('E:\\Projects\\auto_smith\\screen\\' + name_screen)


    """Method assert url"""
        #Метод по сравниванию url
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Get URL")
