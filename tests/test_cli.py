def test_update_rates(runner):
    from app.cli import update_rates
    result = runner.invoke(update_rates)
    assert result.exit_code == 0
    assert float(runner.app.rates.local_cache['USD']) == 1
    assert float(runner.app.rates.local_cache['EUR']) > 0
