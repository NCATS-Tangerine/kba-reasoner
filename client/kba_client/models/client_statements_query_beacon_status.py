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


class ClientStatementsQueryBeaconStatus(object):
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
        'beacon': 'int',
        'status': 'int',
        'count': 'int'
    }

    attribute_map = {
        'beacon': 'beacon',
        'status': 'status',
        'count': 'count'
    }

    def __init__(self, beacon=None, status=None, count=None, local_vars_configuration=None):  # noqa: E501
        """ClientStatementsQueryBeaconStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._beacon = None
        self._status = None
        self._count = None
        self.discriminator = None

        if beacon is not None:
            self.beacon = beacon
        if status is not None:
            self.status = status
        if count is not None:
            self.count = count

    @property
    def beacon(self):
        """Gets the beacon of this ClientStatementsQueryBeaconStatus.  # noqa: E501

        Index number of beacon providing these statements   # noqa: E501

        :return: The beacon of this ClientStatementsQueryBeaconStatus.  # noqa: E501
        :rtype: int
        """
        return self._beacon

    @beacon.setter
    def beacon(self, beacon):
        """Sets the beacon of this ClientStatementsQueryBeaconStatus.

        Index number of beacon providing these statements   # noqa: E501

        :param beacon: The beacon of this ClientStatementsQueryBeaconStatus.  # noqa: E501
        :type: int
        """

        self._beacon = beacon

    @property
    def status(self):
        """Gets the status of this ClientStatementsQueryBeaconStatus.  # noqa: E501

        Http code status of beacon API - 200 means 'data ready',  102 means 'query in progress', other codes (e.g. 500) are  server errors. Once a beacon has a '200' success code,  then the /statements/data endpoint may be used to retrieve it.   # noqa: E501

        :return: The status of this ClientStatementsQueryBeaconStatus.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClientStatementsQueryBeaconStatus.

        Http code status of beacon API - 200 means 'data ready',  102 means 'query in progress', other codes (e.g. 500) are  server errors. Once a beacon has a '200' success code,  then the /statements/data endpoint may be used to retrieve it.   # noqa: E501

        :param status: The status of this ClientStatementsQueryBeaconStatus.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def count(self):
        """Gets the count of this ClientStatementsQueryBeaconStatus.  # noqa: E501

        When a 200 status code is returned, this integer designates  the number of statements matched by the query for the  given beacon.   # noqa: E501

        :return: The count of this ClientStatementsQueryBeaconStatus.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ClientStatementsQueryBeaconStatus.

        When a 200 status code is returned, this integer designates  the number of statements matched by the query for the  given beacon.   # noqa: E501

        :param count: The count of this ClientStatementsQueryBeaconStatus.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if not isinstance(other, ClientStatementsQueryBeaconStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientStatementsQueryBeaconStatus):
            return True

        return self.to_dict() != other.to_dict()
