from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import Page

class MainPage(Page):
    CONTINUE_BTN = (By.CSS_SELECTOR, 'a.login-button.w-button')
    OFF_PLAN_BTN = (By.CSS_SELECTOR, 'a._1-link-menu.w--current')

    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self, url):
        self.driver.get(url)

    def login(self, username, password):
        username_field = self.driver.find_element(By.CSS_SELECTOR, 'input#email-2')
        password_field = self.driver.find_element(By.CSS_SELECTOR, 'input#field')

        username_field.send_keys(username)
        password_field.send_keys(password)

    def click_Continue_BTN(self):
        self.wait.until(EC.element_to_be_clickable(*self.CONTINUE_BTN)).click()

    def click_on_menu(self, menu):
        OFF_PLAN_BTN = (By.ID, 'w-node-_455f4786-676e-1311-ab71-82d622b51c3b-9b22b68b')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OFF_PLAN_BTN)).click()

    def verify_right_page(self):
        try:
            page_title_element = self.driver.find_element(By.CSS_SELECTOR, 'div.page-title')
            return page_title_element.is_displayed()
        except NoSuchElementException:
            return False
