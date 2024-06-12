from config.urls import URLS
from pages.main_page import MainPage


def test_first(browser):
    page = MainPage(browser)
    page.open(URLS.MAIN_PAGE)
    assert page.h2_title() == "Hot Sellers"
