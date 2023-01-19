import pytest
from selenium import webdriver
import os
"""
Creates web driver before test.
"""

# Before test it will launch specified browser, default chrome
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        driver.implicitly_wait(10)
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        print("Launching firefox browser.........")


    else:
        driver=webdriver.Chrome()
        driver.implicitly_wait(10)
        print("Launching chrome browser.........")



    yield driver

    driver.close()

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")






"""

Pytest HTML Report

"""


def pytest_configure(config):
    config._metadata["Project Name"] = "XYZ Bank"
    config._metadata["Module Name"] = "Blank"
    config._metadata["Tester"] = "Eddie"



def pytest_html_report_title(report):
    report.title = "Automation"







#Modify Environment info to html report.
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)




#Data Provider
@pytest.fixture()
def test():
    rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
    cols = ExcelUtils.getColumnCount(self.path, 'Sheet1')

    for r in range(2, self.rows + 1):
        test_name = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
        execute = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
        username = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

        yield {"test_name":test_name, "execute":execute, "username":username}


    #Iterate all excel rows if execute then add to dict return dict



