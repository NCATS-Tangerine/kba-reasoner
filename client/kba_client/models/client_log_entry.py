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

from kba_client.configuration import Configuration


class ClientLogEntry(object):
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
        'timestamp': 'str',
        'beacon': 'int',
        'query': 'str',
        'message': 'str'
    }

    attribute_map = {
        'query_id': 'queryId',
        'timestamp': 'timestamp',
        'beacon': 'beacon',
        'query': 'query',
        'message': 'message'
    }

    def __init__(self, query_id=None, timestamp=None, beacon=None, query=None, message=None, local_vars_configuration=None):  # noqa: E501
        """ClientLogEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._query_id = None
        self._timestamp = None
        self._beacon = None
        self._query = None
        self._message = None
        self.discriminator = None

        if query_id is not None:
            self.query_id = query_id
        if timestamp is not None:
            self.timestamp = timestamp
        if beacon is not None:
            self.beacon = beacon
        if query is not None:
            self.query = query
        if message is not None:
            self.message = message

    @property
    def query_id(self):
        """Gets the query_id of this ClientLogEntry.  # noqa: E501

        session identifier of initiated query   # noqa: E501

        :return: The query_id of this ClientLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this ClientLogEntry.

        session identifier of initiated query   # noqa: E501

        :param query_id: The query_id of this ClientLogEntry.  # noqa: E501
        :type: str
        """

        self._query_id = query_id

    @property
    def timestamp(self):
        """Gets the timestamp of this ClientLogEntry.  # noqa: E501

        timestamp   # noqa: E501

        :return: The timestamp of this ClientLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ClientLogEntry.

        timestamp   # noqa: E501

        :param timestamp: The timestamp of this ClientLogEntry.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def beacon(self):
        """Gets the beacon of this ClientLogEntry.  # noqa: E501

        aggregator assigned beacon index identifier   # noqa: E501

        :return: The beacon of this ClientLogEntry.  # noqa: E501
        :rtype: int
        """
        return self._beacon

    @beacon.setter
    def beacon(self, beacon):
        """Sets the beacon of this ClientLogEntry.

        aggregator assigned beacon index identifier   # noqa: E501

        :param beacon: The beacon of this ClientLogEntry.  # noqa: E501
        :type: int
        """

        self._beacon = beacon

    @property
    def query(self):
        """Gets the query of this ClientLogEntry.  # noqa: E501

        URL of the API call executed by the aggregator   # noqa: E501

        :return: The query of this ClientLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this ClientLogEntry.

        URL of the API call executed by the aggregator   # noqa: E501

        :param query: The query of this ClientLogEntry.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def message(self):
        """Gets the message of this ClientLogEntry.  # noqa: E501

        error message   # noqa: E501

        :return: The message of this ClientLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ClientLogEntry.

        error message   # noqa: E501

        :param message: The message of this ClientLogEntry.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, ClientLogEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientLogEntry):
            return True

        return self.to_dict() != other.to_dict()
