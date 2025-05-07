import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    return "chrome"