from Utilities.config import Config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.TIMEOUT)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def get_title(self):
        return self.driver.title
