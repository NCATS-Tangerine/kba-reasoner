# coding: utf-8

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.   # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: richard@starinformatics.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import, print_function

import sys
import json

import unittest

import kba_client
from kba_client.api.metadata_api import MetadataApi  # noqa: E501
from kba_client.rest import ApiException


class TestMetadataApi(unittest.TestCase):
    """MetadataApi unit test stubs"""

    def setUp(self):
        self.api = kba_client.api.metadata_api.MetadataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_beacons(self):
        """
        Test case for get_beacons
        """
        beacon_list = self.api.get_beacons()
        for ckb in beacon_list:
            print(ckb, sep='\n', end='\n', file=sys.stderr)

    def test_get_concept_categories(self):
        """
        Test case for get_concept_categories
        """
        categories = self.api.get_concept_categories()
        for cc in categories:
            print(cc, sep='\n', end='\n', file=sys.stderr)

    def test_get_errors(self):
        """
        Test case for get_errors
        """
        pass

    def test_get_knowledge_map(self):
        """
        Test case for get_knowledge_map
        """
        knowledge_map = self.api.get_knowledge_map(_request_timeout=(600,600))
        for km in knowledge_map:
            print(km, sep='\n', end='\n', file=sys.stderr)

    def test_get_predicates(self):
        """
        Test case for get_predicates
        """
        predicates = self.api.get_predicates(_request_timeout=(300,300))
        for p in predicates:
            print(p, sep='\n', end='\n', file=sys.stderr)

if __name__ == '__main__':
    unittest.main()
