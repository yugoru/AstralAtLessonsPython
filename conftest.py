from collections import defaultdict

import psycopg2
import pytest

from app_driver.owf_http_client import OwfHttpClient
from app_driver.repositories.user_repository import UserRepository
from config import DB_CONNECTION_PARAMS, APP_BASE_URL


@pytest.fixture(scope="session")
def http_client():
    """ Предусловие"""
    return OwfHttpClient(APP_BASE_URL)


@pytest.fixture(scope="session")
def db_connect():
    connection = psycopg2.connect(
        dbname=DB_CONNECTION_PARAMS.get('dbname'),
        user=DB_CONNECTION_PARAMS.get('user'),
        password=DB_CONNECTION_PARAMS.get('password'),
        host=DB_CONNECTION_PARAMS.get('host')
    )
    yield UserRepository(connection)
    connection.close()


@pytest.fixture(scope="class")
def del_user_bd(db_connect):
    yield
    db_connect.delete_users()


# Код ниже отвечает за пропуск тестов(шагов) внутри одного класса, если хоть один из них упал.
__TEST_FAILED_INCREMENTAL = defaultdict(dict)


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None and call.excinfo.typename != "Skipped":
            param = tuple(item.callspec.indices.values()) if hasattr(item, "callspec") else ()
            __TEST_FAILED_INCREMENTAL[str(item.cls)].setdefault(param, item.originalname or item.name)


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        param = tuple(item.callspec.indices.values()) if hasattr(item, "callspec") else ()
        originalname = __TEST_FAILED_INCREMENTAL[str(item.cls)].get(param)
        if originalname:
            pytest.xfail("previous test failed ({})".format(originalname))