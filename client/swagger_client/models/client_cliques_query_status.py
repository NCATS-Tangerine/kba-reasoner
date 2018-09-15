# coding: utf-8

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.   # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: richard@starinformatics.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.client_cliques_query_beacon_status import ClientCliquesQueryBeaconStatus  # noqa: F401,E501


class ClientCliquesQueryStatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'query_id': 'str',
        'status': 'list[ClientCliquesQueryBeaconStatus]'
    }

    attribute_map = {
        'query_id': 'queryId',
        'status': 'status'
    }

    def __init__(self, query_id=None, status=None):  # noqa: E501
        """ClientCliquesQueryStatus - a model defined in Swagger"""  # noqa: E501

        self._query_id = None
        self._status = None
        self.discriminator = None

        if query_id is not None:
            self.query_id = query_id
        if status is not None:
            self.status = status

    @property
    def query_id(self):
        """Gets the query_id of this ClientCliquesQueryStatus.  # noqa: E501

        session identifier of a query previously initiated by /cliques   # noqa: E501

        :return: The query_id of this ClientCliquesQueryStatus.  # noqa: E501
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this ClientCliquesQueryStatus.

        session identifier of a query previously initiated by /cliques   # noqa: E501

        :param query_id: The query_id of this ClientCliquesQueryStatus.  # noqa: E501
        :type: str
        """

        self._query_id = query_id

    @property
    def status(self):
        """Gets the status of this ClientCliquesQueryStatus.  # noqa: E501

        array of beacon-specific query status reports   # noqa: E501

        :return: The status of this ClientCliquesQueryStatus.  # noqa: E501
        :rtype: list[ClientCliquesQueryBeaconStatus]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClientCliquesQueryStatus.

        array of beacon-specific query status reports   # noqa: E501

        :param status: The status of this ClientCliquesQueryStatus.  # noqa: E501
        :type: list[ClientCliquesQueryBeaconStatus]
        """

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, ClientCliquesQueryStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
