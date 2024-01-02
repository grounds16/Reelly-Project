from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify profile page is displayed')
def verify_profile_page(context):
    context.app.profile.verify_profile_page()


@when('User updates company text')
def update_company_text(context):
    context.app.profile.update_company_text()


@then("Verify Company's text is updated")
def verify_company_updated_text(context):
    context.app.profile.verify_company_updated_text()


@then("Verify close and save button are enabled")
def verify_close_and_save_button_enabled(context):
    context.app.profile.verify_close_and_save_button_enabled()

@when ("User selects close")
def user_selects_close(context):
    context.app.profile.click_close_button()

@when ("User selects save changes")
def user_selects_saves_changes(context):
    context.app.profile.selects_save_button()

@when ("User clears company text")
def clear_company_text(context):
    context.app.profile.clear_company_text()