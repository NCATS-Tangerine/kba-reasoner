# coding: utf-8

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.   # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: richard@starinformatics.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ClientStatementsQuery(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'keywords': 'list[str]',
        'source': 'str',
        'categories': 'list[str]',
        'relations': 'list[str]',
        'query_id': 'str',
        'target': 'str'
    }

    attribute_map = {
        'keywords': 'keywords',
        'source': 'source',
        'categories': 'categories',
        'relations': 'relations',
        'query_id': 'queryId',
        'target': 'target'
    }

    def __init__(self, keywords=None, source=None, categories=None, relations=None, query_id=None, target=None):  # noqa: E501
        """ClientStatementsQuery - a model defined in OpenAPI"""  # noqa: E501

        self._keywords = None
        self._source = None
        self._categories = None
        self._relations = None
        self._query_id = None
        self._target = None
        self.discriminator = None

        if keywords is not None:
            self.keywords = keywords
        if source is not None:
            self.source = source
        if categories is not None:
            self.categories = categories
        if relations is not None:
            self.relations = relations
        if query_id is not None:
            self.query_id = query_id
        if target is not None:
            self.target = target

    @property
    def keywords(self):
        """Gets the keywords of this ClientStatementsQuery.  # noqa: E501

        'keywords' string filter parameter to call, echoed back   # noqa: E501

        :return: The keywords of this ClientStatementsQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this ClientStatementsQuery.

        'keywords' string filter parameter to call, echoed back   # noqa: E501

        :param keywords: The keywords of this ClientStatementsQuery.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def source(self):
        """Gets the source of this ClientStatementsQuery.  # noqa: E501

        'source' string parameter to call, echoed back   # noqa: E501

        :return: The source of this ClientStatementsQuery.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ClientStatementsQuery.

        'source' string parameter to call, echoed back   # noqa: E501

        :param source: The source of this ClientStatementsQuery.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def categories(self):
        """Gets the categories of this ClientStatementsQuery.  # noqa: E501

        'categories' string parameter to call, echoed back   # noqa: E501

        :return: The categories of this ClientStatementsQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this ClientStatementsQuery.

        'categories' string parameter to call, echoed back   # noqa: E501

        :param categories: The categories of this ClientStatementsQuery.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def relations(self):
        """Gets the relations of this ClientStatementsQuery.  # noqa: E501

        'relations' string parameter to call, echoed back   # noqa: E501

        :return: The relations of this ClientStatementsQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this ClientStatementsQuery.

        'relations' string parameter to call, echoed back   # noqa: E501

        :param relations: The relations of this ClientStatementsQuery.  # noqa: E501
        :type: list[str]
        """

        self._relations = relations

    @property
    def query_id(self):
        """Gets the query_id of this ClientStatementsQuery.  # noqa: E501

        session identifier of initiated query   # noqa: E501

        :return: The query_id of this ClientStatementsQuery.  # noqa: E501
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this ClientStatementsQuery.

        session identifier of initiated query   # noqa: E501

        :param query_id: The query_id of this ClientStatementsQuery.  # noqa: E501
        :type: str
        """

        self._query_id = query_id

    @property
    def target(self):
        """Gets the target of this ClientStatementsQuery.  # noqa: E501

        'target' string parameter to call, echoed back   # noqa: E501

        :return: The target of this ClientStatementsQuery.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this ClientStatementsQuery.

        'target' string parameter to call, echoed back   # noqa: E501

        :param target: The target of this ClientStatementsQuery.  # noqa: E501
        :type: str
        """

        self._target = target

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClientStatementsQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
