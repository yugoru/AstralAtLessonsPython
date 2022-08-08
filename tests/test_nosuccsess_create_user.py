from config import APP_BASE_URL
from test_data.create_user_scenarios import NO_EMAIL, NO_PASSWORD, ALREADY_REGISTERED
from app_driver.owf_http_client import OwfHttpClient
from test_data.create_user_scenarios import badPhone


class TestNoSuccessCreateUser:

    def setup(self):
        self.client = OwfHttpClient(APP_BASE_URL)

    def test_register_no_email(self):
        register_response = self.client.register(NO_EMAIL)
        response_body = register_response.json()
        assert register_response.status_code == 400
        assert response_body["errors"]["Email"] == ["The Email field is required."]

    def test_register_no_password(self):
        register_response = self.client.register(NO_PASSWORD)
        response_body = register_response.json()
        assert register_response.status_code == 400
        assert response_body["errors"]["Password"] == ["The Password field is required."]

    def test_register_badphone_other_country(self):
        register_response = self.client.register(badPhone("+34999999999"))
        response_body = register_response.json()
        assert register_response.status_code == 400
        assert response_body["errorMessage"] == "Номер телефона должен соответствовать регулярному выражению ^\\+7\\d{10}$"

    def test_register_badphone_noprefix(self):
        register_response = self.client.register(badPhone("999999999"))
        response_body = register_response.json()
        assert register_response.status_code == 400
        assert response_body["errorMessage"] == "Номер телефона должен соответствовать регулярному выражению ^\\+7\\d{10}$"

    def test_register_already_registered(self):
        register_response = self.client.register(ALREADY_REGISTERED)
        response_body = register_response.json()
        assert register_response.status_code == 400
        assert response_body["errorMessage"] == "Пользователь с Email: " + ALREADY_REGISTERED['email'] + " уже зарегистрирован"
