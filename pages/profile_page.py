from time import sleep
from pages.base_page import Base
from selenium.webdriver.common.by import By



class ProfilePage(Base):
    actual_profile_text = (By.XPATH, "//div[@class='profile-h1']")
    close_button = (By.XPATH, "//div[@class='profile-button-block']/a")
    expected_name_text = "test+greg+careerist"
    company_field = (By.ID, "Company-name")
    name_field = (By.ID, "Fullname")
    company_input_text = "Test1"
    expected_profile_text = "Profile"
    save_changes = (By.XPATH, "//div[@class='save-changes-button']")

    def verify_profile_page(self):
        self.assert_text(self.expected_profile_text, *self.actual_profile_text)

    def update_company_text(self):
        self.ec_wait_text_to_be_present_in_element(expected_text=self.expected_name_text, locator= self.name_field)
        self.clear_text(*self.company_field)
        self.input(self.company_input_text, *self.company_field)

    def verify_company_updated_text(self):
        self.ec_wait_text_to_be_present_in_element(expected_text=self.expected_name_text, locator= self.name_field)
        self.assert_input_text(self.company_input_text,*self.company_field)

    def verify_close_and_save_button_enabled(self):
        assert self.element_displayed(*self.close_button), "Close button is not displayed"
        assert self.element_enabled(*self.close_button), "Close button is not enabled"
        assert self.element_displayed(*self.save_changes), "Save button is not displayed"
        assert self.element_enabled(*self.save_changes), "Save button is not enabled"

    def click_close_button(self):
        self.click(*self.close_button)

    def selects_save_button(self):
        self.click(*self.save_changes)
        sleep(2)

    def clear_company_text(self):
        self.clear_text(*self.company_field)
