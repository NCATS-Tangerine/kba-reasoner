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

import kba_client
from kba_client.models.client_statement_annotation import ClientStatementAnnotation  # noqa: E501
from kba_client.rest import ApiException


class TestClientStatementAnnotation(unittest.TestCase):
    """ClientStatementAnnotation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClientStatementAnnotation(self):
        """Test ClientStatementAnnotation"""
        # FIXME: construct object with mandatory attributes with example values
        model = kba_client.models.client_statement_annotation.ClientStatementAnnotation()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
