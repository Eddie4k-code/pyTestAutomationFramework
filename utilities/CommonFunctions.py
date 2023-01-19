"""
Contains all common functions used on elements.

"""


import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

"""
Waits for element to appear
"""
def wait_for_element_to_appear(driver, element):
    wait = WebDriverWait(driver, 10)
    e = wait.until(ec.element_to_be_clickable(element))

    return e


def left_click(driver, element):
    wait_for_element_to_appear(element)
    driver.click(element)


def enter_text(driver, element, text):
    wait_for_element_to_appear(element)
    element.send_keys(text)

def read_text(driver, element):
    wait_for_element_to_appear(element)

    return int(element.text)


def wait_for_element_to_dis(driver, element):
    wait = WebDriverWait(driver, 10)
    e = wait.until(ec.invisibility_of_element(element))
