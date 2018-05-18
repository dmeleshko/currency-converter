from decimal import Decimal
from time import time
from typing import Dict, List

from flask_redis import FlaskRedis


class UnknownCurrencyException(Exception):
    pass


class LocalCacheOutdatedException(Exception):
    pass


class Rates(object):
    def __init__(self, local_cache: FlaskRedis, currencies: List[str]):
        self.local_cache = local_cache
        self.currencies = currencies

    def get_rate(self, currency: str, base: str = "USD") -> Decimal:
        """Get `currency` rate based on `base` currency."""
        if currency not in self.currencies:
            raise UnknownCurrencyException(f"Unknown currency `{currency}`")
        if base not in self.currencies:
            raise UnknownCurrencyException(f"Unknown currency `{base}`")
        try:
            return Decimal(self.local_cache[currency].decode()) / Decimal(self.local_cache[base].decode())
        except KeyError:
            raise LocalCacheOutdatedException("Local cache is outdated, run update_rates task")

    def convert(self, amount: Decimal, cur_from: str, cur_to: str) -> Decimal:
        """Convert amount from `cur_from` currency to `cur_to`."""
        rate = self.get_rate(cur_to, cur_from)
        return amount * rate

    def update_rates(self, new_rates: Dict[str, Decimal]):
        """Update local_cache rates from given dictionary."""
        for currency in self.currencies:
            self.local_cache[currency] = new_rates[currency]
        self.local_cache["latest_update"] = time()
