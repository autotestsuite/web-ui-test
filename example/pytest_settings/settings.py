import json
import os

from web_test.alternative.pytest.settings import sourced


class Settings(sourced.Settings):

    @sourced.default(6.0)
    def timeout(self): pass

    @sourced.default('gu xin')
    def author(self): pass


config = Settings(
    lambda key, _: json.load(open('settings.json')).get(key),
    os.getenv,
)
