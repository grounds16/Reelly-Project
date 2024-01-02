from time import sleep
from pages.base_page import Base
from selenium.webdriver.common.by import By


class LoginPage(Base):
    email_input = (By.ID, "email-2")
    login_button = (By.XPATH, '//a[@wized="loginButton"]')
    password_input = (By.ID, "field")
    email = "roundsgreg@gmail.com"
    password = "1717@Careerist1919"

    def open_login_page(self):
        self.open_url("https://soft.reelly.io/sign-in")

    def login(self):
        sleep(1)
        self.input(self.email, *self.email_input)
        self.input(self.password, *self.password_input)
        self.click(*self.login_button)

