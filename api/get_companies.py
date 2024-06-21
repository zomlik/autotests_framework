import allure
from api.api import ApiClient
from config.routes import Routes
from models.companies_model import CompaniesModel
from pydantic import ValidationError


class GetCompanies(ApiClient):
    @allure.step("GET запрос к companies")
    def get_companies(self):
        return self.get(Routes.GET_COMPANIES)

    @allure.step("GET запрос к companies с query limit")
    def get_companies_by_limit(self, limit):
        return self.get(Routes.GET_COMPANIES, query={"limit": limit})

    @allure.step("Проверка Json схемы")
    def json_shema_is_valid(self):
        data = self.get_json()
        try:
            CompaniesModel(**data)
        except ValidationError:
            raise ValidationError()
