# :coding: utf-8
# :copyright: Copyright (c) 2021 Lluis Casals Marsol
# Please see the LICENSE file that should have been included as part of this
# package.


from covalent_api import constants


class Pricing(object):

    @property
    def session(self):
        return self._session

    def __init__(self, session):
        self._session = session

    def get_prices_by_address(
            self, chain_id, quote_currency, contract_address, date_from=None,
            date_to=None, prices_at_asc=False, page_number=None, page_size=None,
            format="json"
    ):
        '''
        Get historical prices for a contract_address in a particular chain_Id
        and quote_currency. Can pass to and from to define a range, by default
        if they are omitted, it returns today's price.

        :param chain_id: Chain ID of the Blockchain being queried. Currently
            supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
            for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
            Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
            Fantom Opera Mainnet.
        :type chain_id: string 
        :param quote_currency: The requested fiat currency.
        :type quote_currency: string
        :param contract_address: Smart contract address.
        :type contract_address: string
        :param date_from: The start day of the historical price range. (YYYY-MM-DD)
        :type date_from: string
        :param date_to: The end day of the historical price range. (YYYY-MM-DD)
        :type date_to: string
        :param prices_at_asc: Sort the prices in chronological ascending order.
            By default, it's set to false and returns prices in chronological
            descending order.
        :type prices_at_asc: string
        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        :param format: If format=csv, return a flat CSV instead of JSON responses.
        :type format: string
        '''
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = (
            '/v1/pricing/historical_by_address/{chain_id}/{quote_currency}/'
            '{contract_address}/'.format(
                chain_id=chain_id,
                quote_currency=quote_currency,
                contract_address=contract_address
            )
        )
        params = {
            'from': date_from,
            'to': date_to,
            'prices-at-asc': prices_at_asc,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'
        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_prices_by_addresses(
            self, chain_id, quote_currency, contract_addresses, date_from=None,
            date_to=None, prices_at_asc=False, page_number=None, page_size=None,
            format="json"
    ):
        '''
        Get historical prices for a contract_address, or a comma-separated group
        of contract_addresses in a particular chain_id and quote_currency.
        Can pass to and from to define a range, by default if they are omitted,
        it returns today's price.

        :param chain_id: Chain ID of the Blockchain being queried. Currently
            supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
            for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
            Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
            Fantom Opera Mainnet.
        :type chain_id: string 
        :param quote_currency: The requested fiat currency.
        :type quote_currency: string
        :param contract_addresses: Smart contract address(es).
        :type contract_addresses: string
        :param date_from: The start day of the historical price range. (YYYY-MM-DD)
        :type date_from: string
        :param date_to: The end day of the historical price range. (YYYY-MM-DD)
        :type date_to: string
        :param prices_at_asc: Sort the prices in chronological ascending order.
            By default, it's set to false and returns prices in chronological
            descending order.
        :type prices_at_asc: string
        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        :param format: If format=csv, return a flat CSV instead of JSON responses.
        :type format: string
        '''
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = (
            '/v1/pricing/historical_by_addresses/{chain_id}/{quote_currency}/'
            '{contract_addresses}/'.format(
                chain_id=chain_id,
                quote_currency=quote_currency,
                contract_addresses=contract_addresses
            )
        )
        params = {
            'from': date_from,
            'to': date_to,
            'prices-at-asc': prices_at_asc,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'
        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_historical_prices_by_ticker_symbol(
            self, quote_currency, ticker_symbol, date_from=None, date_to=None,
            prices_at_asc=False, page_number=None, page_size=None, format="json"
    ):
        '''
        Get historical prices for a ticker_symbol in a particular quote_currency.
        Can pass to and from to define a range, by default if they are omitted,
        it returns today's price.

        :param quote_currency: The requested fiat currency.
        :type quote_currency: string
        :param ticker_symbol:
        :type ticker_symbol: string
        :param date_from: The start day of the historical price range. (YYYY-MM-DD)
        :type date_from: string
        :param date_to: The end day of the historical price range. (YYYY-MM-DD)
        :type date_to: string
        :param prices_at_asc: Sort the prices in chronological ascending order.
            By default, it's set to false and returns prices in chronological
            descending order.
        :type prices_at_asc: string
        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        :param format: If format=csv, return a flat CSV instead of JSON responses.
        :type format: string
        '''

        method_url = (
            '/v1/pricing/historical/{quote_currency}/{ticker_symbol}/'.format(
                quote_currency=quote_currency, ticker_symbol=ticker_symbol
            )
        )
        params = {
            'from': date_from,
            'to': date_to,
            'prices-at-asc': prices_at_asc,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'
        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_spot_prices(
            self, tickers=None, page_number=None, page_size=None, format="json"
    ):
        '''
        Get spot prices and metadata for all tickers or a select group of tickers.
        Without tickers query param, it returns a paginated list of all tickers
        sorted by market cap.

        :param tickers: If tickers (a comma separated list of tickers is present),
            only return the spot prices for these tokens.
        :type tickers: string
        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        :param format: If format=csv, return a flat CSV instead of JSON responses.
        :type format: string
        '''
        method_url = '/v1/pricing/tickers/'
        params = {
            'tickers': tickers,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'
        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_price_volatility(
            self, tickers=None, page_number=None, page_size=None, format="json"
    ):
        '''
        Get price volatility and metadata for a select group of tickers.
        Without the tickers query param, it defaults to ETH volatility.

        :param tickers: If tickers (a comma separated list of tickers is present),
            only return the spot prices for these tokens.
        :type tickers: string
        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        :param format: If format=csv, return a flat CSV instead of JSON responses.
        :type format: string
        '''
        method_url = '/v1/pricing/volatility/'
        params = {
            'tickers': tickers,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'
        result = self.session.query(method_url, params, decode=decode)
        return result
