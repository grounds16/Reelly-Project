from pages.login_page import LoginPage
from pages.base_page import Base
from pages.menu_page import  MenuPage
from pages.settings_page import SettingsPage
from pages.profile_page import ProfilePage


class Application:
    def __init__(self, driver):
        self.base = Base(driver)
        self.login = LoginPage(driver)
        self.menu = MenuPage(driver)
        self.settings = SettingsPage(driver)
        self.profile = ProfilePage(driver)
