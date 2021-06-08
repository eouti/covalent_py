# :coding: utf-8
# :copyright: Copyright (c) 2021 Lluis Casals Marsol
# Please see the LICENSE file that should have been included as part of this
# package.

from covalent_api import constants


class ClassB(object):

    @property
    def session(self):
        return self._session

    def __init__(self, session):
        self._session = session

    def get_sushiswap_address_exchange_liquidity_transactions(
            self, chain_id, address, swaps=False
    ):
        '''
        Get Sushiswap address exchange liquidity transactions.

        :param chain_id: Chain ID of the Blockchain being queried. Currently
            supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
            for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
            Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
            Fantom Opera Mainnet.
        :type chain_id: string 
        :param address: Passing in an ENS resolves automatically.
        :type address: string
        :param swaps: Get additional insight on swap event data related to this
            address, default: false
        :type swaps: string
        '''

        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = (
            '/v1/{chain_id}/address/{address}/stacks/sushiswap/acts/'.format(
                chain_id=chain_id,
                address=address
            )
        )
        params = {
            'swaps': swaps
        }

        result = self.session.query(method_url, params, decode=True)
        return result


    def get_sushiswap_address_exchange_balances(self, chain_id, address):
        '''
        Get Sushiswap address exchange balances. Passing in an ENS resolves
        automatically.

        :param chain_id: Chain ID of the Blockchain being queried. Currently
            supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
            for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
            Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
            Fantom Opera Mainnet.
        :type chain_id: string 
        :param address: Passing in an ENS resolves automatically.
        :type address: string
        '''

        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = (
            '/v1/{chain_id}/address/{address}/stacks/sushiswap/balances/'.format(
                chain_id=chain_id,
                address=address
            )
        )
        params = {
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_sushiswap_network_assets(self, chain_id):
        '''
        Return a paginated list of Sushiswap pools sorted by exchange volume.

        :param chain_id: Chain ID of the Blockchain being queried. Currently
            supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
            for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
            Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
            Fantom Opera Mainnet.
        :type chain_id: string
        '''

        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = '/v1/{chain_id}/networks/sushiswap/assets/'.format(
                chain_id=chain_id
            )
        params = {
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_aave_v2_address_balances(self, address):
        '''
        Get Aave v2 address balances, supply and borrow positions.

        :param address: Passing in an ENS resolves automatically.
        :type address: string
        '''
        method_url = (
            '/v1/1/address/{address}/stacks/aave_v2/balances/'.format(
                address=address
            )
        )
        params = {
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_aave_address_balances(self, address):
        '''
        Get Aave address balances.

        :param address: Passing in an ENS resolves automatically.
        :type address: string
        '''
        method_url = '/v1/1/address/{address}/stacks/aave/balances/'.format(
            address=address
        )
        params = {
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_balancer_exchange_address_balances(self, address):
        '''
        Get Balancer exchange address balances.

        :param address: Passing in an ENS resolves automatically.
        :type address: string
        '''
        method_url = '/v1/1/address/{address}/stacks/balancer/balances/'.format(
            address=address
        )
        params = {
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_compound_address_activity(self, address):
        '''
        Get Compound address activity.

        :param address: Passing in an ENS resolves automatically.
        :type address: string
        '''
        method_url = '/v1/1/address/{address}/stacks/compound/acts/'.format(
            address=address
        )
        params = {
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_compound_address_balances(self, address):
        '''
        Get Compound address balances.

        :param address: Passing in an ENS resolves automatically.
        :type address: string
        '''
        method_url = '/v1/1/address/{address}/stacks/compound/balances/'.format(
            address=address
        )
        params = {
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_curve_address_balances(self, address):
        '''
        Get Curve address balances.

        :param address: Passing in an ENS resolves automatically.
        :type address: string
        '''
        method_url = '/v1/1/address/{address}/stacks/curve/balances/'.format(
            address=address
        )
        params = {
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_farming_stats(self, address):
        '''
        Get farming positions on Uniswap, Sushiswap, and Harvest.

        :param address: Passing in an ENS resolves automatically.
        :type address: string
        '''
        method_url = '/v1/1/address/{address}/stacks/farming/positions/'.format(
            address=address
        )
        params = {
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_marker_address_balances_and_acts(self, address):
        '''
        Return user activity in the MakerDAO protocol.

        Inspired by this blog post:
        https://www.covalenthq.com/blog/defi-data-availability-makerdao-csv-export/

        Some unique features:
        1) Return all backing collateral types
        2) Return vaults belonging to other sub-wallets like InstaDapp
        3) Return SHUT/CLOSED/LIQUIDATED Vaults

        :param address: Passing in an ENS resolves automatically.
        :type address: string
        '''
        method_url = '/v1/1/address/{address}/stacks/makerdao/'.format(
            address=address
        )
        params = {
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_uniswap_v1_address_exchange_balances(self, address):
        '''
        Get Uniswap v1 address exchange balances.

        :param address: Passing in an ENS resolves automatically.
        :type address: string
        '''
        method_url = (
            '/v1/1/address/{address}/stacks/uniswap_v1/balances/'.format(
                address=address
            )
        )
        params = {
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_uniswap_v2_address_exchange_liquidity_transactions(
            self, address, swaps=False
    ):
        '''
        Get Uniswap v2 address exchange liquidity transactions.

        :param address: Passing in an ENS resolves automatically.
        :type address: string
        :param swaps: Get additional insight on swap event data related to this
            address, default: false
        :type swaps: string
        '''
        method_url = '/v1/1/address/{address}/stacks/uniswap_v2/acts/'.format(
            address=address
        )
        params = {
            'swaps': swaps
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_uniswap_v2_address_exchange_balances(self, address):
        '''
        Get Uniswap v2 address exchange balances. Passing in an ENS resolves
        automatically.

        :param address: Passing in an ENS resolves automatically.
        :type address: string
        '''
        method_url = '/v1/1/address/{address}/stacks/uniswap_v2/balances/'.format(
            address=address
        )
        params = {
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_aave_v2_network_assets(self):
        '''
        Get Aave v2 network assets.
        '''
        method_url = '/v1/1/networks/aave_v2/assets/'
        params = {
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_aave_network_assets(self):
        '''
        Get Aave network assets.
        '''
        method_url = '/v1/1/networks/aave/assets/'
        params = {
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_augur_market_affiliate_fee_divisors(
            self, page_number=None, page_size=None
    ):
        '''
        Get Augur market affiliate fee divisors.

        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        '''
        method_url = '/v1/1/networks/augur/affiliate_fee/'
        params = {
            'page-number':page_number,
            'page-size':page_size
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_compound_network_assets(self):
        '''
        Get Compound network assets.
        '''
        method_url = '/v1/1/networks/compound/assets/'
        params = {
        }

        result = self.session.query(method_url, params, decode=True)
        return result

    def get_uniswap_v2_network_assets(
            self, tickers=None, page_number=None, page_size=None
    ):
        '''
        Return a paginated list of Uniswap pools sorted by exchange volume.

        :param tickers: If tickers (a comma separated list) is present, only
            return the pools that contain these tickers.
        :type tickers: string
        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        '''
        method_url = '/v1/1/networks/uniswap_v2/assets/'
        params = {
            'tickers': tickers,
            'page-number':page_number,
            'page-size':page_size
        }

        result = self.session.query(method_url, params, decode=True)
        return result