from Utilities.base import BasePage
from selenium.webdriver.common.by import By

class DashboardPage(BasePage):
    LEAVE_MENU = (By.XPATH, "//span[text()='Leave']")
    MY_LEAVE = (By.XPATH, "//a[text()='My Leave']")

    def navigate_to_leave(self):
        self.find(self.LEAVE_MENU).click()
        self.find(self.MY_LEAVE).click()