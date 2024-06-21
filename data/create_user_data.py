from models.users_model import CreateUserModel
from utils.data_generator import DataGenerator


class Users:
    DATA_USER_1 = CreateUserModel(
        first_name=DataGenerator.first_name(),
        last_name=DataGenerator.last_name(),
        company_id=1,
    )

    DATA_USER_2 = CreateUserModel(
        first_name=DataGenerator.first_name(),
        last_name=DataGenerator.last_name(),
        company_id=569345,
    )
