# :coding: utf-8
# :copyright: Copyright (c) 2021 Lluis Casals Marsol
# Please see the LICENSE file that should have been included as part of this
# package.

import os
import logging

from covalent_api import url_utils as utils
import covalent_api

logging.basicConfig()
logger = logging.getLogger('Tests')
logger.setLevel(logging.INFO)



args_dict = {
    'chain_id': '1',
    'address': '0x74c1e4b8cae59269ec1d85d3d4f324396048f4ac',
    'block_height': '1',
    'starting_block': '1',
    'ending_block': '3',
    'topic': '0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925',
    'token_id': '123',
    'id': 'all',
    'tx_hash': '0x77cff4d41d028c10f5fa1ecbc8c899ce537332e9833d4477bbde110e7bc5b5e6',
    'quote_currency': 'EUR',
    'contract_address': '0xB8c77482e45F1F44dE1745F52C74426C631bDD52',
    'contract_addresses': '0xB8c77482e45F1F44dE1745F52C74426C631bDD52',
    'ticker_symbol': 'ETH'
}

#Test class methods
def test_class(cls, class_methods):
    log_errors = []

    for meth_name in class_methods:
        meth = getattr(cls, meth_name)
        required_args, optional_arguments = utils.get_method_arguments(meth)
        meth_args = {}
        for k, v in args_dict.items():
            if k in required_args:
                meth_args[k] = v
        if meth_name == 'get_all_contract_metadata':
            meth_args['chain_id'] = '56'
        try:
            result = meth(**meth_args)
        except Exception as e:
            raise Exception(
                "Could not execute the method {}. \n Arguments: {} \n Error: {}".format(
                    meth_name, meth_args, e
                )
            )

        if not result:
            log_errors.append({'method_name': meth_name, 'result': result})
            logger.debug("meth: {}".format(meth_name))
            logger.debug("result: {}".format(result))
            logger.debug("Test Error")
            logger.debug("******************************")
            continue
        if isinstance(result, dict):
            if result.get('error'):
                log_errors.append({'method_name': meth_name, 'result': result})
                logger.debug("meth: {}".format(meth_name))
                logger.debug("result: {}".format(result))
                logger.debug("Test Error")
                logger.debug("******************************")
                continue
        else:
            log_errors.append({'method_name': meth_name, 'result': result})
            logger.debug("meth: {}".format(meth_name))
            logger.debug("result: {}".format(result))
            logger.debug("Test Error")
            logger.debug("******************************")
            continue

        logger.debug("meth: {}".format(meth_name))
        logger.debug("result: {}".format(result))
        logger.debug("Test OK")
        logger.debug("******************************")

    print("Class {} test result: ".format(cls))
    if log_errors:
        print("The following errors found:")
        for log_error in log_errors:
            print(
                "{}:\n result: {}".format(
                    log_error.get('method_name'),
                    log_error.get('result')
                )
            )
    else:
        print("No errors found")

    print("################################# \n")
    return log_errors


# Create session
session = covalent_api.Session(
    server_url='https://api.covalenthq.com',
    api_key=os.environ.get('COVALENT_API_KEY')
)

#Test class a
class_a = covalent_api.ClassA(session)
class_a_methods = utils.get_class_methods(covalent_api.ClassA)
errors_a = test_class(class_a, class_a_methods)

#Test class b
class_b = covalent_api.ClassB(session)
class_b_methods = utils.get_class_methods(covalent_api.ClassB)
errors_b = test_class(class_b, class_b_methods)

#Test class pricing
class_prices = covalent_api.Pricing(session)
class_prices_methods = utils.get_class_methods(covalent_api.Pricing)
errors_prices = test_class(class_prices, class_prices_methods)
