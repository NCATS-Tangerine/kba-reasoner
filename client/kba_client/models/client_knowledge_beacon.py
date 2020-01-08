# coding: utf-8

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.   # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Contact: richard@starinformatics.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kba_client.configuration import Configuration


class ClientKnowledgeBeacon(object):
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
        'beacon': 'int',
        'name': 'str',
        'url': 'str',
        'description': 'str',
        'contact': 'str',
        'wraps': 'str',
        'repo': 'str'
    }

    attribute_map = {
        'beacon': 'beacon',
        'name': 'name',
        'url': 'url',
        'description': 'description',
        'contact': 'contact',
        'wraps': 'wraps',
        'repo': 'repo'
    }

    def __init__(self, beacon=None, name=None, url=None, description=None, contact=None, wraps=None, repo=None, local_vars_configuration=None):  # noqa: E501
        """ClientKnowledgeBeacon - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._beacon = None
        self._name = None
        self._url = None
        self._description = None
        self._contact = None
        self._wraps = None
        self._repo = None
        self.discriminator = None

        if beacon is not None:
            self.beacon = beacon
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if description is not None:
            self.description = description
        if contact is not None:
            self.contact = contact
        if wraps is not None:
            self.wraps = wraps
        if repo is not None:
            self.repo = repo

    @property
    def beacon(self):
        """Gets the beacon of this ClientKnowledgeBeacon.  # noqa: E501

        aggregator assigned beacon index identifier   # noqa: E501

        :return: The beacon of this ClientKnowledgeBeacon.  # noqa: E501
        :rtype: int
        """
        return self._beacon

    @beacon.setter
    def beacon(self, beacon):
        """Sets the beacon of this ClientKnowledgeBeacon.

        aggregator assigned beacon index identifier   # noqa: E501

        :param beacon: The beacon of this ClientKnowledgeBeacon.  # noqa: E501
        :type: int
        """

        self._beacon = beacon

    @property
    def name(self):
        """Gets the name of this ClientKnowledgeBeacon.  # noqa: E501

        beacon name   # noqa: E501

        :return: The name of this ClientKnowledgeBeacon.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClientKnowledgeBeacon.

        beacon name   # noqa: E501

        :param name: The name of this ClientKnowledgeBeacon.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this ClientKnowledgeBeacon.  # noqa: E501

        URL used to execute API calls on the beacon   # noqa: E501

        :return: The url of this ClientKnowledgeBeacon.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ClientKnowledgeBeacon.

        URL used to execute API calls on the beacon   # noqa: E501

        :param url: The url of this ClientKnowledgeBeacon.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def description(self):
        """Gets the description of this ClientKnowledgeBeacon.  # noqa: E501

        beacon description   # noqa: E501

        :return: The description of this ClientKnowledgeBeacon.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClientKnowledgeBeacon.

        beacon description   # noqa: E501

        :param description: The description of this ClientKnowledgeBeacon.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def contact(self):
        """Gets the contact of this ClientKnowledgeBeacon.  # noqa: E501

        name of the person responsible for this beacon   # noqa: E501

        :return: The contact of this ClientKnowledgeBeacon.  # noqa: E501
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this ClientKnowledgeBeacon.

        name of the person responsible for this beacon   # noqa: E501

        :param contact: The contact of this ClientKnowledgeBeacon.  # noqa: E501
        :type: str
        """

        self._contact = contact

    @property
    def wraps(self):
        """Gets the wraps of this ClientKnowledgeBeacon.  # noqa: E501

        URL of this beacon's data source   # noqa: E501

        :return: The wraps of this ClientKnowledgeBeacon.  # noqa: E501
        :rtype: str
        """
        return self._wraps

    @wraps.setter
    def wraps(self, wraps):
        """Sets the wraps of this ClientKnowledgeBeacon.

        URL of this beacon's data source   # noqa: E501

        :param wraps: The wraps of this ClientKnowledgeBeacon.  # noqa: E501
        :type: str
        """

        self._wraps = wraps

    @property
    def repo(self):
        """Gets the repo of this ClientKnowledgeBeacon.  # noqa: E501

        URL of this beacon's repository   # noqa: E501

        :return: The repo of this ClientKnowledgeBeacon.  # noqa: E501
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this ClientKnowledgeBeacon.

        URL of this beacon's repository   # noqa: E501

        :param repo: The repo of this ClientKnowledgeBeacon.  # noqa: E501
        :type: str
        """

        self._repo = repo

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
        if not isinstance(other, ClientKnowledgeBeacon):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientKnowledgeBeacon):
            return True

        return self.to_dict() != other.to_dict()