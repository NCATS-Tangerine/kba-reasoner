# coding: utf-8

from __future__ import absolute_import
from swagger_server.bio.knowledge.server.model.node_attribute import NodeAttribute
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Node(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: str=None, uri: str=None, name: str=None, type: str=None, description: str=None, symbol: str=None, node_attributes: List[NodeAttribute]=None):
        """
        Node - a model defined in Swagger

        :param id: The id of this Node.
        :type id: str
        :param uri: The uri of this Node.
        :type uri: str
        :param name: The name of this Node.
        :type name: str
        :param type: The type of this Node.
        :type type: str
        :param description: The description of this Node.
        :type description: str
        :param symbol: The symbol of this Node.
        :type symbol: str
        :param node_attributes: The node_attributes of this Node.
        :type node_attributes: List[NodeAttribute]
        """
        self.swagger_types = {
            'id': str,
            'uri': str,
            'name': str,
            'type': str,
            'description': str,
            'symbol': str,
            'node_attributes': List[NodeAttribute]
        }

        self.attribute_map = {
            'id': 'id',
            'uri': 'uri',
            'name': 'name',
            'type': 'type',
            'description': 'description',
            'symbol': 'symbol',
            'node_attributes': 'node_attributes'
        }

        self._id = id
        self._uri = uri
        self._name = name
        self._type = type
        self._description = description
        self._symbol = symbol
        self._node_attributes = node_attributes

    @classmethod
    def from_dict(cls, dikt) -> 'Node':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Node of this Node.
        :rtype: Node
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """
        Gets the id of this Node.
        CURIE identifier for this node

        :return: The id of this Node.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """
        Sets the id of this Node.
        CURIE identifier for this node

        :param id: The id of this Node.
        :type id: str
        """

        self._id = id

    @property
    def uri(self) -> str:
        """
        Gets the uri of this Node.
        URI identifier for this node\"

        :return: The uri of this Node.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri: str):
        """
        Sets the uri of this Node.
        URI identifier for this node\"

        :param uri: The uri of this Node.
        :type uri: str
        """

        self._uri = uri

    @property
    def name(self) -> str:
        """
        Gets the name of this Node.
        Formal name of the entity

        :return: The name of this Node.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this Node.
        Formal name of the entity

        :param name: The name of this Node.
        :type name: str
        """

        self._name = name

    @property
    def type(self) -> str:
        """
        Gets the type of this Node.
        Entity type of this node (e.g., protein, disease, etc.)

        :return: The type of this Node.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """
        Sets the type of this Node.
        Entity type of this node (e.g., protein, disease, etc.)

        :param type: The type of this Node.
        :type type: str
        """

        self._type = type

    @property
    def description(self) -> str:
        """
        Gets the description of this Node.
        One to three sentences of description/definition of this entity

        :return: The description of this Node.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """
        Sets the description of this Node.
        One to three sentences of description/definition of this entity

        :param description: The description of this Node.
        :type description: str
        """

        self._description = description

    @property
    def symbol(self) -> str:
        """
        Gets the symbol of this Node.
        Short abbreviation or symbol for this entity

        :return: The symbol of this Node.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: str):
        """
        Sets the symbol of this Node.
        Short abbreviation or symbol for this entity

        :param symbol: The symbol of this Node.
        :type symbol: str
        """

        self._symbol = symbol

    @property
    def node_attributes(self) -> List[NodeAttribute]:
        """
        Gets the node_attributes of this Node.
        A list of arbitrary attributes for the node

        :return: The node_attributes of this Node.
        :rtype: List[NodeAttribute]
        """
        return self._node_attributes

    @node_attributes.setter
    def node_attributes(self, node_attributes: List[NodeAttribute]):
        """
        Sets the node_attributes of this Node.
        A list of arbitrary attributes for the node

        :param node_attributes: The node_attributes of this Node.
        :type node_attributes: List[NodeAttribute]
        """

        self._node_attributes = node_attributes

