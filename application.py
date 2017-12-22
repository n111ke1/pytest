class Application(object):
    def __init__(self, driver):
        self.driver = driver
    def open_home_page(self):
        self.driver.get("https://rozetka.com.ua/")

    # work with objects
