from pages.base_page import Page
from pages.off_plan_page import OffPlanPage
from pages.main_page import MainPage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = None
        self.off_plan_page = None
    ...
    def intialize_pages(self):
        self.main_page = MainPage(self.driver)
        self.off_plan_page = OffPlanPage(self.driver)
    ...

    def initialize_pages(self):
        self.main_page = MainPage(self.driver)
        self.off_plan_page = OffPlanPage(self.driver)
        # Initialize other pages if needed

    def quit(self, driver):
        self.driver.quit()

