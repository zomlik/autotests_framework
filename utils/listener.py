import logging
import time

import allure
from selenium.webdriver.support.events import AbstractEventListener

from utils.test_utils import page_load, url_status

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class MonitoringListener(AbstractEventListener):
    def __init__(self):
        self.start_time = 0.0
        self.load_time = 0.0

    def before_navigate_to(self, url: str, browser) -> None:
        url_status(url)
        self.start_time = time.time()
        logging.info(f"Starting navigation to {url}")

    def after_navigate_to(self, url: str, browser) -> None:
        page_load(browser)
        end_time = time.time()
        self.load_time = self.start_time - end_time
        logging.info(f"Page loaded in {self.load_time:.2f} seconds")

    def on_exception(self, exception, browser) -> None:
        allure.attach(
            name="Скриншот",
            body=browser.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG,
        )
