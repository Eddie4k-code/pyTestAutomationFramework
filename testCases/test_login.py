import logging

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.AccountPage import AccountPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import openpyxl


#@pytest.mark.parametrize("row", openpyxl.load_workbook(path).active.iter_rows(values_only=True))

class Test_001_Login:
    baseURL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer"
    username = "Harry Potter"
    path = ".//TestData//LoginData.xlsx"
    logger = LogGen.loggen()



    @pytest.mark.parametrize("row", ExcelUtils.testData(ReadConfig.getPath(), 'Sheet1'))
    def test_login(self, setup, row):
        """
        Logs into Web Application
        """


        self.driver = setup
        self.driver.get(ReadConfig.getAppUrl())
        self.lp = LoginPage(self.driver)

        self.test_name = row[0]
        self.execute = row[1]
        self.username = row[2]

        self.logger.info(f"****Starting {self.test_name} Data Driven Login Test ****")

        if self.execute.lower() == 'no':
            self.logger.info("***Test Skipped***")
            pytest.skip("Skipped")

        self.logger.info(f"****Logging in with username {self.username} ****")
        self.lp.setUserName(self.username)
        self.lp.clickLogin()
        actual_username = self.lp.verifyLogin()

        if actual_username != None:
            self.logger.info("***Login Passed ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Customer.png")
            assert True

        else:
            self.logger.info("***Login Failed ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Customer.png")
            assert False









