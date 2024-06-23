import pytest
import selenium
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from collections.abc import MutableMapping
from collections.abc import Mapping
# import allure

def test_verify_title(driver, pass_url):
        driver.get(pass_url)
        driver.find_elements(By.XPATH, "//a[text()='Gift Cards']")[0].click()
        expected_title = "!Barnes & Noble Gift Cards and eGift Cards | Barnes & Noble®"
        title = driver.title
        assert title == expected_title, f"Expected title: {expected_title} is not matching actual title {title}"

# APPROACH # 1
# def test_verify_title(driver, pass_url):
#     with allure.step("Open main page"):
#         driver.get(pass_url)
#     with allure.step("Click of Gift Card"):
#         driver.find_elements(By.XPATH, "//a[text()='Gift Cards']")[0].click()
#     with allure.step("Get title."):
#         expected_title = "!Barnes & Noble Gift Cards and eGift Cards | Barnes & Noble®"
#         title = driver.title
#     with allure.step("Assert title."):
#         assert title == expected_title, f"Expected title: {expected_title} is not matching actual title {title}"


# APPROACH # 2
# def test_verify_title(driver, pass_url):
#     open_main_page(driver, pass_url)
#     click_gift_card(driver)
#     assert_title(driver)

# @allure.step("Open main page")
# def open_main_page(driver, pass_url):
#     driver.get(pass_url)

# @allure.step("Click of Gift Card")
# def click_gift_card(driver):
#     driver.find_elements(By.XPATH, "//a[text()='Gift Cards']")[0].click()

# @allure.step("Get title.")
# def get_title(driver):
#     return driver.title

# @allure.step("Assert title.")
# def assert_title(driver):
#     expected_title = "!Barnes & Noble Gift Cards and eGift Cards | Barnes & Noble®"
#     actual = get_title(driver)
#     assert actual == expected_title, f"Expected title: {expected_title} is not matching actual title {actual}"