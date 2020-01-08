# coding: utf-8

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.   # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Contact: richard@starinformatics.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kba_client
from kba_client.api.statements_api import StatementsApi  # noqa: E501
from kba_client.rest import ApiException


class TestStatementsApi(unittest.TestCase):
    """StatementsApi unit test stubs"""

    def setUp(self):
        self.api = kba_client.api.statements_api.StatementsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_statement_details(self):
        """Test case for get_statement_details

        """
        pass

    def test_get_statements_query(self):
        """Test case for get_statements_query

        """
        pass

    def test_get_statements_query_status(self):
        """Test case for get_statements_query_status

        """
        pass

    def test_post_statements_query(self):
        """Test case for post_statements_query

        """
        pass


if __name__ == '__main__':
    unittest.main()
