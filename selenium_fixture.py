from selenium import webdriver
import pytest
from conftest import *

@pytest.fixture(scope="module")
def app(request, browser_type):
    if browser_type == "chrome":
        driver = webdriver.Chrome()
    elif browser_type == "firefox":
        driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return driver

