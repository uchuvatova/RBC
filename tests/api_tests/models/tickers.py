from datetime import datetime

import requests

from tests.api_tests.data.tickers import Tickers
from tests.api_tests.utils.helpers import assert_status_code


class TickersApiUrls:
    GET_ALL_TICKERS_BY_UNIX_NOW = f'https://www.rbc.ru/v10/ajax/key-indicator-update/?_={datetime.utcnow()}'

    def get_tickers_by_unix_now(self):
        response = requests.get(self.GET_ALL_TICKERS_BY_UNIX_NOW, verify=False)
        assert_status_code(response), "Статус код не 200"
        Tickers(**response.json()), "JSON не соответствует схеме"
        return response.json()
