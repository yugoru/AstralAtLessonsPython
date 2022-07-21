from config import APP_BASE_URL
from test_data.create_user import SCENARIO
from app_driver.owf_http_client import OwfHttpClient


def test_success_create_user():
    #Arrange - подготовка
    client = OwfHttpClient(APP_BASE_URL)

    #Act - действие
    response = client.register(SCENARIO)

    #Assert - проверка
    assert response.status_code == 200

