from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


@given('I open the main page "{url}"')
def get_url(context, url):
    context.app.main_page.get_url('https://soft.reelly.io/')


CONTINUE_BTN = (By.CSS_SELECTOR, 'a.login-button.w-button')
OFF_PLAN_BTN = (By.CSS_SELECTOR, 'a._1-link-menu.w--current')
HEADER = (By.CSS_SELECTOR, 'div.page-title')
FILTERS_BTN = (By.CSS_SELECTOR, 'a.filter-button')
OUT_OF_STOCK_BTN = (By.XPATH, '//div[@class="tag-properties" and @wized="priorityStatusOutOfStock"]/div[@class="tag-text-proparties"]')
OOS_FILTER_RESULTS = (By.CSS_SELECTOR, 'div.div-block-18')


@when('I log in to the page')
def login(context):
    context.app.main_page.login(username='aosias@pivot-point.com', password='Test1234!')


@when('click the continue button')
def click_Continue_BTN(context):
    context.driver.find_element(*CONTINUE_BTN).click()

@when('I click on "{menu}" at the left side menu')
def click_on_menu(context,menu):
    context.app.main_page.click_on_menu(menu)

@then('I verify the right page opens')
def verify_right_page(context):
    context.driver.find_element(*HEADER)
    assert context.app.main_page.verify_right_page(), "Right page not opened"

@when('I filter by sale status of "{status}"')
def filter_by_oos_status(context, status):
    context.app.initialize_pages()
    context.app.off_plan_page.click_filters_button()
    context.app.off_plan_page.filter_by_oos_status(status)



@then('I verify each product contains the "{tag}" tag')
def step_verify_product_tags(context, tag):
    all_contain_tag, product_details = context.app.off_plan_page.verify_product_tags(tag)
    for product_text, contains_tag in product_details:
        print(f"Product: '{product_text}', Contains Tag: {contains_tag}")

    assert all_contain_tag, f"Products don't contain the '{tag}' tag"


