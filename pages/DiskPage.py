import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class DiskPage(BasePage):
    BUTTON_CREATE = (By.CSS_SELECTOR, "span.create-resource-popup-with-anchor button")
    BUTTON_CREATE_DIR = (By.CSS_SELECTOR, "div.create-resource-popup-with-anchor__popup button[aria-label='Папку']")
    BUTTON_CREATE_FILE = (By.CSS_SELECTOR,
                          "div.create-resource-popup-with-anchor__popup button[aria-label='Текстовый документ']")
    DIR_NAME = (By.CSS_SELECTOR, "div.dialog__wrap input")
    BUTTON_SAVE = (By.CSS_SELECTOR, "div.dialog__wrap button.confirmation-dialog__button_submit")


    @allure.step
    def create_content(self, content_name, content_type="dir"):
        self.element(self.BUTTON_CREATE).click()
        if content_type == "dir":
            self.element(self.BUTTON_CREATE_DIR).click()
        elif content_type == "file":
            self.element(self.BUTTON_CREATE_FILE).click()
        self._input(self.element(self.DIR_NAME), content_name)
        self.element(self.BUTTON_SAVE).click()
        return self

    @allure.step
    def open_content(self, content_name):
        self.double_click_to_el(self.element((By.CSS_SELECTOR, f"div[aria-label='{content_name}']")))
        return self

    @allure.step
    def close_file(self):
        self.switch_to_back()
        return self

    @allure.step
    def search_content(self, content_name):
        return self.element((By.CSS_SELECTOR, f"div[aria-label*='{content_name}']")).text
