import allure

from locators.main_page_locators import MainPageLocators
from pages.base.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Получение текста заголовка H2")
    def h2_title(self):
        return self.get_text(MainPageLocators.H2_TITLE)

    @allure.step("Клик по кнопке с текстом 'Shop New Yoga'")
    def click_on_shop_new_yoga(self):
        return self.click(MainPageLocators.SHOP_NEW_YOGA_BUTTON)
