# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class QEdge(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, edge_id=None, type=None, relation=None, source_id=None, target_id=None, negated=None):  # noqa: E501
        """QEdge - a model defined in OpenAPI

        :param edge_id: The edge_id of this QEdge.  # noqa: E501
        :type edge_id: str
        :param type: The type of this QEdge.  # noqa: E501
        :type type: str
        :param relation: The relation of this QEdge.  # noqa: E501
        :type relation: str
        :param source_id: The source_id of this QEdge.  # noqa: E501
        :type source_id: str
        :param target_id: The target_id of this QEdge.  # noqa: E501
        :type target_id: str
        :param negated: The negated of this QEdge.  # noqa: E501
        :type negated: bool
        """
        self.openapi_types = {
            'edge_id': str,
            'type': str,
            'relation': str,
            'source_id': str,
            'target_id': str,
            'negated': bool
        }

        self.attribute_map = {
            'edge_id': 'edge_id',
            'type': 'type',
            'relation': 'relation',
            'source_id': 'source_id',
            'target_id': 'target_id',
            'negated': 'negated'
        }

        self._edge_id = edge_id
        self._type = type
        self._relation = relation
        self._source_id = source_id
        self._target_id = target_id
        self._negated = negated

    @classmethod
    def from_dict(cls, dikt) -> 'QEdge':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QEdge of this QEdge.  # noqa: E501
        :rtype: QEdge
        """
        return util.deserialize_model(dikt, cls)

    @property
    def edge_id(self):
        """Gets the edge_id of this QEdge.

        QueryGraph internal identifier for this QEdge. Recommended form: e00, e01, e02, etc.  # noqa: E501

        :return: The edge_id of this QEdge.
        :rtype: str
        """
        return self._edge_id

    @edge_id.setter
    def edge_id(self, edge_id):
        """Sets the edge_id of this QEdge.

        QueryGraph internal identifier for this QEdge. Recommended form: e00, e01, e02, etc.  # noqa: E501

        :param edge_id: The edge_id of this QEdge.
        :type edge_id: str
        """

        self._edge_id = edge_id

    @property
    def type(self):
        """Gets the type of this QEdge.

        Higher-level relationship type of this edge  # noqa: E501

        :return: The type of this QEdge.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QEdge.

        Higher-level relationship type of this edge  # noqa: E501

        :param type: The type of this QEdge.
        :type type: str
        """

        self._type = type

    @property
    def relation(self):
        """Gets the relation of this QEdge.

        Lower-level relationship type of this edge  # noqa: E501

        :return: The relation of this QEdge.
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        """Sets the relation of this QEdge.

        Lower-level relationship type of this edge  # noqa: E501

        :param relation: The relation of this QEdge.
        :type relation: str
        """

        self._relation = relation

    @property
    def source_id(self):
        """Gets the source_id of this QEdge.

        Corresponds to the @id of source node of this edge  # noqa: E501

        :return: The source_id of this QEdge.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this QEdge.

        Corresponds to the @id of source node of this edge  # noqa: E501

        :param source_id: The source_id of this QEdge.
        :type source_id: str
        """
        if source_id is None:
            raise ValueError("Invalid value for `source_id`, must not be `None`")  # noqa: E501

        self._source_id = source_id

    @property
    def target_id(self):
        """Gets the target_id of this QEdge.

        Corresponds to the @id of target node of this edge  # noqa: E501

        :return: The target_id of this QEdge.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this QEdge.

        Corresponds to the @id of target node of this edge  # noqa: E501

        :param target_id: The target_id of this QEdge.
        :type target_id: str
        """
        if target_id is None:
            raise ValueError("Invalid value for `target_id`, must not be `None`")  # noqa: E501

        self._target_id = target_id

    @property
    def negated(self):
        """Gets the negated of this QEdge.

        Boolean that if set to true, indicates the edge statement is negated i.e. is not true  # noqa: E501

        :return: The negated of this QEdge.
        :rtype: bool
        """
        return self._negated

    @negated.setter
    def negated(self, negated):
        """Sets the negated of this QEdge.

        Boolean that if set to true, indicates the edge statement is negated i.e. is not true  # noqa: E501

        :param negated: The negated of this QEdge.
        :type negated: bool
        """

        self._negated = negated
