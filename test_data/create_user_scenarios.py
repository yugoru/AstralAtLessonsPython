from faker import Faker
from app_driver.owf_http_client import OwfHttpClient
from config import APP_BASE_URL
from test_data.context import TestContext
from test_data.models.viev_models import RegisterVm, LoginVm

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
        }),
        "login": LoginVm.from_dict({
            "email": "astrallkptest@gmail.com",
            "password": "Test123"
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
        }),
        "login": LoginVm.from_dict({
            "email": "astrallkptest@gmail.com",
            "password": "Test123"
        })
    })
]

NO_EMAIL = [
    TestContext.from_dict({
        "register": RegisterVm.from_dict({
            "password": "Test123",
            "confirmPassword": "Test123",
            "email": "",
            "lastName": faker.first_name(),
            "firstName": faker.last_name(),
            "patronymic": faker.first_name() + "ович",
            "phoneNumber": "+79999999999"
        })
    })]

NO_PASSWORD = [
    TestContext.from_dict({
        "register": RegisterVm.from_dict({
            "email": faker.email(),
            "password": "",
            "confirmPassword": "Test123",
            "lastName": faker.first_name(),
            "firstName": faker.last_name(),
            "patronymic": faker.first_name() + "ович",
            "phoneNumber": "+79999999999"
        })
    })]

ALREADY_REGISTERED = [
    TestContext.from_dict({
        "register": RegisterVm.from_dict({
            "email": "astrallkptest@gmail.com",
            "password": "Test123",
            "confirmPassword": "Test123",
            "lastName": faker.first_name(),
            "firstName": faker.last_name(),
            "patronymic": faker.first_name() + "ович",
            "phoneNumber": "+79999999999"
        })
    })]

"""Пусть полежит, пока все не заменю"""

ONLY_REQUIRED = {
    "email": faker.email(),
    "password": "Test123",
    "confirmPassword": "Test123",
    "lastName": faker.first_name(),
    "firstName": faker.last_name(),
    "phoneNumber": "+79999999999"
}


def badPhone(phone: str):
    BAD_PHONE = {
        "email": faker.email(),
        "password": "Test123",
        "confirmPassword": "Test123",
        "lastName": faker.first_name(),
        "firstName": faker.last_name(),
        "phoneNumber": phone
    }
    return BAD_PHONE


"""def checkLoginAfterCreate(Scenario: str):
    login_data = {
        "email": Scenario['email'],
        "password": Scenario['password']
    }
    login_response = client.login(login_data)
    response_body = login_response.json()
    assert login_response.status_code == 200
    assert response_body["accessToken"] is not None
    assert response_body["expiration"] is not None"""
