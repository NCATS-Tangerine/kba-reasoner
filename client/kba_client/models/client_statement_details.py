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


class ClientStatementDetails(object):
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
        'is_defined_by': 'str',
        'annotation': 'list[ClientStatementAnnotation]',
        'page_number': 'int',
        'keywords': 'list[str]',
        'evidence': 'list[ClientStatementCitation]',
        'page_size': 'int',
        'provided_by': 'str',
        'qualifiers': 'list[str]',
        'id': 'str'
    }

    attribute_map = {
        'is_defined_by': 'is_defined_by',
        'annotation': 'annotation',
        'page_number': 'pageNumber',
        'keywords': 'keywords',
        'evidence': 'evidence',
        'page_size': 'pageSize',
        'provided_by': 'provided_by',
        'qualifiers': 'qualifiers',
        'id': 'id'
    }

    def __init__(self, is_defined_by=None, annotation=None, page_number=None, keywords=None, evidence=None, page_size=None, provided_by=None, qualifiers=None, id=None):  # noqa: E501
        """ClientStatementDetails - a model defined in OpenAPI"""  # noqa: E501

        self._is_defined_by = None
        self._annotation = None
        self._page_number = None
        self._keywords = None
        self._evidence = None
        self._page_size = None
        self._provided_by = None
        self._qualifiers = None
        self._id = None
        self.discriminator = None

        if is_defined_by is not None:
            self.is_defined_by = is_defined_by
        if annotation is not None:
            self.annotation = annotation
        if page_number is not None:
            self.page_number = page_number
        if keywords is not None:
            self.keywords = keywords
        if evidence is not None:
            self.evidence = evidence
        if page_size is not None:
            self.page_size = page_size
        if provided_by is not None:
            self.provided_by = provided_by
        if qualifiers is not None:
            self.qualifiers = qualifiers
        if id is not None:
            self.id = id

    @property
    def is_defined_by(self):
        """Gets the is_defined_by of this ClientStatementDetails.  # noqa: E501

        A CURIE/URI for the translator group that wrapped this knowledge source ('beacon') that publishes the statement made in an edge.   # noqa: E501

        :return: The is_defined_by of this ClientStatementDetails.  # noqa: E501
        :rtype: str
        """
        return self._is_defined_by

    @is_defined_by.setter
    def is_defined_by(self, is_defined_by):
        """Sets the is_defined_by of this ClientStatementDetails.

        A CURIE/URI for the translator group that wrapped this knowledge source ('beacon') that publishes the statement made in an edge.   # noqa: E501

        :param is_defined_by: The is_defined_by of this ClientStatementDetails.  # noqa: E501
        :type: str
        """

        self._is_defined_by = is_defined_by

    @property
    def annotation(self):
        """Gets the annotation of this ClientStatementDetails.  # noqa: E501

        Extra edge properties, generally compliant with Translator Knowledge Graph Standard Specification   # noqa: E501

        :return: The annotation of this ClientStatementDetails.  # noqa: E501
        :rtype: list[ClientStatementAnnotation]
        """
        return self._annotation

    @annotation.setter
    def annotation(self, annotation):
        """Sets the annotation of this ClientStatementDetails.

        Extra edge properties, generally compliant with Translator Knowledge Graph Standard Specification   # noqa: E501

        :param annotation: The annotation of this ClientStatementDetails.  # noqa: E501
        :type: list[ClientStatementAnnotation]
        """

        self._annotation = annotation

    @property
    def page_number(self):
        """Gets the page_number of this ClientStatementDetails.  # noqa: E501

        'pageNumber' string parameter to API call, echoed back   # noqa: E501

        :return: The page_number of this ClientStatementDetails.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ClientStatementDetails.

        'pageNumber' string parameter to API call, echoed back   # noqa: E501

        :param page_number: The page_number of this ClientStatementDetails.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def keywords(self):
        """Gets the keywords of this ClientStatementDetails.  # noqa: E501

        'keywords' string parameter to API call, echoed back   # noqa: E501

        :return: The keywords of this ClientStatementDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this ClientStatementDetails.

        'keywords' string parameter to API call, echoed back   # noqa: E501

        :param keywords: The keywords of this ClientStatementDetails.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def evidence(self):
        """Gets the evidence of this ClientStatementDetails.  # noqa: E501


        :return: The evidence of this ClientStatementDetails.  # noqa: E501
        :rtype: list[ClientStatementCitation]
        """
        return self._evidence

    @evidence.setter
    def evidence(self, evidence):
        """Sets the evidence of this ClientStatementDetails.


        :param evidence: The evidence of this ClientStatementDetails.  # noqa: E501
        :type: list[ClientStatementCitation]
        """

        self._evidence = evidence

    @property
    def page_size(self):
        """Gets the page_size of this ClientStatementDetails.  # noqa: E501

        'pageSize' string parameter to API call, echoed back   # noqa: E501

        :return: The page_size of this ClientStatementDetails.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ClientStatementDetails.

        'pageSize' string parameter to API call, echoed back   # noqa: E501

        :param page_size: The page_size of this ClientStatementDetails.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def provided_by(self):
        """Gets the provided_by of this ClientStatementDetails.  # noqa: E501

        A CURIE prefix, e.g. Pharos, MGI, Monarch. The group that curated/asserted the statement made in an edge.   # noqa: E501

        :return: The provided_by of this ClientStatementDetails.  # noqa: E501
        :rtype: str
        """
        return self._provided_by

    @provided_by.setter
    def provided_by(self, provided_by):
        """Sets the provided_by of this ClientStatementDetails.

        A CURIE prefix, e.g. Pharos, MGI, Monarch. The group that curated/asserted the statement made in an edge.   # noqa: E501

        :param provided_by: The provided_by of this ClientStatementDetails.  # noqa: E501
        :type: str
        """

        self._provided_by = provided_by

    @property
    def qualifiers(self):
        """Gets the qualifiers of this ClientStatementDetails.  # noqa: E501

        (Optional) terms representing qualifiers that modify or qualify the meaning of the statement made in an edge.   # noqa: E501

        :return: The qualifiers of this ClientStatementDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._qualifiers

    @qualifiers.setter
    def qualifiers(self, qualifiers):
        """Sets the qualifiers of this ClientStatementDetails.

        (Optional) terms representing qualifiers that modify or qualify the meaning of the statement made in an edge.   # noqa: E501

        :param qualifiers: The qualifiers of this ClientStatementDetails.  # noqa: E501
        :type: list[str]
        """

        self._qualifiers = qualifiers

    @property
    def id(self):
        """Gets the id of this ClientStatementDetails.  # noqa: E501

        Statement identifier of the statement made in an edge (echoed back)   # noqa: E501

        :return: The id of this ClientStatementDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClientStatementDetails.

        Statement identifier of the statement made in an edge (echoed back)   # noqa: E501

        :param id: The id of this ClientStatementDetails.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, ClientStatementDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
