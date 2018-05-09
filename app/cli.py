import click
from flask.cli import with_appcontext
from flask import current_app


@click.command('update_rates')
@with_appcontext
def update_rates():
    """Update rates from openxchangerates.org."""
    all_rates = current_app.rates_client.latest()
    current_app.rates.update_rates(all_rates)


def register(app):
    """Register all necessary cli commands."""
    app.cli.add_command(update_rates)