import time

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    PATH = ""
    ALERT = (By.CSS_SELECTOR, "div.alert")

    def __init__(self, browser):
        self.browser = browser

    def open(self, path=None):
        if path is None:
            path = self.PATH
        try:
            self.browser.get(self.browser.url + path)
            self.browser.logger.info(f"Opening url: {self.browser.url + path}")
        except Exception:
            self.browser.logger.error(f"Not opening url: {self.browser.url + path}")
            exit(1)
        with allure.step(f"Открываю {self.browser.url + path}"):
            allure.attach(body=self.browser.page_source,
                          name="Attach html",
                          attachment_type=allure.attachment_type.HTML)
        return self

    @allure.step("Достаю title страницы")
    def get_title(self):
        self.browser.logger.info(f"Return title: '{self.browser.title}'")
        return self.browser.title

    def alert(self):
        self.browser.logger.info(f"Check Alert of element '{self.ALERT}' is visibility")
        with allure.step(f"Ищу Allert {self.ALERT}"):
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name="Attach screenshot Allert",
                          attachment_type=allure.attachment_type.PNG)
        return WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.ALERT)).text

    @allure.step("Ищу элемент")
    def element(self, locator):
        self.browser.logger.info(f"Check if element '{locator}' is visibility")
        return WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(locator))

    @allure.step("Ищу элементы")
    def elements(self, locator):
        self.browser.logger.info(f"Check if elements '{locator}' is visibility")
        return WebDriverWait(self.browser, 2).until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Ввожу данные в поле")
    def _input(self, element, value):
        self.browser.logger.info(f"Input '{value}' in element")
        time.sleep(1)
        element.send_keys("\b\b\b\b\b\b")
        time.sleep(1)
        element.send_keys(value)

    @allure.step("Переключаю окно")
    def switch_to_window(self):
        handles = self.browser.window_handles
        for handle in handles:
            if handle != self.browser.current_window_handle:
                self.browser.logger.info(f"switch to second window {handle}")
                self.browser.switch_to.window(handle)

    @allure.step("Переключаю окно")
    def switch_to_back(self):
        handles = self.browser.window_handles
        for handle in handles:
            if handle == self.browser.current_window_handle:
                self.browser.logger.info(f"switch to second window {handle}")
                self.browser.switch_to.window(handle)

    @allure.step("Двойной клик мыши")
    def double_click_to_el(self, element):
        action = ActionChains(self.browser)
        action.double_click(on_element=element)
        action.perform()
