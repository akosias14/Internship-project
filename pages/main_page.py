from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import Page
import time

class MainPage(Page):
    CONTINUE_BTN = (By.CSS_SELECTOR, 'a.login-button.w-button')
    USERNAME = (By.ID, 'email-2')
    PASSWORD = (By.CSS_SELECTOR, 'input#field.input.w-input')
    HEADER = (By.CSS_SELECTOR, 'div.page-title')

    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self, url):
        if self.driver is None:
            raise ValueError("Driver is not initialized")
        self.driver.get(url)

    def login(self, username, password):
        # time.sleep(5)
        username_field = self.driver.find_element(*self.USERNAME)
        password_field = self.driver.find_element(*self.PASSWORD)
        username_field.send_keys(username)
        password_field.send_keys(password)

    def click_Continue_BTN(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN)).click()

    def click_on_menu(self, menu):
        OFF_PLAN_BTN = (By.ID, 'w-node-_455f4786-676e-1311-ab71-82d622b51c3b-9b22b68b')
        MAIN_MENU_BTN = (By.CSS_SELECTOR, 'a.menu-button-block.link-block.link-block-2.link-block-3.link-block-4.w-inline-block.w--current')
        time.sleep(5)
        wait = WebDriverWait(self.driver, 5)
        menu_button = wait.until(EC.element_to_be_clickable(MAIN_MENU_BTN))
        menu_button.click()

        if menu.lower() == "off plan":
            try:
                off_plan_menu = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(OFF_PLAN_BTN))
                off_plan_menu.click()
            except TimeoutException:
                print("Timeout occurred while waiting for the element")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", menu_button)
                off_plan_menu = self.driver.find_element(*OFF_PLAN_BTN)
                off_plan_menu.click()
        else:
            print(f"Menu option '{menu}' not recognized.")
        WebDriverWait(self.driver, 5).until(lambda driver: 'off-plan' in driver.current_url)

    def verify_right_page(self):
        time.sleep(5)
        try:
            page_title_element = self.driver.find_element(*self.HEADER)
            return page_title_element.is_displayed()
        except NoSuchElementException:
            return False
