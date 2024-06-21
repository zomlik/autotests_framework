import allure

from config.routes import Routes
from data.create_user_data import Users


@allure.title("Создание пользователя")
@allure.tag("API", "User")
def test_create_user_defoult(create_users):
    create_users.create_user(Routes.CREATE_USER, json_body=Users.DATA_USER_1)
    create_users.status_code_is(201)
    create_users.json_shema_is_valid()


@allure.title("Компания с таким id не найдена")
@allure.tag("API", "Users")
def test_create_user_no_companies(create_users):
    create_users.create_user(Routes.CREATE_USER, json_body=Users.DATA_USER_2)
    create_users.status_code_is(404)
    create_users.json_error_message_is_valid()
