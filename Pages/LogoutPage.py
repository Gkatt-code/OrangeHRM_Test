from Utilities.base import BasePage
from selenium.webdriver.common.by import By

class LogoutPage(BasePage):
    PROFILE_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-tab")
    LOGOUT_LINK = (By.XPATH, "//a[text()='Logout']")

    def perform_logout(self):
        self.find(self.PROFILE_DROPDOWN).click()
        self.find(self.LOGOUT_LINK).click()