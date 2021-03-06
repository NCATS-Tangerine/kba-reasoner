# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class MessageFeedback(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, feedback_list=None):  # noqa: E501
        """MessageFeedback - a model defined in OpenAPI

        :param feedback_list: The feedback_list of this MessageFeedback.  # noqa: E501
        :type feedback_list: List[Feedback]
        """
        self.openapi_types = {
            'feedback_list': List[Feedback]
        }

        self.attribute_map = {
            'feedback_list': 'feedback_list'
        }

        self._feedback_list = feedback_list

    @classmethod
    def from_dict(cls, dikt) -> 'MessageFeedback':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MessageFeedback of this MessageFeedback.  # noqa: E501
        :rtype: MessageFeedback
        """
        return util.deserialize_model(dikt, cls)

    @property
    def feedback_list(self):
        """Gets the feedback_list of this MessageFeedback.

        List of feedback posts for this entire message  # noqa: E501

        :return: The feedback_list of this MessageFeedback.
        :rtype: List[Feedback]
        """
        return self._feedback_list

    @feedback_list.setter
    def feedback_list(self, feedback_list):
        """Sets the feedback_list of this MessageFeedback.

        List of feedback posts for this entire message  # noqa: E501

        :param feedback_list: The feedback_list of this MessageFeedback.
        :type feedback_list: List[Feedback]
        """

        self._feedback_list = feedback_list
