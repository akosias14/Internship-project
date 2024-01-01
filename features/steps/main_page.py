from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@given('I open the main page "{url}"')
def get_url(context, url):
    if context.app is None:
        raise Exception("Application has not been initialized")
    context.app.main_page.get_url('https://soft.reelly.io/')


CONTINUE_BTN = (By.CSS_SELECTOR, 'a.login-button.w-button')
HEADER = (By.CSS_SELECTOR, 'div.page-title')
FILTERS_BTN = (By.CSS_SELECTOR, 'a.filter-button')
OUT_OF_STOCK_BTN = (By.XPATH, '//div[@class="tag-properties" and @wized="priorityStatusOutOfStock"]/div[@class="tag-text-proparties"]')
OOS_FILTER_RESULTS = (By.CSS_SELECTOR, 'div.div-block-18')


@when('I log in to the page')
def login(context):
    context.app.main_page.login(username='aosias@pivot-point.com', password='Test1234!')
    sleep(5)


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
    context.app.off_plan_page.verify_product_tags(tag)

