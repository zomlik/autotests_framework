from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url: str) -> None:
        return self.browser.get(url)

    def find(self, locator: tuple) -> WebElement:
        return self.browser.find_elements(*locator)

    def find_elems(self, locator: tuple) -> WebElement:
        return self.browser.find_elements(*locator)

    def get_text(self, locator: tuple) -> str:
        return self.find(locator).text

    def current_url(self) -> str:
        return self.browser.current_url
