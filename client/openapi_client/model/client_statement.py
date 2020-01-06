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


class ClientStatement(object):
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
        'id': 'str',
        'subject': 'ClientStatementSubject',
        'predicate': 'ClientStatementPredicate',
        'object': 'ClientStatementObject',
        'beacon': 'int'
    }

    attribute_map = {
        'id': 'id',
        'subject': 'subject',
        'predicate': 'predicate',
        'object': 'object',
        'beacon': 'beacon'
    }

    def __init__(self, id=None, subject=None, predicate=None, object=None, beacon=None, local_vars_configuration=None):  # noqa: E501
        """ClientStatement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._subject = None
        self._predicate = None
        self._object = None
        self._beacon = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if subject is not None:
            self.subject = subject
        if predicate is not None:
            self.predicate = predicate
        if object is not None:
            self.object = object
        if beacon is not None:
            self.beacon = beacon

    @property
    def id(self):
        """Gets the id of this ClientStatement.  # noqa: E501

        CURIE-encoded identifier for statement (can be used to retrieve associated evidence)  # noqa: E501

        :return: The id of this ClientStatement.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClientStatement.

        CURIE-encoded identifier for statement (can be used to retrieve associated evidence)  # noqa: E501

        :param id: The id of this ClientStatement.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def subject(self):
        """Gets the subject of this ClientStatement.  # noqa: E501


        :return: The subject of this ClientStatement.  # noqa: E501
        :rtype: ClientStatementSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ClientStatement.


        :param subject: The subject of this ClientStatement.  # noqa: E501
        :type: ClientStatementSubject
        """

        self._subject = subject

    @property
    def predicate(self):
        """Gets the predicate of this ClientStatement.  # noqa: E501


        :return: The predicate of this ClientStatement.  # noqa: E501
        :rtype: ClientStatementPredicate
        """
        return self._predicate

    @predicate.setter
    def predicate(self, predicate):
        """Sets the predicate of this ClientStatement.


        :param predicate: The predicate of this ClientStatement.  # noqa: E501
        :type: ClientStatementPredicate
        """

        self._predicate = predicate

    @property
    def object(self):
        """Gets the object of this ClientStatement.  # noqa: E501


        :return: The object of this ClientStatement.  # noqa: E501
        :rtype: ClientStatementObject
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this ClientStatement.


        :param object: The object of this ClientStatement.  # noqa: E501
        :type: ClientStatementObject
        """

        self._object = object

    @property
    def beacon(self):
        """Gets the beacon of this ClientStatement.  # noqa: E501

        aggregator assigned beacon index number   # noqa: E501

        :return: The beacon of this ClientStatement.  # noqa: E501
        :rtype: int
        """
        return self._beacon

    @beacon.setter
    def beacon(self, beacon):
        """Sets the beacon of this ClientStatement.

        aggregator assigned beacon index number   # noqa: E501

        :param beacon: The beacon of this ClientStatement.  # noqa: E501
        :type: int
        """

        self._beacon = beacon

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
        if not isinstance(other, ClientStatement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientStatement):
            return True

        return self.to_dict() != other.to_dict()
