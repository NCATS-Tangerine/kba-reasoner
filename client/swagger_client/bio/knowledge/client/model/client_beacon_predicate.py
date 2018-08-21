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


class ClientBeaconPredicate(object):
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
        'id': 'str',
        'uri': 'str',
        'relation': 'str',
        'description': 'str',
        'frequency': 'int'
    }

    attribute_map = {
        'id': 'id',
        'uri': 'uri',
        'relation': 'relation',
        'description': 'description',
        'frequency': 'frequency'
    }

    def __init__(self, id=None, uri=None, relation=None, description=None, frequency=None):  # noqa: E501
        """ClientBeaconPredicate - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._uri = None
        self._relation = None
        self._description = None
        self._frequency = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if uri is not None:
            self.uri = uri
        if relation is not None:
            self.relation = relation
        if description is not None:
            self.description = description
        if frequency is not None:
            self.frequency = frequency

    @property
    def id(self):
        """Gets the id of this ClientBeaconPredicate.  # noqa: E501

        the 'local' CURIE-encoded identifier of a maximal predicate relation, as published by  the given beacon   # noqa: E501

        :return: The id of this ClientBeaconPredicate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClientBeaconPredicate.

        the 'local' CURIE-encoded identifier of a maximal predicate relation, as published by  the given beacon   # noqa: E501

        :param id: The id of this ClientBeaconPredicate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def uri(self):
        """Gets the uri of this ClientBeaconPredicate.  # noqa: E501

        the 'local' URI of a maximal predicate relation,  as published by the given beacon   # noqa: E501

        :return: The uri of this ClientBeaconPredicate.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ClientBeaconPredicate.

        the 'local' URI of a maximal predicate relation,  as published by the given beacon   # noqa: E501

        :param uri: The uri of this ClientBeaconPredicate.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def relation(self):
        """Gets the relation of this ClientBeaconPredicate.  # noqa: E501

        the human readable 'relation of the 'maximal' predicate (see the [Biolink Model](https://biolink.github.io/biolink-model) for a list of Biolink maximal predicates; this field may map onto beacon-specific non-Biolink relations   # noqa: E501

        :return: The relation of this ClientBeaconPredicate.  # noqa: E501
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        """Sets the relation of this ClientBeaconPredicate.

        the human readable 'relation of the 'maximal' predicate (see the [Biolink Model](https://biolink.github.io/biolink-model) for a list of Biolink maximal predicates; this field may map onto beacon-specific non-Biolink relations   # noqa: E501

        :param relation: The relation of this ClientBeaconPredicate.  # noqa: E501
        :type: str
        """

        self._relation = relation

    @property
    def description(self):
        """Gets the description of this ClientBeaconPredicate.  # noqa: E501

        human readable definition of the given  predicate relation   # noqa: E501

        :return: The description of this ClientBeaconPredicate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClientBeaconPredicate.

        human readable definition of the given  predicate relation   # noqa: E501

        :param description: The description of this ClientBeaconPredicate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def frequency(self):
        """Gets the frequency of this ClientBeaconPredicate.  # noqa: E501

        the number of instances of the specified predicate relation is used in statements within the given beacon   # noqa: E501

        :return: The frequency of this ClientBeaconPredicate.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this ClientBeaconPredicate.

        the number of instances of the specified predicate relation is used in statements within the given beacon   # noqa: E501

        :param frequency: The frequency of this ClientBeaconPredicate.  # noqa: E501
        :type: int
        """

        self._frequency = frequency

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
        if not isinstance(other, ClientBeaconPredicate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
