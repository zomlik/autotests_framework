import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    _TIMEOUT = 10

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Открытие страницы")
    def open(self, url: str) -> None:
        return self.browser.get(url)

    @property
    def current_url(self) -> None:
        return self.browser.current_url

    def find(self, locator: tuple) -> WebElement:
        return self.browser.find_element(*locator)

    def find_elems(self, locator: tuple) -> WebElement:
        return self.browser.find_elements(*locator)

    def get_text(self, locator: tuple) -> str:
        return self.find(locator).text

    def click(self, locator: tuple) -> None:
        return (
            wait(self.browser, timeout=self._TIMEOUT)
            .until(EC.visibility_of_element_located(locator))
            .click()
        )

    def send_text(self, text: str, locator: tuple) -> None:
        return (
            wait(self.browser, self._TIMEOUT)
            .until(EC.visibility_of_element_located(locator))
            .send_text(text)
        )
