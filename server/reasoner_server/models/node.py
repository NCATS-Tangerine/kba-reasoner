# coding: utf-8

from __future__ import absolute_import

from reasoner_server import util
from reasoner_server.models.base_model_ import Model
from reasoner_server.models.one_ofstringarray import OneOfstringarray  # noqa: E501


class Node(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, type=None):  # noqa: E501
        """Node - a model defined in OpenAPI

        :param id: The id of this Node.  # noqa: E501
        :type id: str
        :param name: The name of this Node.  # noqa: E501
        :type name: str
        :param type: The type of this Node.  # noqa: E501
        :type type: OneOfstringarray
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'type': OneOfstringarray
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type'
        }

        self._id = id
        self._name = name
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Node':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Node of this Node.  # noqa: E501
        :rtype: Node
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Node.

        CURIE identifier for this node  # noqa: E501

        :return: The id of this Node.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Node.

        CURIE identifier for this node  # noqa: E501

        :param id: The id of this Node.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Node.

        Formal name of the entity  # noqa: E501

        :return: The name of this Node.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Node.

        Formal name of the entity  # noqa: E501

        :param name: The name of this Node.
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Node.


        :return: The type of this Node.
        :rtype: OneOfstringarray
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Node.


        :param type: The type of this Node.
        :type type: OneOfstringarray
        """

        self._type = type
