from Utilities.base import BasePage
from selenium.webdriver.common.by import By

class LeavePage(BasePage):
    PAGE_HEADER = (By.XPATH, "//h6[text()='My Leave List']")

    def is_page_loaded(self):
        try:
            element = self.find(self.PAGE_HEADER)
            return element.is_displayed()
        except Exception as e:
            self.driver.save_screenshot("leave_page_failure.png")
            print(f"Failed to find Leave page header: {str(e)}")
            raise e