# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from reasoner_server.models.base_model_ import Model
from reasoner_server.models.edge import Edge  # noqa: F401,E501
from reasoner_server.models.node import Node  # noqa: F401,E501
from reasoner_server import util


class ResultGraph(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, node_list: List[Node]=None, edge_list: List[Edge]=None):  # noqa: E501
        """ResultGraph - a model defined in OpenAPI

        :param node_list: The node_list of this ResultGraph.  # noqa: E501
        :type node_list: List[Node]
        :param edge_list: The edge_list of this ResultGraph.  # noqa: E501
        :type edge_list: List[Edge]
        """
        self.openapi_types = {
            'node_list': List[Node],
            'edge_list': List[Edge]
        }

        self.attribute_map = {
            'node_list': 'node_list',
            'edge_list': 'edge_list'
        }

        self._node_list = node_list
        self._edge_list = edge_list

    @classmethod
    def from_dict(cls, dikt) -> 'ResultGraph':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Result_graph of this ResultGraph.  # noqa: E501
        :rtype: ResultGraph
        """
        return util.deserialize_model(dikt, cls)

    @property
    def node_list(self) -> List[Node]:
        """Gets the node_list of this ResultGraph.


        :return: The node_list of this ResultGraph.
        :rtype: List[Node]
        """
        return self._node_list

    @node_list.setter
    def node_list(self, node_list: List[Node]):
        """Sets the node_list of this ResultGraph.


        :param node_list: The node_list of this ResultGraph.
        :type node_list: List[Node]
        """

        self._node_list = node_list

    @property
    def edge_list(self) -> List[Edge]:
        """Gets the edge_list of this ResultGraph.


        :return: The edge_list of this ResultGraph.
        :rtype: List[Edge]
        """
        return self._edge_list

    @edge_list.setter
    def edge_list(self, edge_list: List[Edge]):
        """Sets the edge_list of this ResultGraph.


        :param edge_list: The edge_list of this ResultGraph.
        :type edge_list: List[Edge]
        """

        self._edge_list = edge_list