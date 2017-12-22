from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium_fixture import app

from application import Application

def test_1(app):
    application = Application(app)
    application.open_home_page()
def test_search(app):
    application = Application(app)
    application.driver.find_element_by_class_name("rz-header-search-inner").click()
    actions = ActionChains(application.driver)
    actions.send_keys('iphone 8')
    actions.perform()



