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


"""
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, setup):
    driver = setup()
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):


            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            self.driver.save_screenshot(destinationFile)

            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" onclick="window.open(this.src)" align="right" />' % file_name





            extra.append(pytest_html.extras.html(html))
        report.extra = extra
"""

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



