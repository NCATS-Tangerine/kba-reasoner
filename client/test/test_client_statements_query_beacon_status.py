# coding: utf-8

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.   # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: richard@starinformatics.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.models.client_statements_query_beacon_status import ClientStatementsQueryBeaconStatus  # noqa: E501
from openapi_client.rest import ApiException


class TestClientStatementsQueryBeaconStatus(unittest.TestCase):
    """ClientStatementsQueryBeaconStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClientStatementsQueryBeaconStatus(self):
        """Test ClientStatementsQueryBeaconStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = openapi_client.models.client_statements_query_beacon_status.ClientStatementsQueryBeaconStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
