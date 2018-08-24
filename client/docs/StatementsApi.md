# swagger_client.StatementsApi

All URIs are relative to *https://kba.ncats.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statement_details**](StatementsApi.md#get_statement_details) | **GET** /statements/details/{statementId} | 
[**get_statements_query**](StatementsApi.md#get_statements_query) | **GET** /statements/data/{queryId} | 
[**get_statements_query_status**](StatementsApi.md#get_statements_query_status) | **GET** /statements/status/{queryId} | 
[**post_statements_query**](StatementsApi.md#post_statements_query) | **POST** /statements | 


# **get_statement_details**
> ClientStatementDetails get_statement_details(statement_id, keywords=keywords, page_number=page_number, page_size=page_size)



Retrieves a details relating to a specified concept-relationship statement include 'is_defined_by and 'provided_by' provenance; extended edge properties exported as tag = value; and any associated annotations (publications, etc.)  cited as evidence for the given statement. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatementsApi()
statement_id = 'statement_id_example' # str | (url-encoded) CURIE identifier of the concept-relationship statement (\"assertion\", \"claim\") for which associated evidence is sought, e.g. kbs:Q420626_P2175_Q126691 
keywords = ['keywords_example'] # list[str] | an array of keywords or substrings against which to filter a reference label (e.g. title) statement evidence citation array. (optional)
page_number = 56 # int | (1-based) number of the page to be returned in a paged set of statement.evidence array entries. Defaults to 1.  (optional)
page_size = 56 # int | number of cited references per page to be returned in a paged set of statement.evidence array entries. Defaults to '10'.  (optional)

try:
    api_response = api_instance.get_statement_details(statement_id, keywords=keywords, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementsApi->get_statement_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statement_id** | **str**| (url-encoded) CURIE identifier of the concept-relationship statement (\&quot;assertion\&quot;, \&quot;claim\&quot;) for which associated evidence is sought, e.g. kbs:Q420626_P2175_Q126691  | 
 **keywords** | [**list[str]**](str.md)| an array of keywords or substrings against which to filter a reference label (e.g. title) statement evidence citation array. | [optional] 
 **page_number** | **int**| (1-based) number of the page to be returned in a paged set of statement.evidence array entries. Defaults to 1.  | [optional] 
 **page_size** | **int**| number of cited references per page to be returned in a paged set of statement.evidence array entries. Defaults to &#39;10&#39;.  | [optional] 

### Return type

[**ClientStatementDetails**](ClientStatementDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statements_query**
> ClientStatementsQueryResult get_statements_query(query_id, beacons=beacons, page_number=page_number, page_size=page_size)



Given a specification [CURIE-encoded](https://www.w3.org/TR/curie/) a 'source' clique identifier for a set of exactly matching concepts,  retrieves a paged list of concept-relations where either the subject or object concept matches the 'source' clique identifier.  Optionally, a 'target' clique identifier may also be given, in which case the 'target' clique identifier should match the concept clique opposing the 'source', that is, if the 'source' matches a subject, then the  'target' should match the object of a given statement (or vice versa). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatementsApi()
query_id = 'query_id_example' # str | an active query identifier as returned by a POST of statement query parameters.
beacons = [56] # list[int] | subset of aggregator indices of beacons whose statements are to be retrieved  (optional)
page_number = 56 # int | (1-based) number of the page to be returned in a paged set of query results. Defaults to '1'.  (optional)
page_size = 56 # int | number of concepts per page to be returned in a paged set of query results. Defaults to '10'.  (optional)

try:
    api_response = api_instance.get_statements_query(query_id, beacons=beacons, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementsApi->get_statements_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| an active query identifier as returned by a POST of statement query parameters. | 
 **beacons** | [**list[int]**](int.md)| subset of aggregator indices of beacons whose statements are to be retrieved  | [optional] 
 **page_number** | **int**| (1-based) number of the page to be returned in a paged set of query results. Defaults to &#39;1&#39;.  | [optional] 
 **page_size** | **int**| number of concepts per page to be returned in a paged set of query results. Defaults to &#39;10&#39;.  | [optional] 

### Return type

[**ClientStatementsQueryResult**](ClientStatementsQueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statements_query_status**
> ClientStatementsQueryStatus get_statements_query_status(query_id, beacons=beacons)



Retrieves the status of a given query about the statements in the system 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatementsApi()
query_id = 'query_id_example' # str | an active query identifier as returned by a POST of statements  query parameters.
beacons = [56] # list[int] | subset of aggregator indices of beacons whose status is being polled (if omitted, then the status of all beacons from the query are returned)  (optional)

try:
    api_response = api_instance.get_statements_query_status(query_id, beacons=beacons)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementsApi->get_statements_query_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| an active query identifier as returned by a POST of statements  query parameters. | 
 **beacons** | [**list[int]**](int.md)| subset of aggregator indices of beacons whose status is being polled (if omitted, then the status of all beacons from the query are returned)  | [optional] 

### Return type

[**ClientStatementsQueryStatus**](ClientStatementsQueryStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_statements_query**
> ClientStatementsQuery post_statements_query(source, relations=relations, target=target, keywords=keywords, categories=categories, beacons=beacons)



Posts a query to retrieve concept-relations where either the subject or object concept matches a [CURIE-encoded 'source'](https://www.w3.org/TR/curie/) clique identifier designating a set of exactly matching concepts. A 'target' clique identifier may optionally be given, in which case the 'target' clique identifier should match the concept clique opposing the 'source', that is, if the 'source' matches a subject, then the  'target' should match the object of a given statement (or vice versa). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatementsApi()
source = 'source_example' # str | a [CURIE-encoded](https://www.w3.org/TR/curie/) identifier of the  exactly matching 'source' clique, cliques as identified by other endpoints of the beacon aggregator API.  
relations = ['relations_example'] # list[str] | a subset (array) of identifiers of predicate relation identifiers with which to constrain the statement relations retrieved  for the given query seed concept. The predicate ids sent should  be as published by the beacon-aggregator by the /predicates API endpoint.  (optional)
target = 'target_example' # str | a [CURIE-encoded](https://www.w3.org/TR/curie/) identifier of the  exactly matching 'target' clique, cliques as identified by other endpoints of the beacon aggregator API.   (optional)
keywords = ['keywords_example'] # list[str] | an array of keywords or substrings against which to match the  'target' concept or 'predicate' names of the set of  concept-relations matched by the 'source' concepts. (optional)
categories = ['categories_example'] # list[str] | a subset (array) of identifiers of concept categories to which to constrain 'target' concepts associated with the given 'source' concept ((see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of categories).  (optional)
beacons = [56] # list[int] | set of aggregator indices of beacons to be used as knowledge sources for the query  (optional)

try:
    api_response = api_instance.post_statements_query(source, relations=relations, target=target, keywords=keywords, categories=categories, beacons=beacons)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementsApi->post_statements_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| a [CURIE-encoded](https://www.w3.org/TR/curie/) identifier of the  exactly matching &#39;source&#39; clique, cliques as identified by other endpoints of the beacon aggregator API.   | 
 **relations** | [**list[str]**](str.md)| a subset (array) of identifiers of predicate relation identifiers with which to constrain the statement relations retrieved  for the given query seed concept. The predicate ids sent should  be as published by the beacon-aggregator by the /predicates API endpoint.  | [optional] 
 **target** | **str**| a [CURIE-encoded](https://www.w3.org/TR/curie/) identifier of the  exactly matching &#39;target&#39; clique, cliques as identified by other endpoints of the beacon aggregator API.   | [optional] 
 **keywords** | [**list[str]**](str.md)| an array of keywords or substrings against which to match the  &#39;target&#39; concept or &#39;predicate&#39; names of the set of  concept-relations matched by the &#39;source&#39; concepts. | [optional] 
 **categories** | [**list[str]**](str.md)| a subset (array) of identifiers of concept categories to which to constrain &#39;target&#39; concepts associated with the given &#39;source&#39; concept ((see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of categories).  | [optional] 
 **beacons** | [**list[int]**](int.md)| set of aggregator indices of beacons to be used as knowledge sources for the query  | [optional] 

### Return type

[**ClientStatementsQuery**](ClientStatementsQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

