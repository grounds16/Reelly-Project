from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify menu landing page')
def verify_menu_page(context):
    context.app.menu.verify_menu_page()

@when('User select settings')
def click_settings(context):
    context.app.menu.click_settings()
