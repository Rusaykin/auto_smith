import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as CO


@pytest.fixture(scope="function")
def browser():
    print("Using conftest driver")
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "109.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False}}
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor='http://172.19.4.193:4444/wd/hub',
                              desired_capabilities=capabilities,
                              options=chrome_options
                              )
    driver.maximize_window()

    return driver

# @pytest.fixture()
# def setup():
#     print("Start test from conftest")  # Всё что до теста
#     yield  # Test
#     print("Finish test2")  # всё что после теста
