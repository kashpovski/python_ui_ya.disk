import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "input[autocomplete='username']")
    PASSWORD = (By.CSS_SELECTOR, "input[autocomplete='current-password']")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button[type='submit']")


    @allure.step
    def login(self, username="", password=""):
        self._input(self.element(self.USERNAME), username)
        self.element(self.BUTTON_LOGIN).click()
        self._input(self.element(self.PASSWORD), password)
        self.element(self.BUTTON_LOGIN).click()
        return self

