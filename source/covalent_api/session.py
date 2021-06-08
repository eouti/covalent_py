# :coding: utf-8
# :copyright: Copyright (c) 2021 Lluis Casals Marsol
# Please see the LICENSE file that should have been included as part of this
# package.

import os
import json
import logging
import requests


class Session(object):
    '''Attach session authentication information to requests.'''

    @property
    def server_url(self):
        '''Return server url used for session.'''
        return self._server_url

    @property
    def api_key(self):
        '''Return API key used for session.'''
        return self._api_key

    def __init__(
            self, server_url='https://api.covalenthq.com',
            api_key=None,
            timeout=60
    ):
        '''
        Initialize Session with the given *server_url* and *api_key*

        :param server_url: Default covalent api url: https://api.covalenthq.com
            If None, will check for envar:: COVALENT_SERVER environment variable.
        :type server_url: string
        :param api_key: Personal covalent API key. If None check for
        envar:: COVALENT_API_KEY environment variable.
        :type api_key: string
        :param timeout: Timeout in case the server is not responding.
        :type timeout: float
        '''
        super(Session, self).__init__()
        logging.basicConfig()

        self.logger = logging.getLogger(
            __name__ + '.' + self.__class__.__name__
        )
        self.logger.setLevel(logging.INFO)

        #If no server_url provided check the environment variable.
        if server_url is None:
            server_url = os.environ.get('COVALENT_SERVER')

        if not server_url:
            raise TypeError(
                'Required "server_url" not specified. Pass as argument or set '
                'in environment variable COVALENT_SERVER.'
            )

        self._server_url = server_url

        #If no api_key provided check the environment variable.
        if api_key is None:
            api_key = os.environ.get('COVALENT_API_KEY')

        if not api_key:
            raise TypeError(
                'Required "api_key" not specified. Pass as argument or set in '
                'environment variable COVALENT_API_KEY.'
            )

        self._api_key = api_key

        self._request = requests.Session()
        self._request.auth = ('', self._api_key)

        self.request_timeout = timeout

    def decode(self, string):
        '''
        Return decoded JSON *string* as Python object.
        '''
        return json.loads(string)

    def encode(self, data):
        '''Return encoded *data* as JSON'''
        return json.dumps(
            data,
            sort_keys=True
        )

    def _check_params(self, params):
        '''
        Check given *params* to remove invalid ones.
        :param params: Dictionary with parameters.
        :type params: dictionary
        '''
        if not isinstance(params, dict):
            raise Exception("params should be a dicctionary")
        params_to_pop = []
        for k, v in params.items():
            if v==None:
                params_to_pop.append(k)
        for param in params_to_pop:
            params.pop(param)
        return params

    def query(self, url, params=None, decode=True):
        '''
        Query the *url* request with the given *params*

        :param url: path url to query.
        :type url: string
        :param params: Dictionary with url parameters
        :type params: dictionary
        :param decode: Json decode the returned response from the server.
            True by default.
        :type decode: boolean
        '''
        url = "{}{}".format(self._server_url, url)


        self.logger.debug("Url: {}".format(url))
        #params = self.encode(params)
        params = self._check_params(params)

        self.logger.debug("Parameters: {}".format(params))

        response = self._request.get(
            url,
            params=params,
            auth=(self._api_key, ''),
            timeout=self.request_timeout
        )

        result = response.text
        if not result:
            return result
        if decode:
            try:
                result = self.decode(result)
            except Exception as e:
                error_message = (
                    'Server reported error in unexpected format. '
                    'Raw error was: {0}. \n Exception: {1}'.format(response.text, e)
                )
                self.logger.exception(error_message)
                raise Exception(error_message)

        return result

