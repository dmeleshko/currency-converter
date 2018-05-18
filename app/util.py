from decimal import Decimal

from werkzeug.routing import BaseConverter


class DecimalConverter(BaseConverter):

    def to_python(self, value):
        return Decimal(value.decode())

    def to_url(self, value):
        return str(value)
