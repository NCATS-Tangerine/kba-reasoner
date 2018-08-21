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


class ClientStatementObject(object):
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
        'clique': 'str',
        'id': 'str',
        'name': 'str',
        'categories': 'list[str]'
    }

    attribute_map = {
        'clique': 'clique',
        'id': 'id',
        'name': 'name',
        'categories': 'categories'
    }

    def __init__(self, clique=None, id=None, name=None, categories=None):  # noqa: E501
        """ClientStatementObject - a model defined in Swagger"""  # noqa: E501

        self._clique = None
        self._id = None
        self._name = None
        self._categories = None
        self.discriminator = None

        if clique is not None:
            self.clique = clique
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if categories is not None:
            self.categories = categories

    @property
    def clique(self):
        """Gets the clique of this ClientStatementObject.  # noqa: E501

        CURIE-encoded canonical identifier of \"equivalent concepts clique\" of the object concept   # noqa: E501

        :return: The clique of this ClientStatementObject.  # noqa: E501
        :rtype: str
        """
        return self._clique

    @clique.setter
    def clique(self, clique):
        """Sets the clique of this ClientStatementObject.

        CURIE-encoded canonical identifier of \"equivalent concepts clique\" of the object concept   # noqa: E501

        :param clique: The clique of this ClientStatementObject.  # noqa: E501
        :type: str
        """

        self._clique = clique

    @property
    def id(self):
        """Gets the id of this ClientStatementObject.  # noqa: E501

        CURIE-encoded identifier of the object concept   # noqa: E501

        :return: The id of this ClientStatementObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClientStatementObject.

        CURIE-encoded identifier of the object concept   # noqa: E501

        :param id: The id of this ClientStatementObject.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ClientStatementObject.  # noqa: E501

        human readable label of the object concept  # noqa: E501

        :return: The name of this ClientStatementObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClientStatementObject.

        human readable label of the object concept  # noqa: E501

        :param name: The name of this ClientStatementObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def categories(self):
        """Gets the categories of this ClientStatementObject.  # noqa: E501

        Semantic categories of the object concept ((see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of categories).   # noqa: E501

        :return: The categories of this ClientStatementObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this ClientStatementObject.

        Semantic categories of the object concept ((see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of categories).   # noqa: E501

        :param categories: The categories of this ClientStatementObject.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

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
        if not isinstance(other, ClientStatementObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
