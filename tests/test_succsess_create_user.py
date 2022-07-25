import psycopg2

from config import APP_BASE_URL, DB_CONNECTION_PARAMS
from test_data.create_user import SCENARIO, ONLY_REQUIRED, checkLoginAfterCreate
from app_driver.owf_http_client import OwfHttpClient
from app_driver.user_repository import UserRepository


class TestSuccessCreateUser:

    def setup(self):
        self.client = OwfHttpClient(APP_BASE_URL)
        self.connection = psycopg2.connect(
            dbname=DB_CONNECTION_PARAMS('dbname'),
            user=DB_CONNECTION_PARAMS('user'),
            password=DB_CONNECTION_PARAMS('password'),
            host=DB_CONNECTION_PARAMS('host')
        )
        self.user_repository = UserRepository(self.connection)

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

    def test_get_user_date(self):
        self.user_repository.get_users()

    def teardown(self):
        self.connection.close()
