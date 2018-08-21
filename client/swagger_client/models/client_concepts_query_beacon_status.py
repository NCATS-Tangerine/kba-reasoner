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


class ClientConceptsQueryBeaconStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, beacon=None, status=None, count=None):
        """
        ClientConceptsQueryBeaconStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'beacon': 'int',
            'status': 'int',
            'count': 'int'
        }

        self.attribute_map = {
            'beacon': 'beacon',
            'status': 'status',
            'count': 'count'
        }

        self._beacon = beacon
        self._status = status
        self._count = count

    @property
    def beacon(self):
        """
        Gets the beacon of this ClientConceptsQueryBeaconStatus.
        Index number of beacon providing these concept details 

        :return: The beacon of this ClientConceptsQueryBeaconStatus.
        :rtype: int
        """
        return self._beacon

    @beacon.setter
    def beacon(self, beacon):
        """
        Sets the beacon of this ClientConceptsQueryBeaconStatus.
        Index number of beacon providing these concept details 

        :param beacon: The beacon of this ClientConceptsQueryBeaconStatus.
        :type: int
        """

        self._beacon = beacon

    @property
    def status(self):
        """
        Gets the status of this ClientConceptsQueryBeaconStatus.
        Http code status of beacon API - 200 means 'data ready', 102 means 'query in progress', other codes (e.g. 500) are server errors. Once a beacon has a '200' success code, then the /concepts/data  endpoint may be used to retrieve it. 

        :return: The status of this ClientConceptsQueryBeaconStatus.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ClientConceptsQueryBeaconStatus.
        Http code status of beacon API - 200 means 'data ready', 102 means 'query in progress', other codes (e.g. 500) are server errors. Once a beacon has a '200' success code, then the /concepts/data  endpoint may be used to retrieve it. 

        :param status: The status of this ClientConceptsQueryBeaconStatus.
        :type: int
        """

        self._status = status

    @property
    def count(self):
        """
        Gets the count of this ClientConceptsQueryBeaconStatus.
        When a 200 status code is returned, this integer designates  the number of concepts matched by the query for the given beacon. 

        :return: The count of this ClientConceptsQueryBeaconStatus.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this ClientConceptsQueryBeaconStatus.
        When a 200 status code is returned, this integer designates  the number of concepts matched by the query for the given beacon. 

        :param count: The count of this ClientConceptsQueryBeaconStatus.
        :type: int
        """

        self._count = count

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
        if not isinstance(other, ClientConceptsQueryBeaconStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
