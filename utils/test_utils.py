import requests
from selenium.webdriver.support.ui import WebDriverWait


def page_load(browser):
    return WebDriverWait(browser, 10).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )


def url_status(url: str):
    response = requests.get(url)
    assert response.status_code == 200, f"Resource status code: {response.status_code}"
