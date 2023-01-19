# pyTestAutomationFramework
A Data Driven Automation Testing Framework for a Demo Site.
https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer

<h1>Description</h1>
Having experience in automation testing with Java, Selenium and TestNG. I wanted to get my hands on pytest and create an automation framework with it to practice my skills.


<h1>Command Line</h1>
(Tests that are avaliable are test_login and test_customer)
<h3>Run a specific test</h3> -  pytest -v -s testCases/test_file_name.py --html=Reports\report.html --capture sys -rF

<h3>Change Browser</h3>
add --browser= chrome or firefox


<h1>Tests</h1>
Login Test - Tests logging into the application
Customer Test - Tests Logging into the application and making a deposit and a withdrawl.

<h1>Directory</h1>
<h3>Configurations</h3> Contains all config info such as URL, and path to test data.
<h3>Logs</h3> Stores all logs from run time
<h3>PageObjects</h3> Contains functions and element selectors for each page
<h3>Reports</h3> After run time a html report is generated and stored here.
<h3>Screenshots</h3>When a test fails a screenshot is saved here
<h3>testCases</h3>Contains all test methods
<h3>TestData</h3>Test Data Excel file is stored here
<h3>utilities</h3>Contains utilities such as common functions that are used, functions for reading test data, reading properties and logging.
