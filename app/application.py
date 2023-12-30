from pages.base_page import Page
from pages.off_plan_page import OffPlanPage
from pages.main_page import MainPage

class Application:
    def __init__(self, driver):
        if driver is None:
            raise ValueError("Driver should not be None")
        self.driver = driver
        self.main_page = None
        self.off_plan_page = None
        self.initialize_pages()
    ...
    def initialize_pages(self):
        self.main_page = MainPage(self.driver)
        self.off_plan_page = OffPlanPage(self.driver)
    ...
    def quit(self, driver):
        self.driver.quit()

