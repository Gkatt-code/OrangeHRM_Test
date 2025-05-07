import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from Pages.LoginPage import LoginPage
from Pages.DashboardPage import DashboardPage
from Pages.LeavePage import LeavePage
from Pages.LogoutPage import LogoutPage
from Utilities.config import Config

@pytest.fixture
def driver():
    service = Service(Config.EDGE_DRIVER_PATH)
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_home_page_title(driver):
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    assert driver.title == Config.LOGIN_TITLE

def test_login_functionality(driver):
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.enter_credentials(Config.USERNAME, Config.PASSWORD)
    login_page.click_login()
    assert driver.current_url == Config.DASHBOARD_URL

def test_leave_functionality(driver):
    driver.get(Config.BASE_URL)
    LoginPage(driver).enter_credentials(Config.USERNAME, Config.PASSWORD).click_login()
    DashboardPage(driver).navigate_to_leave()
    assert LeavePage(driver).is_page_loaded()

def test_logout_functionality(driver):
    driver.get(Config.BASE_URL)
    LoginPage(driver).enter_credentials(Config.USERNAME, Config.PASSWORD).click_login()
    LogoutPage(driver).perform_logout()
    assert driver.current_url == Config.BASE_URL + "/auth/login"