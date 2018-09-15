# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from reasoner_server.models.base_model_ import Model
from reasoner_server import util


class Feedback(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, result_id: str=None, expertise_level_id: int=None, rating_id: int=None, commenter_id: int=None, commenter_full_name: str=None, datetime: str=None, comment: str=None):  # noqa: E501
        """Feedback - a model defined in OpenAPI

        :param id: The id of this Feedback.  # noqa: E501
        :type id: str
        :param result_id: The result_id of this Feedback.  # noqa: E501
        :type result_id: str
        :param expertise_level_id: The expertise_level_id of this Feedback.  # noqa: E501
        :type expertise_level_id: int
        :param rating_id: The rating_id of this Feedback.  # noqa: E501
        :type rating_id: int
        :param commenter_id: The commenter_id of this Feedback.  # noqa: E501
        :type commenter_id: int
        :param commenter_full_name: The commenter_full_name of this Feedback.  # noqa: E501
        :type commenter_full_name: str
        :param datetime: The datetime of this Feedback.  # noqa: E501
        :type datetime: str
        :param comment: The comment of this Feedback.  # noqa: E501
        :type comment: str
        """
        self.openapi_types = {
            'id': str,
            'result_id': str,
            'expertise_level_id': int,
            'rating_id': int,
            'commenter_id': int,
            'commenter_full_name': str,
            'datetime': str,
            'comment': str
        }

        self.attribute_map = {
            'id': 'id',
            'result_id': 'result_id',
            'expertise_level_id': 'expertise_level_id',
            'rating_id': 'rating_id',
            'commenter_id': 'commenter_id',
            'commenter_full_name': 'commenter_full_name',
            'datetime': 'datetime',
            'comment': 'comment'
        }

        self._id = id
        self._result_id = result_id
        self._expertise_level_id = expertise_level_id
        self._rating_id = rating_id
        self._commenter_id = commenter_id
        self._commenter_full_name = commenter_full_name
        self._datetime = datetime
        self._comment = comment

    @classmethod
    def from_dict(cls, dikt) -> 'Feedback':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Feedback of this Feedback.  # noqa: E501
        :rtype: Feedback
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Feedback.

        URI for this feedback item  # noqa: E501

        :return: The id of this Feedback.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Feedback.

        URI for this feedback item  # noqa: E501

        :param id: The id of this Feedback.
        :type id: str
        """

        self._id = id

    @property
    def result_id(self) -> str:
        """Gets the result_id of this Feedback.

        URI for the result that this feedback corresponds to  # noqa: E501

        :return: The result_id of this Feedback.
        :rtype: str
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id: str):
        """Sets the result_id of this Feedback.

        URI for the result that this feedback corresponds to  # noqa: E501

        :param result_id: The result_id of this Feedback.
        :type result_id: str
        """

        self._result_id = result_id

    @property
    def expertise_level_id(self) -> int:
        """Gets the expertise_level_id of this Feedback.

        Integer identifier of the claimed expertise level  # noqa: E501

        :return: The expertise_level_id of this Feedback.
        :rtype: int
        """
        return self._expertise_level_id

    @expertise_level_id.setter
    def expertise_level_id(self, expertise_level_id: int):
        """Sets the expertise_level_id of this Feedback.

        Integer identifier of the claimed expertise level  # noqa: E501

        :param expertise_level_id: The expertise_level_id of this Feedback.
        :type expertise_level_id: int
        """

        self._expertise_level_id = expertise_level_id

    @property
    def rating_id(self) -> int:
        """Gets the rating_id of this Feedback.

        Integer identifier of the applied rating  # noqa: E501

        :return: The rating_id of this Feedback.
        :rtype: int
        """
        return self._rating_id

    @rating_id.setter
    def rating_id(self, rating_id: int):
        """Sets the rating_id of this Feedback.

        Integer identifier of the applied rating  # noqa: E501

        :param rating_id: The rating_id of this Feedback.
        :type rating_id: int
        """

        self._rating_id = rating_id

    @property
    def commenter_id(self) -> int:
        """Gets the commenter_id of this Feedback.

        Integer identifier of the commenter  # noqa: E501

        :return: The commenter_id of this Feedback.
        :rtype: int
        """
        return self._commenter_id

    @commenter_id.setter
    def commenter_id(self, commenter_id: int):
        """Sets the commenter_id of this Feedback.

        Integer identifier of the commenter  # noqa: E501

        :param commenter_id: The commenter_id of this Feedback.
        :type commenter_id: int
        """

        self._commenter_id = commenter_id

    @property
    def commenter_full_name(self) -> str:
        """Gets the commenter_full_name of this Feedback.

        Full name of the commenter  # noqa: E501

        :return: The commenter_full_name of this Feedback.
        :rtype: str
        """
        return self._commenter_full_name

    @commenter_full_name.setter
    def commenter_full_name(self, commenter_full_name: str):
        """Sets the commenter_full_name of this Feedback.

        Full name of the commenter  # noqa: E501

        :param commenter_full_name: The commenter_full_name of this Feedback.
        :type commenter_full_name: str
        """

        self._commenter_full_name = commenter_full_name

    @property
    def datetime(self) -> str:
        """Gets the datetime of this Feedback.

        Datetime when the feedback was provided  # noqa: E501

        :return: The datetime of this Feedback.
        :rtype: str
        """
        return self._datetime

    @datetime.setter
    def datetime(self, datetime: str):
        """Sets the datetime of this Feedback.

        Datetime when the feedback was provided  # noqa: E501

        :param datetime: The datetime of this Feedback.
        :type datetime: str
        """

        self._datetime = datetime

    @property
    def comment(self) -> str:
        """Gets the comment of this Feedback.

        A free text comment about this result  # noqa: E501

        :return: The comment of this Feedback.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment: str):
        """Sets the comment of this Feedback.

        A free text comment about this result  # noqa: E501

        :param comment: The comment of this Feedback.
        :type comment: str
        """

        self._comment = comment
