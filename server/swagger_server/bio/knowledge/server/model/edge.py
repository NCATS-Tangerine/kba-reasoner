# coding: utf-8

from __future__ import absolute_import
from swagger_server.bio.knowledge.server.model.edge_attribute import EdgeAttribute
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Edge(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type: str=None, relation: str=None, source_id: str=None, target_id: str=None, is_defined_by: str=None, provided_by: str=None, confidence: float=None, publications: str=None, evidence_type: str=None, qualifiers: str=None, negated: bool=None, attribute_list: List[EdgeAttribute]=None):
        """
        Edge - a model defined in Swagger

        :param type: The type of this Edge.
        :type type: str
        :param relation: The relation of this Edge.
        :type relation: str
        :param source_id: The source_id of this Edge.
        :type source_id: str
        :param target_id: The target_id of this Edge.
        :type target_id: str
        :param is_defined_by: The is_defined_by of this Edge.
        :type is_defined_by: str
        :param provided_by: The provided_by of this Edge.
        :type provided_by: str
        :param confidence: The confidence of this Edge.
        :type confidence: float
        :param publications: The publications of this Edge.
        :type publications: str
        :param evidence_type: The evidence_type of this Edge.
        :type evidence_type: str
        :param qualifiers: The qualifiers of this Edge.
        :type qualifiers: str
        :param negated: The negated of this Edge.
        :type negated: bool
        :param attribute_list: The attribute_list of this Edge.
        :type attribute_list: List[EdgeAttribute]
        """
        self.swagger_types = {
            'type': str,
            'relation': str,
            'source_id': str,
            'target_id': str,
            'is_defined_by': str,
            'provided_by': str,
            'confidence': float,
            'publications': str,
            'evidence_type': str,
            'qualifiers': str,
            'negated': bool,
            'attribute_list': List[EdgeAttribute]
        }

        self.attribute_map = {
            'type': 'type',
            'relation': 'relation',
            'source_id': 'source_id',
            'target_id': 'target_id',
            'is_defined_by': 'is_defined_by',
            'provided_by': 'provided_by',
            'confidence': 'confidence',
            'publications': 'publications',
            'evidence_type': 'evidence_type',
            'qualifiers': 'qualifiers',
            'negated': 'negated',
            'attribute_list': 'attribute_list'
        }

        self._type = type
        self._relation = relation
        self._source_id = source_id
        self._target_id = target_id
        self._is_defined_by = is_defined_by
        self._provided_by = provided_by
        self._confidence = confidence
        self._publications = publications
        self._evidence_type = evidence_type
        self._qualifiers = qualifiers
        self._negated = negated
        self._attribute_list = attribute_list

    @classmethod
    def from_dict(cls, dikt) -> 'Edge':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Edge of this Edge.
        :rtype: Edge
        """
        return deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """
        Gets the type of this Edge.
        Higher-level relationship type of this edge

        :return: The type of this Edge.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """
        Sets the type of this Edge.
        Higher-level relationship type of this edge

        :param type: The type of this Edge.
        :type type: str
        """

        self._type = type

    @property
    def relation(self) -> str:
        """
        Gets the relation of this Edge.
        Lower-level relationship type of this edge

        :return: The relation of this Edge.
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation: str):
        """
        Sets the relation of this Edge.
        Lower-level relationship type of this edge

        :param relation: The relation of this Edge.
        :type relation: str
        """

        self._relation = relation

    @property
    def source_id(self) -> str:
        """
        Gets the source_id of this Edge.
        Corresponds to the @id of source node of this edge

        :return: The source_id of this Edge.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id: str):
        """
        Sets the source_id of this Edge.
        Corresponds to the @id of source node of this edge

        :param source_id: The source_id of this Edge.
        :type source_id: str
        """

        self._source_id = source_id

    @property
    def target_id(self) -> str:
        """
        Gets the target_id of this Edge.
        Corresponds to the @id of target node of this edge

        :return: The target_id of this Edge.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id: str):
        """
        Sets the target_id of this Edge.
        Corresponds to the @id of target node of this edge

        :param target_id: The target_id of this Edge.
        :type target_id: str
        """

        self._target_id = target_id

    @property
    def is_defined_by(self) -> str:
        """
        Gets the is_defined_by of this Edge.
        A CURIE/URI for the translator group that made the KG

        :return: The is_defined_by of this Edge.
        :rtype: str
        """
        return self._is_defined_by

    @is_defined_by.setter
    def is_defined_by(self, is_defined_by: str):
        """
        Sets the is_defined_by of this Edge.
        A CURIE/URI for the translator group that made the KG

        :param is_defined_by: The is_defined_by of this Edge.
        :type is_defined_by: str
        """

        self._is_defined_by = is_defined_by

    @property
    def provided_by(self) -> str:
        """
        Gets the provided_by of this Edge.
        A CURIE/URI for the knowledge source that defined this edge

        :return: The provided_by of this Edge.
        :rtype: str
        """
        return self._provided_by

    @provided_by.setter
    def provided_by(self, provided_by: str):
        """
        Sets the provided_by of this Edge.
        A CURIE/URI for the knowledge source that defined this edge

        :param provided_by: The provided_by of this Edge.
        :type provided_by: str
        """

        self._provided_by = provided_by

    @property
    def confidence(self) -> float:
        """
        Gets the confidence of this Edge.
        Confidence metric for this edge, a value 0.0 (no confidence) and 1.0 (highest confidence)

        :return: The confidence of this Edge.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence: float):
        """
        Sets the confidence of this Edge.
        Confidence metric for this edge, a value 0.0 (no confidence) and 1.0 (highest confidence)

        :param confidence: The confidence of this Edge.
        :type confidence: float
        """

        self._confidence = confidence

    @property
    def publications(self) -> str:
        """
        Gets the publications of this Edge.
        A CURIE/URI for publications associated with this edge

        :return: The publications of this Edge.
        :rtype: str
        """
        return self._publications

    @publications.setter
    def publications(self, publications: str):
        """
        Sets the publications of this Edge.
        A CURIE/URI for publications associated with this edge

        :param publications: The publications of this Edge.
        :type publications: str
        """

        self._publications = publications

    @property
    def evidence_type(self) -> str:
        """
        Gets the evidence_type of this Edge.
        A CURIE/URI for class of evidence supporting the statement made in an edge - typically a class from the ECO ontology

        :return: The evidence_type of this Edge.
        :rtype: str
        """
        return self._evidence_type

    @evidence_type.setter
    def evidence_type(self, evidence_type: str):
        """
        Sets the evidence_type of this Edge.
        A CURIE/URI for class of evidence supporting the statement made in an edge - typically a class from the ECO ontology

        :param evidence_type: The evidence_type of this Edge.
        :type evidence_type: str
        """

        self._evidence_type = evidence_type

    @property
    def qualifiers(self) -> str:
        """
        Gets the qualifiers of this Edge.
        Terms representing qualifiers that modify or qualify the meaning of the statement made in an edge

        :return: The qualifiers of this Edge.
        :rtype: str
        """
        return self._qualifiers

    @qualifiers.setter
    def qualifiers(self, qualifiers: str):
        """
        Sets the qualifiers of this Edge.
        Terms representing qualifiers that modify or qualify the meaning of the statement made in an edge

        :param qualifiers: The qualifiers of this Edge.
        :type qualifiers: str
        """

        self._qualifiers = qualifiers

    @property
    def negated(self) -> bool:
        """
        Gets the negated of this Edge.
        Boolean that if set to true, indicates the edge statement is negated i.e. is not true

        :return: The negated of this Edge.
        :rtype: bool
        """
        return self._negated

    @negated.setter
    def negated(self, negated: bool):
        """
        Sets the negated of this Edge.
        Boolean that if set to true, indicates the edge statement is negated i.e. is not true

        :param negated: The negated of this Edge.
        :type negated: bool
        """

        self._negated = negated

    @property
    def attribute_list(self) -> List[EdgeAttribute]:
        """
        Gets the attribute_list of this Edge.
        A list of additional attributes for this edge

        :return: The attribute_list of this Edge.
        :rtype: List[EdgeAttribute]
        """
        return self._attribute_list

    @attribute_list.setter
    def attribute_list(self, attribute_list: List[EdgeAttribute]):
        """
        Sets the attribute_list of this Edge.
        A list of additional attributes for this edge

        :param attribute_list: The attribute_list of this Edge.
        :type attribute_list: List[EdgeAttribute]
        """

        self._attribute_list = attribute_list

