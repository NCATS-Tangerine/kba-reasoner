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


class ClientPredicate(object):
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
        'description': 'str',
        'id': 'str',
        'uri': 'str',
        'edge_label': 'str',
        'beacons': 'list[ClientPredicatesByBeacon]'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'uri': 'uri',
        'edge_label': 'edge_label',
        'beacons': 'beacons'
    }

    def __init__(self, description=None, id=None, uri=None, edge_label=None, beacons=None):  # noqa: E501
        """ClientPredicate - a model defined in OpenAPI"""  # noqa: E501

        self._description = None
        self._id = None
        self._uri = None
        self._edge_label = None
        self._beacons = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if uri is not None:
            self.uri = uri
        if edge_label is not None:
            self.edge_label = edge_label
        if beacons is not None:
            self.beacons = beacons

    @property
    def description(self):
        """Gets the description of this ClientPredicate.  # noqa: E501

        human readable definition assigned by the beacon for the predicate relation   # noqa: E501

        :return: The description of this ClientPredicate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClientPredicate.

        human readable definition assigned by the beacon for the predicate relation   # noqa: E501

        :param description: The description of this ClientPredicate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this ClientPredicate.  # noqa: E501

        the CURIE of the predicate relation (see [Biolink Model](https://biolink.github.io/biolink-model)  # noqa: E501

        :return: The id of this ClientPredicate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClientPredicate.

        the CURIE of the predicate relation (see [Biolink Model](https://biolink.github.io/biolink-model)  # noqa: E501

        :param id: The id of this ClientPredicate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def uri(self):
        """Gets the uri of this ClientPredicate.  # noqa: E501

        the URI of the predicate relation (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of URI)  # noqa: E501

        :return: The uri of this ClientPredicate.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ClientPredicate.

        the URI of the predicate relation (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of URI)  # noqa: E501

        :param uri: The uri of this ClientPredicate.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def edge_label(self):
        """Gets the edge_label of this ClientPredicate.  # noqa: E501

        the human readable 'edge label' of the 'minimal' predicate (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of Biolink Model minimal predicates)  # noqa: E501

        :return: The edge_label of this ClientPredicate.  # noqa: E501
        :rtype: str
        """
        return self._edge_label

    @edge_label.setter
    def edge_label(self, edge_label):
        """Sets the edge_label of this ClientPredicate.

        the human readable 'edge label' of the 'minimal' predicate (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of Biolink Model minimal predicates)  # noqa: E501

        :param edge_label: The edge_label of this ClientPredicate.  # noqa: E501
        :type: str
        """

        self._edge_label = edge_label

    @property
    def beacons(self):
        """Gets the beacons of this ClientPredicate.  # noqa: E501

        list of metadata for beacons that support the use of this predicate relation   # noqa: E501

        :return: The beacons of this ClientPredicate.  # noqa: E501
        :rtype: list[ClientPredicatesByBeacon]
        """
        return self._beacons

    @beacons.setter
    def beacons(self, beacons):
        """Sets the beacons of this ClientPredicate.

        list of metadata for beacons that support the use of this predicate relation   # noqa: E501

        :param beacons: The beacons of this ClientPredicate.  # noqa: E501
        :type: list[ClientPredicatesByBeacon]
        """

        self._beacons = beacons

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
        if not isinstance(other, ClientPredicate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
