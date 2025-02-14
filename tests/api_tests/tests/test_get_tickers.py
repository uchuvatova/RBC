from tests.api_tests.models.tickers import TickersApiUrls


class TestTickers(TickersApiUrls):
    def test_check_ticker_under_topline(self):
        data = self.get_tickers_by_unix_now()
        items = data['shared_key_indicators_under_topline']
        for i in items:
            ticker = [i][0]['item']['ticker']
            if ticker == 'USD Нал':
                ticker_value = float([i][0]['item']['prepared']['value1'].replace(',', '.'))
                assert 60 <= ticker_value <= 120, "Значение меньше 60 или больше 120"
                break

    def test_check_ticker(self):
        data = self.get_tickers_by_unix_now()
        items = data['shared_key_indicators']
        for i in items:
            ticker = [i][0]['item']['ticker']
            if ticker == 'USD Нал':
                ticker_value = float([i][0]['item']['prepared']['value1'].replace(',', '.'))
                assert 60 <= ticker_value <= 120
                break
