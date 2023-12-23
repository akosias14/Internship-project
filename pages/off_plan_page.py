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
    OUT_OF_STOCK_BTN = (By.CSS_SELECTOR, "#email-form > div:nth-child(1) > div.filters-tags > div:nth-child(6) > div")
    OOS_FILTER_RESULTS = (By.CSS_SELECTOR, 'div.project-image[wized="projectImage"] .commision-text-box [wized="projectStatus"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_filters_button(self):
        self.wait.until(EC.element_to_be_clickable(self.FILTERS_BTN)).click()


    def filter_by_oos_status(self, status):
        OUT_OF_STOCK_BTN = (By.CSS_SELECTOR, "#email-form > div:nth-child(1) > div.filters-tags > div:nth-child(6) > div")
        try:
            out_of_stock = (self.wait.until(EC.visibility_of_element_located(OUT_OF_STOCK_BTN)))
            out_of_stock.click()
            sleep(10)
        except TimeoutException:
            print(self.driver.page_source)
            raise




    def verify_product_tags(self, tag):
        OOS_FILTER_RESULTS = (By.CSS_SELECTOR, 'div.project-image[wized="projectImage"] .commision-text-box [wized="projectStatus"]')
        product_elements = self.find_elements(*self.OOS_FILTER_RESULTS)
        product_details = []
        all_contain_tag = True

        for product in product_elements:
            product_text = product.text.strip().lower()
            expected_tag = tag.strip().lower()
            contains_tag = expected_tag not in product_text
            product_details.append((product_text,contains_tag))
            if not contains_tag:
                all_contain_tag = False
        return all_contain_tag, product_details

    sleep(20)
