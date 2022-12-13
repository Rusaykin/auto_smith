import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as CO


@pytest.fixture()
def setup():
    print("Start test from conftest")  # Всё что до теста
    yield  # Test
    print("Finish test2")  # всё что после теста


@pytest.fixture(scope="module")
def set_group():
    print("Enter system")  # Всё что до теста
    yield  # Test
    print("Exit system")  # всё что после теста


@pytest.fixture()
def get_chrome_options():
    options = CO()
    options.add_argument('headless')
    yield  # Test
    print("Finish test2")  # всё что после теста


@pytest.fixture(scope="function")
def browser():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "108.0",
        "selenoid:options": {
            "enableVideo": False}}
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                              desired_capabilities=capabilities,
                              options=chrome_options)
    driver.maximize_window()
    yield
    driver.quit()