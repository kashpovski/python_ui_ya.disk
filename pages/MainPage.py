import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    BUTTON_TO_LOGIN = (By.CSS_SELECTOR, "a.headline__personal-enter")
    BUTTON_MENU = (By.CSS_SELECTOR, "a.services-pinned__all")
    BUTTON_DISK = (By.CSS_SELECTOR, "a[data-statlog='services-more-popup.item.disk']")


    @allure.step
    def go_to_login_page(self):
        self.element(self.BUTTON_TO_LOGIN).click()
        return self

    @allure.step
    def go_to_disk(self):
        self.element(self.BUTTON_MENU).click()
        self.element(self.BUTTON_DISK).click()
        self.switch_to_window()
        return self
