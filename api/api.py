import allure
import requests
from pydantic import ValidationError
from models.error_model import ErrorMessageModel


class ApiClient:
    _TIMEOUT = 10

    def __init__(self):
        self.response = None

    def get(self, url: str, query: dict = None):
        self.response = requests.get(url=url, params=query, timeout=self._TIMEOUT)

    def post(self, url: str, json_body: dict = None):
        self.response = requests.post(url=url, json=json_body, timeout=self._TIMEOUT)

    def put(self, url: str, json_body: dict = None):
        self.response = requests.put(url=url, json=json_body, timeout=self._TIMEOUT)

    def delite(self, url: str):
        self.response = requests.delete(url=url, timeout=self._TIMEOUT)

    def get_json(self):
        json_data = self.response.json()
        return json_data

    @allure.step("Cтатус код {expected_code}")
    def status_code_is(self, expected_code: int):
        actual_code = self.response.status_code
        assert actual_code == expected_code, f"Ожидаемый {actual_code}, {expected_code}"

    @allure.step("Проверка Json схемы")
    def json_error_message_is_valid(self):
        data = self.get_json()
        try:
            ErrorMessageModel(**data)
        except ValidationError:
            raise ValidationError()


