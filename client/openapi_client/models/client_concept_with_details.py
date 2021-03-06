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


class ClientConceptWithDetails(object):
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
        'clique': 'str',
        'entries': 'list[ClientConceptWithDetailsBeaconEntry]',
        'aliases': 'list[str]',
        'name': 'str',
        'categories': 'list[str]'
    }

    attribute_map = {
        'clique': 'clique',
        'entries': 'entries',
        'aliases': 'aliases',
        'name': 'name',
        'categories': 'categories'
    }

    def __init__(self, clique=None, entries=None, aliases=None, name=None, categories=None):  # noqa: E501
        """ClientConceptWithDetails - a model defined in OpenAPI"""  # noqa: E501

        self._clique = None
        self._entries = None
        self._aliases = None
        self._name = None
        self._categories = None
        self.discriminator = None

        if clique is not None:
            self.clique = clique
        if entries is not None:
            self.entries = entries
        if aliases is not None:
            self.aliases = aliases
        if name is not None:
            self.name = name
        if categories is not None:
            self.categories = categories

    @property
    def clique(self):
        """Gets the clique of this ClientConceptWithDetails.  # noqa: E501

        CURIE identifying the equivalent concept clique to which the concept belongs.   # noqa: E501

        :return: The clique of this ClientConceptWithDetails.  # noqa: E501
        :rtype: str
        """
        return self._clique

    @clique.setter
    def clique(self, clique):
        """Sets the clique of this ClientConceptWithDetails.

        CURIE identifying the equivalent concept clique to which the concept belongs.   # noqa: E501

        :param clique: The clique of this ClientConceptWithDetails.  # noqa: E501
        :type: str
        """

        self._clique = clique

    @property
    def entries(self):
        """Gets the entries of this ClientConceptWithDetails.  # noqa: E501

        List of details specifically harvested from beacons, indexed by beacon   # noqa: E501

        :return: The entries of this ClientConceptWithDetails.  # noqa: E501
        :rtype: list[ClientConceptWithDetailsBeaconEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this ClientConceptWithDetails.

        List of details specifically harvested from beacons, indexed by beacon   # noqa: E501

        :param entries: The entries of this ClientConceptWithDetails.  # noqa: E501
        :type: list[ClientConceptWithDetailsBeaconEntry]
        """

        self._entries = entries

    @property
    def aliases(self):
        """Gets the aliases of this ClientConceptWithDetails.  # noqa: E501

        set of alias CURIES in the equivalent concept clique of the concept   # noqa: E501

        :return: The aliases of this ClientConceptWithDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this ClientConceptWithDetails.

        set of alias CURIES in the equivalent concept clique of the concept   # noqa: E501

        :param aliases: The aliases of this ClientConceptWithDetails.  # noqa: E501
        :type: list[str]
        """

        self._aliases = aliases

    @property
    def name(self):
        """Gets the name of this ClientConceptWithDetails.  # noqa: E501

        Canonical human readable name of the key concept of the clique   # noqa: E501

        :return: The name of this ClientConceptWithDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClientConceptWithDetails.

        Canonical human readable name of the key concept of the clique   # noqa: E501

        :param name: The name of this ClientConceptWithDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def categories(self):
        """Gets the categories of this ClientConceptWithDetails.  # noqa: E501

        Concept semantic type as a CURIE into a data type ontology   # noqa: E501

        :return: The categories of this ClientConceptWithDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this ClientConceptWithDetails.

        Concept semantic type as a CURIE into a data type ontology   # noqa: E501

        :param categories: The categories of this ClientConceptWithDetails.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

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
        if not isinstance(other, ClientConceptWithDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
