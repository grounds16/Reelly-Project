from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
import os
from dotenv.main import load_dotenv
from selenium import webdriver


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    #Browser Stack#
    #-------------------------------------------------------------------------#
    # bs_user = 'gregrounds_ihN9M2'
    # bs_key = 'AL7h559zLeeEcb66sKE2'
    # url = f"http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub"
    # browser = 'ChromeOptions'
    #
    # if browser == 'ChromeOptions':
    #     options = ChromeOptions()
    #     options.add_argument("headless")
    #     options.add_argument("--window-size=1920,1080")
    # if browser == 'FirefoxOptions':
    #     options = FirefoxOptions()
    #     options.headless = True
    #
    # bstack_options = {
    #         "os": "Windows",
    #         "osVersion": "11",
    #         "browserVersion": "latest",
    #         "local": "false",
    #         "seleniumVersion": "4.14.1",
    #         "sessionName": scenario_name
    # }
    #
    # options.set_capability('bstack:options', bstack_options)
    #
    #
    # context.driver = webdriver.Remote(command_executor=url, options=options)
    # context.driver.wait = WebDriverWait(context.driver, 10)
    # context.driver.implicitly_wait(4)
    # context.app = Application(context.driver)

    # -------------------------------------------------------------------------#


    #Local Firefox#
    # -------------------------------------------------------------------------#
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # context.driver.maximize_window()
    # context.driver.wait = WebDriverWait(context.driver, 10)
    # context.driver.implicitly_wait(4)
    # context.app = Application(context.driver)
    # -------------------------------------------------------------------------#


    #Chrome Mobile Emulator#
    # -------------------------------------------------------------------------#
    mobile_emulation = {
        "deviceName": "Nest Hub Max"
    }

    options = webdriver.ChromeOptions()

    options.add_experimental_option("mobileEmulation", mobile_emulation)


    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)
    # -------------------------------------------------------------------------#


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
