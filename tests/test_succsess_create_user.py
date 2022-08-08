import pytest

from app_driver.db_connector import DbConnector
from config import APP_BASE_URL, DB_CONNECTION_PARAMS
from test_data.context import TestContext
from test_data.create_user_scenarios import SUCCESS_CREATE_USER
from app_driver.owf_http_client import OwfHttpClient
from test_data.models.viev_models import *


@pytest.mark.incremental
@pytest.mark.parametrize('test_data', SUCCESS_CREATE_USER, scope="class")
class TestSuccessCreateUser:

    def setup_class(self):
        self.http_client = OwfHttpClient(APP_BASE_URL)
        self.db_connector = DbConnector(DB_CONNECTION_PARAMS)

    def test_register(self, test_data: TestContext):
        # Arrange
        register_data: RegisterVm = test_data.get('register')

        # Act
        response = self.http_client.register(register_data)

        # Assert
        assert response.status_code == 200

        """
        register_response = self.client.register(SUCCESS_CREATE_USER_TEST_DATA)
        response_body = register_response.json()
        assert register_response.status_code == 200
        assert response_body["message"] == "Пользователь " + SUCCESS_CREATE_USER_TEST_DATA[
            'email'] + " успешно зарегистрирован"
        checkLoginAfterCreate(SUCCESS_CREATE_USER_TEST_DATA)

    def test_register_only_required(self):
        register_response = self.client.register(ONLY_REQUIRED)
        response_body = register_response.json()
        assert register_response.status_code == 200
        assert response_body["message"] == "Пользователь " + ONLY_REQUIRED['email'] + " успешно зарегистрирован"
        checkLoginAfterCreate(ONLY_REQUIRED)

    def test_get_user_date(self):
        print(self.user_repository.get_users())
        
            def teardown(self):
        self.connection.close()
"""
