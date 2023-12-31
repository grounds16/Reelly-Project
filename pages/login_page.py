from time import sleep
from pages.base_page import Base
from selenium.webdriver.common.by import By
import os
from dotenv.main import load_dotenv


class LoginPage(Base):
    load_dotenv()
    email_input = (By.ID, "email-2")
    login_button = (By.XPATH, '//a[@wized="loginButton"]')
    password_input = (By.ID, "field")
    email = os.getenv("reelly_email")
    password = os.getenv("reelly_password")
    number_of_agents = (By.XPATH, "//div[@wized='usersCounter']")

    def open_login_page(self):
        self.open_url("https://soft.reelly.io/sign-in")

    def login(self):
        sleep(2) #Used a sleep here instead of a EW on purpose. Couldnt find a better way atm.
        self.input(self.email, *self.email_input)
        self.input(self.password, *self.password_input)
        self.click(*self.login_button)

