from decimal import Decimal


def test_update_rates(runner):
    from app.cli import update_rates
    result = runner.invoke(update_rates)
    assert result.exit_code == 0
    assert Decimal(runner.app.rates.get_rate('USD')) == Decimal('1')
    assert Decimal(runner.app.rates.get_rate('EUR')) > Decimal('0')
