from Utilities.base import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def enter_credentials(self, username, password):
        self.find(self.USERNAME_FIELD).send_keys(username)
        self.find(self.PASSWORD_FIELD).send_keys(password)
        return self

    def click_login(self):
        self.find(self.LOGIN_BUTTON).click()