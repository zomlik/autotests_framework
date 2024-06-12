from locators.main_page_locators import MainPageLocators
from pages.base.base import BasePage


class MainPage(BasePage):
    def h2_title(self):
        return self.get_text(MainPageLocators.H2_TITLE)
