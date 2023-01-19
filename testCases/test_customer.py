import pytest

from PageObjects.AccountPage import AccountPage
from PageObjects.LoginPage import LoginPage
from utilities import ExcelUtils
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_002_Customer:
    """
                Tests all functionality for customer on application
    """

    baseURL = ReadConfig.getAppUrl()
    path = ReadConfig.getPath()
    logger = LogGen.loggen()

    @pytest.mark.parametrize("row", ExcelUtils.testData(ReadConfig.getPath(), 'Sheet1'))
    def test_customer(self, setup, row):

        """
        Logs in to application then makes deposit and withdrawl.

        :param setup: The webdriver
        :param row: row of test data from excel file.
        """

        if row[1].lower() == 'no':
            self.logger.info('***Test Execution Set to No, Skipping***')
            pytest.skip("Skipped, if mistake set execution to yes in test data")

        self.logger.info(f'***Starting Customer Test for test case {row[0]}***')
        self.driver = setup
        self.logger.info('***Getting Base Url***')
        self.driver.get(self.baseURL)
        self.logger.info('***Getting LoginPage Object Model***')
        self.lp = LoginPage(self.driver)
        self.logger.info('***Getting AccountPage Object Model***')
        self.ap = AccountPage(self.driver)
        self.logger.info('***Getting Test Data***')
        self.username = row[2]
        self.deposit_amount = row[3]
        self.after_deposit_amount = row[4]
        self.withdrawl_amount = row[5]
        self.after_withdrawl_amount = row[6]
        self.deposit = row[7]
        self.withdrawl = row[8]
        self.fail = row[9]

        self.logger.info(f"***Logging in with username {self.username}***")
        self.lp.setUserName(self.username)
        self.lp.clickLogin()
        verify_login = self.lp.verifyLogin()

        if verify_login != None:
            self.logger.info('***Login Success***')

        else:
            self.logger.info('***Login Failed, ending test case***')
            assert False


        if self.deposit.lower() == 'yes':

            self.logger.info('***Making Deposit***')

            self.ap.select_deposit_option()

            self.ap.enter_deposit(self.deposit_amount)

            self.ap.submit_deposit_button()

            self.currentBalance = self.ap.getCurrentBalance()

            if int(self.currentBalance) == int(self.after_deposit_amount):
                self.logger.info(f'***Balance after deposit as expected***')

            else:
                self.logger.info(f'***Balance not as expected, balance is {self.currentBalance}, failing test case')
                self.driver.save_screenshot(".\\Screenshots\\" + "test_Customer.png")
                assert False


        if self.withdrawl.lower() == 'yes':


            self.logger.info('***Making Withdrawl***')

            self.ap.select_withdrawl_option()

            self.ap.deposit_msg_dis_wait()

            self.ap.enter_withdrawl(self.withdrawl_amount)


            self.ap.submit_withdrawl_option()



            if self.fail.lower() == 'yes':

                if self.ap.error_msg() is not None:
                    self.logger.info(f'***Transaction Failed as expected, {self.ap.error_msg()}***')
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_Customer.png")
                    assert True

                else:
                    self.logger.info(f'***Transaction Error Message not showing as expected, failing test case***')
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_Customer.png")
                    assert False


            self.currentBalance = self.ap.getCurrentBalance()


            if int(self.currentBalance) == int(self.after_withdrawl_amount):
                self.logger.info(f'***Balance after withdrawl as expected***')

            else:
                self.logger.info(f'***Balance not as expected, balance is {self.currentBalance}, failing test case')
                self.driver.save_screenshot(".\\Screenshots\\" + "test_Customer.png")
                assert False

        self.logger.info(f'***Test has Passed***')
        assert True

























