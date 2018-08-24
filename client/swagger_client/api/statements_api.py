# coding: utf-8

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.   # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: richard@starinformatics.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class StatementsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_statement_details(self, statement_id, **kwargs):  # noqa: E501
        """get_statement_details  # noqa: E501

        Retrieves a details relating to a specified concept-relationship statement include 'is_defined_by and 'provided_by' provenance; extended edge properties exported as tag = value; and any associated annotations (publications, etc.)  cited as evidence for the given statement.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_statement_details(statement_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str statement_id: (url-encoded) CURIE identifier of the concept-relationship statement (\"assertion\", \"claim\") for which associated evidence is sought, e.g. kbs:Q420626_P2175_Q126691  (required)
        :param list[str] keywords: an array of keywords or substrings against which to filter a reference label (e.g. title) statement evidence citation array.
        :param int page_number: (1-based) number of the page to be returned in a paged set of statement.evidence array entries. Defaults to 1. 
        :param int page_size: number of cited references per page to be returned in a paged set of statement.evidence array entries. Defaults to '10'. 
        :return: ClientStatementDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_statement_details_with_http_info(statement_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_statement_details_with_http_info(statement_id, **kwargs)  # noqa: E501
            return data

    def get_statement_details_with_http_info(self, statement_id, **kwargs):  # noqa: E501
        """get_statement_details  # noqa: E501

        Retrieves a details relating to a specified concept-relationship statement include 'is_defined_by and 'provided_by' provenance; extended edge properties exported as tag = value; and any associated annotations (publications, etc.)  cited as evidence for the given statement.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_statement_details_with_http_info(statement_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str statement_id: (url-encoded) CURIE identifier of the concept-relationship statement (\"assertion\", \"claim\") for which associated evidence is sought, e.g. kbs:Q420626_P2175_Q126691  (required)
        :param list[str] keywords: an array of keywords or substrings against which to filter a reference label (e.g. title) statement evidence citation array.
        :param int page_number: (1-based) number of the page to be returned in a paged set of statement.evidence array entries. Defaults to 1. 
        :param int page_size: number of cited references per page to be returned in a paged set of statement.evidence array entries. Defaults to '10'. 
        :return: ClientStatementDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['statement_id', 'keywords', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_statement_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'statement_id' is set
        if ('statement_id' not in params or
                params['statement_id'] is None):
            raise ValueError("Missing the required parameter `statement_id` when calling `get_statement_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'statement_id' in params:
            path_params['statementId'] = params['statement_id']  # noqa: E501

        query_params = []
        if 'keywords' in params:
            query_params.append(('keywords', params['keywords']))  # noqa: E501
            collection_formats['keywords'] = 'csv'  # noqa: E501
        if 'page_number' in params:
            query_params.append(('pageNumber', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/statements/details/{statementId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClientStatementDetails',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_statements_query(self, query_id, **kwargs):  # noqa: E501
        """get_statements_query  # noqa: E501

        Given a specification [CURIE-encoded](https://www.w3.org/TR/curie/) a 'source' clique identifier for a set of exactly matching concepts,  retrieves a paged list of concept-relations where either the subject or object concept matches the 'source' clique identifier.  Optionally, a 'target' clique identifier may also be given, in which case the 'target' clique identifier should match the concept clique opposing the 'source', that is, if the 'source' matches a subject, then the  'target' should match the object of a given statement (or vice versa).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_statements_query(query_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str query_id: an active query identifier as returned by a POST of statement query parameters. (required)
        :param list[int] beacons: subset of aggregator indices of beacons whose statements are to be retrieved 
        :param int page_number: (1-based) number of the page to be returned in a paged set of query results. Defaults to '1'. 
        :param int page_size: number of concepts per page to be returned in a paged set of query results. Defaults to '10'. 
        :return: ClientStatementsQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_statements_query_with_http_info(query_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_statements_query_with_http_info(query_id, **kwargs)  # noqa: E501
            return data

    def get_statements_query_with_http_info(self, query_id, **kwargs):  # noqa: E501
        """get_statements_query  # noqa: E501

        Given a specification [CURIE-encoded](https://www.w3.org/TR/curie/) a 'source' clique identifier for a set of exactly matching concepts,  retrieves a paged list of concept-relations where either the subject or object concept matches the 'source' clique identifier.  Optionally, a 'target' clique identifier may also be given, in which case the 'target' clique identifier should match the concept clique opposing the 'source', that is, if the 'source' matches a subject, then the  'target' should match the object of a given statement (or vice versa).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_statements_query_with_http_info(query_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str query_id: an active query identifier as returned by a POST of statement query parameters. (required)
        :param list[int] beacons: subset of aggregator indices of beacons whose statements are to be retrieved 
        :param int page_number: (1-based) number of the page to be returned in a paged set of query results. Defaults to '1'. 
        :param int page_size: number of concepts per page to be returned in a paged set of query results. Defaults to '10'. 
        :return: ClientStatementsQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_id', 'beacons', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_statements_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_id' is set
        if ('query_id' not in params or
                params['query_id'] is None):
            raise ValueError("Missing the required parameter `query_id` when calling `get_statements_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'query_id' in params:
            path_params['queryId'] = params['query_id']  # noqa: E501

        query_params = []
        if 'beacons' in params:
            query_params.append(('beacons', params['beacons']))  # noqa: E501
            collection_formats['beacons'] = 'csv'  # noqa: E501
        if 'page_number' in params:
            query_params.append(('pageNumber', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/statements/data/{queryId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClientStatementsQueryResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_statements_query_status(self, query_id, **kwargs):  # noqa: E501
        """get_statements_query_status  # noqa: E501

        Retrieves the status of a given query about the statements in the system   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_statements_query_status(query_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str query_id: an active query identifier as returned by a POST of statements  query parameters. (required)
        :param list[int] beacons: subset of aggregator indices of beacons whose status is being polled (if omitted, then the status of all beacons from the query are returned) 
        :return: ClientStatementsQueryStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_statements_query_status_with_http_info(query_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_statements_query_status_with_http_info(query_id, **kwargs)  # noqa: E501
            return data

    def get_statements_query_status_with_http_info(self, query_id, **kwargs):  # noqa: E501
        """get_statements_query_status  # noqa: E501

        Retrieves the status of a given query about the statements in the system   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_statements_query_status_with_http_info(query_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str query_id: an active query identifier as returned by a POST of statements  query parameters. (required)
        :param list[int] beacons: subset of aggregator indices of beacons whose status is being polled (if omitted, then the status of all beacons from the query are returned) 
        :return: ClientStatementsQueryStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_id', 'beacons']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_statements_query_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_id' is set
        if ('query_id' not in params or
                params['query_id'] is None):
            raise ValueError("Missing the required parameter `query_id` when calling `get_statements_query_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'query_id' in params:
            path_params['queryId'] = params['query_id']  # noqa: E501

        query_params = []
        if 'beacons' in params:
            query_params.append(('beacons', params['beacons']))  # noqa: E501
            collection_formats['beacons'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/statements/status/{queryId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClientStatementsQueryStatus',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_statements_query(self, source, **kwargs):  # noqa: E501
        """post_statements_query  # noqa: E501

        Posts a query to retrieve concept-relations where either the subject or object concept matches a [CURIE-encoded 'source'](https://www.w3.org/TR/curie/) clique identifier designating a set of exactly matching concepts. A 'target' clique identifier may optionally be given, in which case the 'target' clique identifier should match the concept clique opposing the 'source', that is, if the 'source' matches a subject, then the  'target' should match the object of a given statement (or vice versa).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_statements_query(source, async=True)
        >>> result = thread.get()

        :param async bool
        :param str source: a [CURIE-encoded](https://www.w3.org/TR/curie/) identifier of the  exactly matching 'source' clique, cliques as identified by other endpoints of the beacon aggregator API.   (required)
        :param list[str] relations: a subset (array) of identifiers of predicate relation identifiers with which to constrain the statement relations retrieved  for the given query seed concept. The predicate ids sent should  be as published by the beacon-aggregator by the /predicates API endpoint. 
        :param str target: a [CURIE-encoded](https://www.w3.org/TR/curie/) identifier of the  exactly matching 'target' clique, cliques as identified by other endpoints of the beacon aggregator API.  
        :param list[str] keywords: an array of keywords or substrings against which to match the  'target' concept or 'predicate' names of the set of  concept-relations matched by the 'source' concepts.
        :param list[str] categories: a subset (array) of identifiers of concept categories to which to constrain 'target' concepts associated with the given 'source' concept ((see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of categories). 
        :param list[int] beacons: set of aggregator indices of beacons to be used as knowledge sources for the query 
        :return: ClientStatementsQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_statements_query_with_http_info(source, **kwargs)  # noqa: E501
        else:
            (data) = self.post_statements_query_with_http_info(source, **kwargs)  # noqa: E501
            return data

    def post_statements_query_with_http_info(self, source, **kwargs):  # noqa: E501
        """post_statements_query  # noqa: E501

        Posts a query to retrieve concept-relations where either the subject or object concept matches a [CURIE-encoded 'source'](https://www.w3.org/TR/curie/) clique identifier designating a set of exactly matching concepts. A 'target' clique identifier may optionally be given, in which case the 'target' clique identifier should match the concept clique opposing the 'source', that is, if the 'source' matches a subject, then the  'target' should match the object of a given statement (or vice versa).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_statements_query_with_http_info(source, async=True)
        >>> result = thread.get()

        :param async bool
        :param str source: a [CURIE-encoded](https://www.w3.org/TR/curie/) identifier of the  exactly matching 'source' clique, cliques as identified by other endpoints of the beacon aggregator API.   (required)
        :param list[str] relations: a subset (array) of identifiers of predicate relation identifiers with which to constrain the statement relations retrieved  for the given query seed concept. The predicate ids sent should  be as published by the beacon-aggregator by the /predicates API endpoint. 
        :param str target: a [CURIE-encoded](https://www.w3.org/TR/curie/) identifier of the  exactly matching 'target' clique, cliques as identified by other endpoints of the beacon aggregator API.  
        :param list[str] keywords: an array of keywords or substrings against which to match the  'target' concept or 'predicate' names of the set of  concept-relations matched by the 'source' concepts.
        :param list[str] categories: a subset (array) of identifiers of concept categories to which to constrain 'target' concepts associated with the given 'source' concept ((see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of categories). 
        :param list[int] beacons: set of aggregator indices of beacons to be used as knowledge sources for the query 
        :return: ClientStatementsQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source', 'relations', 'target', 'keywords', 'categories', 'beacons']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_statements_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source' is set
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `post_statements_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'source' in params:
            query_params.append(('source', params['source']))  # noqa: E501
        if 'relations' in params:
            query_params.append(('relations', params['relations']))  # noqa: E501
            collection_formats['relations'] = 'csv'  # noqa: E501
        if 'target' in params:
            query_params.append(('target', params['target']))  # noqa: E501
        if 'keywords' in params:
            query_params.append(('keywords', params['keywords']))  # noqa: E501
            collection_formats['keywords'] = 'csv'  # noqa: E501
        if 'categories' in params:
            query_params.append(('categories', params['categories']))  # noqa: E501
            collection_formats['categories'] = 'csv'  # noqa: E501
        if 'beacons' in params:
            query_params.append(('beacons', params['beacons']))  # noqa: E501
            collection_formats['beacons'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/statements', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClientStatementsQuery',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
