import allure


@allure.title("API Test 1")
@allure.tag("API")
def test_get_companies(companies):
    companies.get_companies()
    companies.status_code_is(200)
    companies.json_shema_is_valid()


@allure.title("API Test Error")
@allure.tag("API")
def test_error_message(companies):
    companies.get_companies_by_limit("str")
    companies.status_code_is(422)
    companies.json_error_message_is_valid()
