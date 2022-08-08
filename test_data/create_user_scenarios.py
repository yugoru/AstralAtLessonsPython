from faker import Faker
from app_driver.owf_http_client import OwfHttpClient
from config import APP_BASE_URL
from test_data.context import TestContext
from test_data.models.viev_models import RegisterVm

faker = Faker('ru-RU')
client = OwfHttpClient(APP_BASE_URL)

SUCCESS_CREATE_USER = [
    TestContext.from_dict({
        "register": RegisterVm.from_dict({
            "email": faker.email(),
            "password": "Test123",
            "confirmPassword": "Test123",
            "lastName": faker.first_name(),
            "firstName": faker.last_name(),
            "patronymic": faker.first_name() + "ович",
            "phoneNumber": "+79999999999"
        })
    }),
    TestContext.from_dict({
        "register": RegisterVm.from_dict({
            "email": faker.email(),
            "password": "Test123",
            "confirmPassword": "Test123",
            "lastName": faker.first_name(),
            "firstName": faker.last_name(),
            "patronymic": "",
            "phoneNumber": "+79999999999"
        })
    })
]

NO_EMAIL = {
    "password": "Test123",
    "confirmPassword": "Test123",
    "lastName": faker.first_name(),
    "firstName": faker.last_name(),
    "patronymic": faker.first_name() + "ович",
    "phoneNumber": "+79999999999"
}

NO_PASSWORD = {
    "email": faker.email(),
    "confirmPassword": "Test123",
    "lastName": faker.first_name(),
    "firstName": faker.last_name(),
    "patronymic": faker.first_name() + "ович",
    "phoneNumber": "+79999999999"
}

ALREADY_REGISTERED = {
    "email": "astrallkptest@gmail.com",
    "password": "Test123",
    "confirmPassword": "Test123",
    "lastName": faker.first_name(),
    "firstName": faker.last_name(),
    "patronymic": faker.first_name() + "ович",
    "phoneNumber": "+79999999999"
}


def bad_phone(phone: str):
    return ({
        "email": faker.email(),
        "password": "Test123",
        "confirmPassword": "Test123",
        "lastName": faker.first_name(),
        "firstName": faker.last_name(),
        "patronymic": faker.first_name() + "ович",
        "phoneNumber": phone
    })


BAD_PHONE = [
    TestContext.from_dict({
        "badPhone": RegisterVm.from_dict(bad_phone("+7-999-999-99-99"))
    }),
    TestContext.from_dict({
        "badPhone": RegisterVm.from_dict(bad_phone("+34999999999"))
    }),
    TestContext.from_dict({
        "badPhone": RegisterVm.from_dict(bad_phone("99999999"))
    }),
    TestContext.from_dict({
        "badPhone": RegisterVm.from_dict(bad_phone("89999999999"))
    })
]


def assert_login_getAdmin(self, email: str):
    """Логинимся под новым юзером и проверяем успешность"""
    test_data = {
        "email": email,
        "password": "Test123",
    }
    login_response = self.http_client.login_check(test_data)
    response_body = login_response.json()
    assert login_response.status_code == 200
    assert response_body["accessToken"] is not None
    assert response_body["expiration"] is not None

    """Под администратором проверяем, что юзер есть в списке"""
    response_get_users = self.http_client.get_user_by_admin(admin_token())
    user_data = response_get_users.json()
    assert any(check_email['email'] == email for check_email in user_data['items'])


def admin_token():
    return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiQWRtaW4iLCJzdWIiOiIyOGVkMTdmYy0xMTc1LTQ1MjgtYTZhMi00ZjI0NjgzNjUzM2UiLCJqdGkiOiJjMzcwZmU0YS0zMjU1LTQ3ZGQtODVhNy0wNWZlYzgzMzExYjMiLCJleHAiOjE5NzE0NDA1NTIsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NDIwMCJ9.Ii8pPvYLetMcQuFaBL3Uqqtq9X2tn3EPl_t9rx_BeK4"



