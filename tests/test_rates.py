import pytest

from app.rates import UnknownCurrencyException, LocalCacheOutdatedException


def test_get_rate(app):
    with pytest.raises(LocalCacheOutdatedException):
        r = app.rates.get_rate('USD')

    app.rates.update_rates({'USD': 1, 'EUR': 0.89, 'AUD': 2})

    assert app.rates.get_rate('USD') == 1
    assert app.rates.get_rate('EUR') == 0.89
    assert app.rates.get_rate('USD', 'EUR') == 1/0.89

    with pytest.raises(UnknownCurrencyException):
        r = app.rates.get_rate('AUD')


def test_convert(app):
    app.rates.update_rates({'USD': 1, 'EUR': 0.89, 'AUD': 2})

    with pytest.raises(UnknownCurrencyException):
        r = app.rates.convert(1, 'AUD', 'USD')

    assert app.rates.convert(1, 'USD', 'USD') == 1
    assert app.rates.convert(1, 'USD', 'EUR') == 0.89
    assert app.rates.convert(1, 'EUR', 'USD') == 1/0.89
