# coding: utf-8

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself. 

    OpenAPI spec version: 1.1.1
    Contact: richard@starinformatics.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ClientConceptsQuery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, query_id=None, keywords=None, categories=None):
        """
        ClientConceptsQuery - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'query_id': 'str',
            'keywords': 'list[str]',
            'categories': 'list[str]'
        }

        self.attribute_map = {
            'query_id': 'queryId',
            'keywords': 'keywords',
            'categories': 'categories'
        }

        self._query_id = query_id
        self._keywords = keywords
        self._categories = categories

    @property
    def query_id(self):
        """
        Gets the query_id of this ClientConceptsQuery.
        session identifier of initiated query 

        :return: The query_id of this ClientConceptsQuery.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """
        Sets the query_id of this ClientConceptsQuery.
        session identifier of initiated query 

        :param query_id: The query_id of this ClientConceptsQuery.
        :type: str
        """

        self._query_id = query_id

    @property
    def keywords(self):
        """
        Gets the keywords of this ClientConceptsQuery.
        'keywords' string parameter to API call, echoed back 

        :return: The keywords of this ClientConceptsQuery.
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """
        Sets the keywords of this ClientConceptsQuery.
        'keywords' string parameter to API call, echoed back 

        :param keywords: The keywords of this ClientConceptsQuery.
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def categories(self):
        """
        Gets the categories of this ClientConceptsQuery.
        'categories' string parameter to API call, echoed back 

        :return: The categories of this ClientConceptsQuery.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this ClientConceptsQuery.
        'categories' string parameter to API call, echoed back 

        :param categories: The categories of this ClientConceptsQuery.
        :type: list[str]
        """

        self._categories = categories

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ClientConceptsQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
