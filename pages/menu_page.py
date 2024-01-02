from pages.base_page import Base
from selenium.webdriver.common.by import By


class MenuPage(Base):
    my_menu_title = (By.XPATH, "//h1[@class='h1-menu']")
    settings = (By.XPATH, "//div[contains(text(),'Settings')]")
    expected_menu_text = "My menu"

    def click_settings(self):
        self.click(*self.settings)
    def verify_menu_page(self):
        self.assert_text(self.expected_menu_text, *self.my_menu_title)
