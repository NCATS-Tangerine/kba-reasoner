# coding: utf-8

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.   # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: richard@starinformatics.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import
from sys import stderr

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
        """Test case for get_beacons

        """
        beacons = self.api.get_beacons()
        for beacon in beacons:
            print(beacon,sep='',end='',file=stderr)

    def test_get_concept_categories(self):
        """Test case for get_concept_categories

        """
        pass

    def test_get_errors(self):
        """Test case for get_errors

        """
        pass

    def test_get_knowledge_map(self):
        """Test case for get_knowledge_map

        """
        pass

    def test_get_predicates(self):
        """Test case for get_predicates

        """
        pass


if __name__ == '__main__':
    unittest.main()
