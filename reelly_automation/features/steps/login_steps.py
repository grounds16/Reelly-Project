from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open login page')
def open_login_page(context):
    context.app.login.open_login_page()


@when('Login into Reelly')
def open_login_page(context):
    context.app.login.login()
