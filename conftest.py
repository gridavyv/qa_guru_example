import pytest
import selenium
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re

PAGE_URL = "https://www.barnesandnoble.com/"

# # set up and tear down fixtures for test environments
@pytest.fixture
def driver():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option(name="detach", value=True)  # Chrome browser will not be closed when the ChromeDriver object is destroyed
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver  # statement in the fixture function is where the setup part ends and the teardown part begins
    driver.close()
    print("Browser is closed.")
    driver.quit()
    print("Driver is quited.")

@pytest.fixture
def pass_url():
    return PAGE_URL