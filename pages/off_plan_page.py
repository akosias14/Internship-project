from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class OffPlanPage(Page):
    FILTERS_BTN = (By.CSS_SELECTOR, 'a.filter-button')
    OOS_BTN = (By.CSS_SELECTOR, '[wized="priorityStatusOutOfStock"][class="tag-properties margin-bottom-8"]>[class="tag-text-proparties"]')
    OOS_FILTER_RESULTS = (By.CSS_SELECTOR, 'div.div-block-18')

    def __init__(self, driver):
        super().__init__(driver)

    def click_filters_button(self):
        self.wait.until(EC.element_to_be_clickable(self.FILTERS_BTN)).click()


    def filter_by_oos_status(self, status):
        OOS_BTN = (By.CSS_SELECTOR, '[wized="priorityStatusOutOfStock"][class="tag-properties margin-bottom-8"]>[class="tag-text-proparties"]')
        try:
            out_of_stock = (self.wait.until(EC.visibility_of_element_located(OOS_BTN)))
            out_of_stock.click()
            sleep(10)
        except TimeoutException:
            print(self.driver.page_source)
            raise

    def verify_product_tags(self, expected_tag):
        tags = self.find_elements(*self.OOS_FILTER_RESULTS)
        expected_tag = expected_tag.strip().lower()

        for tag in tags:
            assert expected_tag in tag.text.strip().lower(), f"Expected '{expected_tag}' not in '{tag.text}'"

    sleep(5)
