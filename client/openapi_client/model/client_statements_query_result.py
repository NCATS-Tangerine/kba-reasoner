# coding: utf-8

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.   # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Contact: richard@starinformatics.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ClientStatementsQueryResult(object):
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
        'query_id': 'str',
        'beacons': 'list[int]',
        'page_number': 'int',
        'page_size': 'int',
        'results': 'list[ClientStatement]'
    }

    attribute_map = {
        'query_id': 'queryId',
        'beacons': 'beacons',
        'page_number': 'pageNumber',
        'page_size': 'pageSize',
        'results': 'results'
    }

    def __init__(self, query_id=None, beacons=None, page_number=None, page_size=None, results=None, local_vars_configuration=None):  # noqa: E501
        """ClientStatementsQueryResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._query_id = None
        self._beacons = None
        self._page_number = None
        self._page_size = None
        self._results = None
        self.discriminator = None

        if query_id is not None:
            self.query_id = query_id
        if beacons is not None:
            self.beacons = beacons
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if results is not None:
            self.results = results

    @property
    def query_id(self):
        """Gets the query_id of this ClientStatementsQueryResult.  # noqa: E501

        session identifier of the query returning the results   # noqa: E501

        :return: The query_id of this ClientStatementsQueryResult.  # noqa: E501
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this ClientStatementsQueryResult.

        session identifier of the query returning the results   # noqa: E501

        :param query_id: The query_id of this ClientStatementsQueryResult.  # noqa: E501
        :type: str
        """

        self._query_id = query_id

    @property
    def beacons(self):
        """Gets the beacons of this ClientStatementsQueryResult.  # noqa: E501


        :return: The beacons of this ClientStatementsQueryResult.  # noqa: E501
        :rtype: list[int]
        """
        return self._beacons

    @beacons.setter
    def beacons(self, beacons):
        """Sets the beacons of this ClientStatementsQueryResult.


        :param beacons: The beacons of this ClientStatementsQueryResult.  # noqa: E501
        :type: list[int]
        """

        self._beacons = beacons

    @property
    def page_number(self):
        """Gets the page_number of this ClientStatementsQueryResult.  # noqa: E501

        'pageNumber' string parameter to API call, echoed back   # noqa: E501

        :return: The page_number of this ClientStatementsQueryResult.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ClientStatementsQueryResult.

        'pageNumber' string parameter to API call, echoed back   # noqa: E501

        :param page_number: The page_number of this ClientStatementsQueryResult.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this ClientStatementsQueryResult.  # noqa: E501

        'pageSize' string parameter to API call, echoed back   # noqa: E501

        :return: The page_size of this ClientStatementsQueryResult.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ClientStatementsQueryResult.

        'pageSize' string parameter to API call, echoed back   # noqa: E501

        :param page_size: The page_size of this ClientStatementsQueryResult.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def results(self):
        """Gets the results of this ClientStatementsQueryResult.  # noqa: E501


        :return: The results of this ClientStatementsQueryResult.  # noqa: E501
        :rtype: list[ClientStatement]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ClientStatementsQueryResult.


        :param results: The results of this ClientStatementsQueryResult.  # noqa: E501
        :type: list[ClientStatement]
        """

        self._results = results

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
        if not isinstance(other, ClientStatementsQueryResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientStatementsQueryResult):
            return True

        return self.to_dict() != other.to_dict()
