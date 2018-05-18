# currency-converter

## Requirements

* pipenv (can be installed using: __pip install pipenv__)
* redis
* openexchangerates.org api key

## How to run

```bash
# pipenv install
# pipenv shell
# export FLASK_APP=currency_converter.py
# export REDIS_URL=redis://localhost:6379
# export OPENEXCHANGE_API_KEY="<here is your key>"`
# flask update_rates && flask run
```
