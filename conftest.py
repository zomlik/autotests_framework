import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.events import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager

from api.create_users import CreateUsers
from api.get_companies import GetCompanies
from utils.listener import MonitoringListener


@pytest.fixture()
def browser_options():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--headless=new")
    return options


@pytest.fixture()
def browser(browser_options):
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=browser_options
    )
    driver.implicitly_wait(10)
    event_listener = MonitoringListener()
    e_driver = EventFiringWebDriver(driver, event_listener)
    yield e_driver
    e_driver.quit()


@pytest.fixture()
def companies():
    return GetCompanies()


@pytest.fixture()
def create_users():
    return CreateUsers()
