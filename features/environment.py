from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options as FirefoxOptions


def browser_init(context, scenario_name):
    """
    Initialize the browser and the Application object.
    :param context: Behave context
    """

    ### Firefox Configuration ###
    # service = Service(executable_path='/Users/ms.kerry/Downloads/Scrambled GA Logo/Automation Internship/geckodriver')
    # context.driver = webdriver.Firefox(service=service)
    # options = FirefoxOptions()
    # context.driver = webdriver.Firefox(options=options)
    # context.app = Application(context.driver)
    # context.app.initialize_pages()
    # context.driver = webdriver.Safari()
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)


# HEADLESS MODE ####
#
    # options = webdriver.FirefoxOptions()
    # options.add_argument('headless')
    # service = Service(GeckoDriverManager().install())
    # context.driver = webdriver.Firefox(options=options, service=service)

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'anneosias_xSOENm'
    bs_key = '8jP8v1yu9aRD3KApCVMQ'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'os': 'Windows',
        'osVersion': '10',
        'browserName': 'Chrome',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.wait = WebDriverWait(context.driver, 15)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)



def before_scenario(context, scenario):
    """
    This hook will be executed before each scenario.
    """
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    """
    This hook will be executed before each step.
    """
    print('\nStarted step: ', step)


def after_step(context, step):
    """
    This hook will be executed after each step.
    """
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    """
    This hook will be executed after each scenario.
    """
    if hasattr(context, 'driver') and context.driver:
        context.driver.delete_all_cookies()
        context.driver.quit()
