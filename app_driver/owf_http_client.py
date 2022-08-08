from urllib.parse import urljoin
import requests
from requests import Response

from test_data.models.viev_models import RegisterVm, LoginVm


class OwfHttpClient:
    LOGIN_ROUT = "api/auth/login"
    REGISTER_ROUTE = "api/auth/register"
    GET_USER_ROUTE = "api/auth/requisites"

    def __init__(self, base_url: str):
        """
        Инициализатор класса
        параметр base_url - базовый url тестируемого приложения
        """
        self.base_url = base_url

    def register(self, register_vm: RegisterVm) -> Response:
        """
        Отправка запроса на регистрацию
            :param register_vm:
            :param register_vm: данные запроса регистрации
            :return: объект, содержащий ответ запроса
        """
        return requests.post(
            url=urljoin(self.base_url, self.REGISTER_ROUTE),
            json=register_vm.to_dict())

    def login(self, login_vm: LoginVm) -> Response:
        """
        Отправка запроса на авторизацию пользователя
            :param login_vm: данные запроса авторизации
            :return: объект, содержащий ответ запроса
        """
        return requests.post(
            url=urljoin(self.base_url, self.LOGIN_ROUT),
            json=login_vm.to_dict())

    def get_user_requisites(self, token: str) -> Response:

        return requests.get(
            url=urljoin(self.base_url, self.GET_USER_ROUTE),
            headers={'Authorisation': f'Bearer {token}'}
        )
