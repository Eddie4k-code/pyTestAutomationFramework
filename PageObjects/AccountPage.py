from selenium.webdriver.common.by import By

from utilities import CommonFunctions

"""
All functions for the Account Page on the application
"""

class AccountPage:
    select_deposit = '/html/body/div[1]/div/div[2]/div/div[3]/button[2]'
    deposit_entry = '/html/body/div[1]/div/div[2]/div/div[4]/div/form/div/input'
    submit_deposit = '/html/body/div[1]/div/div[2]/div/div[4]/div/form/button'
    deposit_success = '/html/body/div[1]/div/div[2]/div/div[4]/div/span'

    select_withdrawl = '/html/body/div[1]/div/div[2]/div/div[3]/button[3]'
    withdrawl_entry = '/html/body/div[1]/div/div[2]/div/div[4]/div/form/div/input'
    submit_withdrawl = '/html/body/div[1]/div/div[2]/div/div[4]/div/form/button'

    withdrawl_error_msg = '/html/body/div[1]/div/div[2]/div/div[4]/div/span'

    withdrawn_text = '/html/body/div[1]/div/div[2]/div/div[4]/div/form/div/label'

    current_balance = '/html/body/div[1]/div/div[2]/div/div[2]/strong[2]'

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()


    def getCurrentBalance(self):
        """
        Gets current account balance
        :return: current account balance
        """
        return CommonFunctions.wait_for_element_to_appear(self.driver, self.driver.find_element(By.XPATH, self.current_balance)).text


    def select_deposit_option(self):
        """
        Selects Depsoit button
        """
        CommonFunctions.wait_for_element_to_appear(self.driver, self.driver.find_element(By.XPATH, self.select_deposit)).click()

    def enter_deposit(self, amount):
        """
        Enters amount to be deposited
        """
        CommonFunctions.wait_for_element_to_appear(self.driver, self.driver.find_element(By.XPATH, self.deposit_entry)).send_keys(amount)


    def submit_deposit_button(self):
        """
        Clicks the submit deposit button
        """
        CommonFunctions.wait_for_element_to_appear(self.driver, self.driver.find_element(By.XPATH, self.submit_deposit)).click()

    def error_msg(self):
        """
        Gets the text of the error message element
        :return:  The text of the element
        """
        return CommonFunctions.wait_for_element_to_appear(self.driver, self.driver.find_element(By.XPATH, self.withdrawl_error_msg)).text

    def select_withdrawl_option(self):
        """
        Clicks the withdrawl button
        """
        CommonFunctions.wait_for_element_to_appear(self.driver, self.driver.find_element(By.XPATH, self.select_withdrawl)).click()

    def enter_withdrawl(self, amount):
        """
        Enters amount to withdraw
        """
        CommonFunctions.wait_for_element_to_appear(self.driver, self.driver.find_element(By.XPATH, self.withdrawl_entry)).send_keys(amount)

    def submit_withdrawl_option(self):
        """
        Clicks the submit withdraw button
        """
        CommonFunctions.wait_for_element_to_appear(self.driver, self.driver.find_element(By.XPATH, self.submit_withdrawl)).click()

    def deposit_msg_dis_wait(self):
        """
        Waits for successful deposit message to dissapear (this happens after selecting withdraw option)
        """
        CommonFunctions.wait_for_element_to_dis(self.driver, self.driver.find_element(By.XPATH, self.deposit_success))












