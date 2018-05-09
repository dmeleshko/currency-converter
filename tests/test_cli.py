import pytest

from app import create_app
from config import Config
from flask.testing import CliRunner


class TestConfig(Config):
    TESTING = True
    CURRENCIES = ['USD', 'EUR']


@pytest.fixture
def cli_runner():
    app = create_app(TestConfig)
    return app.test_cli_runner()


def test_update_rates(cli_runner: CliRunner):
    from app.cli import update_rates
    result = cli_runner.invoke(update_rates)
    assert result.exit_code == 0
    assert float(cli_runner.app.rates.local_cache['USD']) == 1
    assert float(cli_runner.app.rates.local_cache['EUR']) > 0
