import allure
from pydantic import ValidationError

from api.api import ApiClient
from models.users_model import CreateUserModel, ResponseUserModel, UserErrorModel


class CreateUsers(ApiClient):
    @allure.step("Создание пользователя")
    def create_user(self, url: str, json_body: CreateUserModel):
        return self.post(url, json_body.model_dump())

    @allure.step("Валидация Json схемы")
    def json_error_message_is_valid(self):
        data = self.get_json()
        try:
            UserErrorModel(**data)
        except ValidationError:
            raise ValidationError()

    @allure.step("Валидация Json схемы")
    def json_shema_is_valid(self):
        data = self.get_json()
        try:
            ResponseUserModel(**data)
        except ValidationError:
            raise ValidationError()
