import allure

from config.urls import URLS
from pages.main_page import MainPage


@allure.title("Первый тест")
@allure.tag("UI", "Main Page")
@allure.severity("Critical")
def test_first(browser):
    page = MainPage(browser)
    page.open(URLS.MAIN_PAGE)
    with allure.step("Проверка заголовка H2"):
        assert page.h2_title() == "Hot Sellers1"
    with allure.step("Проверка url текущей страницы"):
        assert page.current_url() == URLS.MAIN_PAGE


@allure.title("Второй тест")
@allure.tag("UI", "URL", "Main Page")
def test_clik_on_button(browser):
    page = MainPage(browser)
    page.open(URLS.MAIN_PAGE)
    page.click_on_shop_new_yoga()
    with allure.step("Проверка перехода на страницу 'Shop New Yoga'"):
        assert page.current_url() == URLS.YOGA_PAGE
