# coding: utf-8

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself. 

    OpenAPI spec version: 1.1.1
    Contact: richard@starinformatics.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.client_concept_category import ClientConceptCategory


class TestClientConceptCategory(unittest.TestCase):
    """ ClientConceptCategory unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClientConceptCategory(self):
        """
        Test ClientConceptCategory
        """
        model = swagger_client.models.client_concept_category.ClientConceptCategory()


if __name__ == '__main__':
    unittest.main()
