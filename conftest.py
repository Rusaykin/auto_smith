import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


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
