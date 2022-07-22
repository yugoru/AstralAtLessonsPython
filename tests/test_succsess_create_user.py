from config import APP_BASE_URL
from test_data.create_user import SCENARIO, ONLY_REQUIRED, checkLoginAfterCreate
from app_driver.owf_http_client import OwfHttpClient


class TestSuccessCreateUser:

    def setup(self):
        self.client = OwfHttpClient(APP_BASE_URL)

    def test_register(self):
        register_response = self.client.register(SCENARIO)
        response_body = register_response.json()
        assert register_response.status_code == 200
        assert response_body["message"] == "Пользователь " + SCENARIO['email'] + " успешно зарегистрирован"
        checkLoginAfterCreate(SCENARIO)

    def test_register_only_required(self):
        register_response = self.client.register(ONLY_REQUIRED)
        response_body = register_response.json()
        assert register_response.status_code == 200
        assert response_body["message"] == "Пользователь " + ONLY_REQUIRED['email'] + " успешно зарегистрирован"
        checkLoginAfterCreate(ONLY_REQUIRED)
