from reelly_automation.pages.base_page import Base
from selenium.webdriver.common.by import By


class SettingsPage(Base):
    edit_profile = (By.XPATH, "//div[@class='setting-text']")
    edit_profile_text = "Edit profile"
    def click_edit_profile(self):
        self.click(*self.edit_profile)

    def verify_settings_page(self):
        self.assert_text(self.edit_profile_text, *self.edit_profile)