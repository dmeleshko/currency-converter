import pytest
from decimal import Decimal
from app.rates import UnknownCurrencyException, LocalCacheOutdatedException


def test_get_rate(app):
    with pytest.raises(LocalCacheOutdatedException):
        r = app.rates.get_rate('USD')

    app.rates.update_rates({'USD': Decimal('1'), 'EUR': Decimal('0.89'), 'AUD': Decimal('2')})

    assert app.rates.get_rate('USD') == Decimal('1')
    assert app.rates.get_rate('EUR') == Decimal('0.89')
    assert app.rates.get_rate('USD', 'EUR') == Decimal('1')/Decimal('0.89')

    with pytest.raises(UnknownCurrencyException):
        r = app.rates.get_rate('AUD')


def test_convert(app):
    app.rates.update_rates({'USD': Decimal('1'), 'EUR': Decimal('0.89'), 'AUD': Decimal('2')})

    with pytest.raises(UnknownCurrencyException):
        r = app.rates.convert(Decimal('1'), 'AUD', 'USD')

    assert app.rates.convert(Decimal('1'), 'USD', 'USD') == Decimal('1')
    assert app.rates.convert(Decimal('1'), 'USD', 'EUR') == Decimal('0.89')
    assert app.rates.convert(Decimal('1'), 'EUR', 'USD') == Decimal('1')/Decimal('0.89')
