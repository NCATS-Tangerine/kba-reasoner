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


class ClientConceptsQueryStatus(object):
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
        'status': 'list[ClientConceptsQueryBeaconStatus]'
    }

    attribute_map = {
        'query_id': 'queryId',
        'status': 'status'
    }

    def __init__(self, query_id=None, status=None, local_vars_configuration=None):  # noqa: E501
        """ClientConceptsQueryStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._query_id = None
        self._status = None
        self.discriminator = None

        if query_id is not None:
            self.query_id = query_id
        if status is not None:
            self.status = status

    @property
    def query_id(self):
        """Gets the query_id of this ClientConceptsQueryStatus.  # noqa: E501

        session identifier of a query previously initiated by /concepts   # noqa: E501

        :return: The query_id of this ClientConceptsQueryStatus.  # noqa: E501
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this ClientConceptsQueryStatus.

        session identifier of a query previously initiated by /concepts   # noqa: E501

        :param query_id: The query_id of this ClientConceptsQueryStatus.  # noqa: E501
        :type: str
        """

        self._query_id = query_id

    @property
    def status(self):
        """Gets the status of this ClientConceptsQueryStatus.  # noqa: E501

        array of beacon-specific query status reports   # noqa: E501

        :return: The status of this ClientConceptsQueryStatus.  # noqa: E501
        :rtype: list[ClientConceptsQueryBeaconStatus]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClientConceptsQueryStatus.

        array of beacon-specific query status reports   # noqa: E501

        :param status: The status of this ClientConceptsQueryStatus.  # noqa: E501
        :type: list[ClientConceptsQueryBeaconStatus]
        """

        self._status = status

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
        if not isinstance(other, ClientConceptsQueryStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientConceptsQueryStatus):
            return True

        return self.to_dict() != other.to_dict()
