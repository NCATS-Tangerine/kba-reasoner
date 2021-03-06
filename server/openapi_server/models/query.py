# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Query(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bypass_cache=None, asynchronous=None, max_results=None, page_size=None, page_number=None, reasoner_ids=None, query_message=None, previous_message_processing_plan=None):  # noqa: E501
        """Query - a model defined in OpenAPI

        :param bypass_cache: The bypass_cache of this Query.  # noqa: E501
        :type bypass_cache: str
        :param asynchronous: The asynchronous of this Query.  # noqa: E501
        :type asynchronous: str
        :param max_results: The max_results of this Query.  # noqa: E501
        :type max_results: int
        :param page_size: The page_size of this Query.  # noqa: E501
        :type page_size: int
        :param page_number: The page_number of this Query.  # noqa: E501
        :type page_number: int
        :param reasoner_ids: The reasoner_ids of this Query.  # noqa: E501
        :type reasoner_ids: List[str]
        :param query_message: The query_message of this Query.  # noqa: E501
        :type query_message: List[Message]
        :param previous_message_processing_plan: The previous_message_processing_plan of this Query.  # noqa: E501
        :type previous_message_processing_plan: List[PreviousMessageProcessingPlan]
        """
        self.openapi_types = {
            'bypass_cache': str,
            'asynchronous': str,
            'max_results': int,
            'page_size': int,
            'page_number': int,
            'reasoner_ids': List[str],
            'query_message': List[Message],
            'previous_message_processing_plan': List[PreviousMessageProcessingPlan]
        }

        self.attribute_map = {
            'bypass_cache': 'bypass_cache',
            'asynchronous': 'asynchronous',
            'max_results': 'max_results',
            'page_size': 'page_size',
            'page_number': 'page_number',
            'reasoner_ids': 'reasoner_ids',
            'query_message': 'query_message',
            'previous_message_processing_plan': 'previous_message_processing_plan'
        }

        self._bypass_cache = bypass_cache
        self._asynchronous = asynchronous
        self._max_results = max_results
        self._page_size = page_size
        self._page_number = page_number
        self._reasoner_ids = reasoner_ids
        self._query_message = query_message
        self._previous_message_processing_plan = previous_message_processing_plan

    @classmethod
    def from_dict(cls, dikt) -> 'Query':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Query of this Query.  # noqa: E501
        :rtype: Query
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bypass_cache(self):
        """Gets the bypass_cache of this Query.

        Set to true in order to bypass any possible cached message and try to answer the query over again  # noqa: E501

        :return: The bypass_cache of this Query.
        :rtype: str
        """
        return self._bypass_cache

    @bypass_cache.setter
    def bypass_cache(self, bypass_cache):
        """Sets the bypass_cache of this Query.

        Set to true in order to bypass any possible cached message and try to answer the query over again  # noqa: E501

        :param bypass_cache: The bypass_cache of this Query.
        :type bypass_cache: str
        """

        self._bypass_cache = bypass_cache

    @property
    def asynchronous(self):
        """Gets the asynchronous of this Query.

        Set to true in order to receive an incomplete message_id if the query will take a while. Client can then periodically request that message_id for a status update and eventual complete message  # noqa: E501

        :return: The asynchronous of this Query.
        :rtype: str
        """
        return self._asynchronous

    @asynchronous.setter
    def asynchronous(self, asynchronous):
        """Sets the asynchronous of this Query.

        Set to true in order to receive an incomplete message_id if the query will take a while. Client can then periodically request that message_id for a status update and eventual complete message  # noqa: E501

        :param asynchronous: The asynchronous of this Query.
        :type asynchronous: str
        """

        self._asynchronous = asynchronous

    @property
    def max_results(self):
        """Gets the max_results of this Query.

        Maximum number of individual results to return  # noqa: E501

        :return: The max_results of this Query.
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this Query.

        Maximum number of individual results to return  # noqa: E501

        :param max_results: The max_results of this Query.
        :type max_results: int
        """

        self._max_results = max_results

    @property
    def page_size(self):
        """Gets the page_size of this Query.

        Split the results into pages with this number of results each  # noqa: E501

        :return: The page_size of this Query.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this Query.

        Split the results into pages with this number of results each  # noqa: E501

        :param page_size: The page_size of this Query.
        :type page_size: int
        """

        self._page_size = page_size

    @property
    def page_number(self):
        """Gets the page_number of this Query.

        Page number of results when the number of results exceeds the page_size  # noqa: E501

        :return: The page_number of this Query.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this Query.

        Page number of results when the number of results exceeds the page_size  # noqa: E501

        :param page_number: The page_number of this Query.
        :type page_number: int
        """

        self._page_number = page_number

    @property
    def reasoner_ids(self):
        """Gets the reasoner_ids of this Query.

        List of reasoners to consult for the query  # noqa: E501

        :return: The reasoner_ids of this Query.
        :rtype: List[str]
        """
        return self._reasoner_ids

    @reasoner_ids.setter
    def reasoner_ids(self, reasoner_ids):
        """Sets the reasoner_ids of this Query.

        List of reasoners to consult for the query  # noqa: E501

        :param reasoner_ids: The reasoner_ids of this Query.
        :type reasoner_ids: List[str]
        """

        self._reasoner_ids = reasoner_ids

    @property
    def query_message(self):
        """Gets the query_message of this Query.

        Message object that represents the query to be answered  # noqa: E501

        :return: The query_message of this Query.
        :rtype: List[Message]
        """
        return self._query_message

    @query_message.setter
    def query_message(self, query_message):
        """Sets the query_message of this Query.

        Message object that represents the query to be answered  # noqa: E501

        :param query_message: The query_message of this Query.
        :type query_message: List[Message]
        """

        self._query_message = query_message

    @property
    def previous_message_processing_plan(self):
        """Gets the previous_message_processing_plan of this Query.

        Container for one or more Message objects or identifiers for one or more Messages along with a processing plan for how those messages should be processed and returned  # noqa: E501

        :return: The previous_message_processing_plan of this Query.
        :rtype: List[PreviousMessageProcessingPlan]
        """
        return self._previous_message_processing_plan

    @previous_message_processing_plan.setter
    def previous_message_processing_plan(self, previous_message_processing_plan):
        """Sets the previous_message_processing_plan of this Query.

        Container for one or more Message objects or identifiers for one or more Messages along with a processing plan for how those messages should be processed and returned  # noqa: E501

        :param previous_message_processing_plan: The previous_message_processing_plan of this Query.
        :type previous_message_processing_plan: List[PreviousMessageProcessingPlan]
        """

        self._previous_message_processing_plan = previous_message_processing_plan
