import allure
import requests
from pydantic import ValidationError

from models.error_model import ValidationErrorModel
from utils.logger import log


class ApiClient:
    _TIMEOUT = 10

    def __init__(self):
        self.response = None

    def get(self, url: str, query: dict = None):
        self.response = requests.get(url=url, params=query, timeout=self._TIMEOUT)
        log(response=self.response)

    def post(self, url: str, json_body: dict = None):
        self.response = requests.post(url=url, json=json_body, timeout=self._TIMEOUT)
        log(response=self.response, json=json_body)

    def put(self, url: str, json_body: dict = None):
        self.response = requests.put(url=url, json=json_body, timeout=self._TIMEOUT)
        log(response=self.response, json=json_body)

    def delite(self, url: str):
        self.response = requests.delete(url=url, timeout=self._TIMEOUT)
        log(response=self.response)

    def get_json(self):
        json_data = self.response.json()
        return json_data

    @allure.step("Cтатус код {expected_code}")
    def status_code_is(self, expected_code: int):
        actual_code = self.response.status_code
        assert actual_code == expected_code, f"Ожидаемый {actual_code}, {expected_code}"

    @allure.step("Проверка Json схемы")
    def json_validation_error_shema_is_valid(self):
        data = self.get_json()
        try:
            ValidationErrorModel(**data)
        except ValidationError:
            raise ValidationError()
