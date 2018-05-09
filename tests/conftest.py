import pytest

from app import create_app
from config import Config


class TestConfig(Config):
    TESTING = True
    CURRENCIES = ['USD', 'EUR']


@pytest.fixture()
def app():
    yield create_app(TestConfig)


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
