from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify settings page')
def verify_settings_page(context):
    context.app.settings.verify_settings_page()
@when('User clicks edit profile')
def click_edit_button(context):
    context.app.settings.click_edit_profile()