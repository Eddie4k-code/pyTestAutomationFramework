"""

All Functions and elements for the Login page of the application.

"""

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from utilities import CommonFunctions
import selenium


class LoginPage:
    name_selector = "/html/body/div/div/div[2]/div/form/div/select"
    login_button = "/html/body/div[1]/div/div[2]/div/form/button"
    welcome_message = "/html/body/div[1]/div/div[2]/div/div[3]/button[1]"

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    # Selects username
    def setUserName(self, username):
        """
        Clicks dropdown and selects username
        """
        dropdown = CommonFunctions.wait_for_element_to_appear(self.driver, self.driver.find_element(By.CSS_SELECTOR, "#userSelect"))
        select = Select(dropdown)
        select.select_by_visible_text(username)


    def clickLogin(self):
        """
        Clicks Login Button
        """
        CommonFunctions.wait_for_element_to_appear(self.driver, self.driver.find_element(By.XPATH, self.login_button)).click()

    def verifyLogin(self):
        """
        Verifies user logged in by reading welcome message and checking if it contains username.
        """
        try:

            welcome = self.driver.find_element(By.XPATH, self.welcome_message)
            return welcome

        except:
            return None


