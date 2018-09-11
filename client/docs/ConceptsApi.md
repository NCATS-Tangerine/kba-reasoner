# kba_client.ConceptsApi

All URIs are relative to *https://kba.ncats.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cliques**](ConceptsApi.md#get_cliques) | **GET** /cliques/data/{queryId} | 
[**get_cliques_query_status**](ConceptsApi.md#get_cliques_query_status) | **GET** /cliques/status/{queryId} | 
[**get_concept_details**](ConceptsApi.md#get_concept_details) | **GET** /concepts/details/{cliqueId} | 
[**get_concepts**](ConceptsApi.md#get_concepts) | **GET** /concepts/data/{queryId} | 
[**get_concepts_query_status**](ConceptsApi.md#get_concepts_query_status) | **GET** /concepts/status/{queryId} | 
[**post_cliques_query**](ConceptsApi.md#post_cliques_query) | **POST** /cliques | 
[**post_concepts_query**](ConceptsApi.md#post_concepts_query) | **POST** /concepts | 


# **get_cliques**
> ClientCliquesQueryResult get_cliques(query_id)



Retrieves a list of concept cliques based on  'data ready' from a previously /cliques posted query parameter submission 

### Example
```python
from __future__ import print_function
import time
import kba_client
from kba_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kba_client.ConceptsApi()
query_id = 'query_id_example' # str | the query identifier of a concepts query previously posted by the /cliques endpoint

try:
    api_response = api_instance.get_cliques(query_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->get_cliques: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| the query identifier of a concepts query previously posted by the /cliques endpoint | 

### Return type

[**ClientCliquesQueryResult**](ClientCliquesQueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cliques_query_status**
> ClientCliquesQueryStatus get_cliques_query_status(query_id)



Retrieves the status of a given query about the cliques in the system 

### Example
```python
from __future__ import print_function
import time
import kba_client
from kba_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kba_client.ConceptsApi()
query_id = 'query_id_example' # str | an active query identifier as returned by a POST of clique query parameters.

try:
    api_response = api_instance.get_cliques_query_status(query_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->get_cliques_query_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| an active query identifier as returned by a POST of clique query parameters. | 

### Return type

[**ClientCliquesQueryStatus**](ClientCliquesQueryStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concept_details**
> ClientConceptWithDetails get_concept_details(clique_id, beacons=beacons)



Retrieves details for a specified clique of equivalent concepts in the system,  as specified by a (url-encoded) CURIE identifier of a clique known to the aggregator 

### Example
```python
from __future__ import print_function
import time
import kba_client
from kba_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kba_client.ConceptsApi()
clique_id = 'clique_id_example' # str | a [CURIE-encoded](https://www.w3.org/TR/curie/) identifier, as returned  by any other endpoint of the beacon aggregator API, of an exactly matching  concept clique of interest.
beacons = [56] # list[int] | set of aggregator indices of beacons to be used as knowledge sources for the query  (optional)

try:
    api_response = api_instance.get_concept_details(clique_id, beacons=beacons)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->get_concept_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clique_id** | **str**| a [CURIE-encoded](https://www.w3.org/TR/curie/) identifier, as returned  by any other endpoint of the beacon aggregator API, of an exactly matching  concept clique of interest. | 
 **beacons** | [**list[int]**](int.md)| set of aggregator indices of beacons to be used as knowledge sources for the query  | [optional] 

### Return type

[**ClientConceptWithDetails**](ClientConceptWithDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concepts**
> ClientConceptsQueryResult get_concepts(query_id, beacons=beacons, page_number=page_number, page_size=page_size)



Retrieves a (paged) list of basic equivalent concept clique data from beacons 'data ready' from a previously /concepts posted query parameter submission 

### Example
```python
from __future__ import print_function
import time
import kba_client
from kba_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kba_client.ConceptsApi()
query_id = 'query_id_example' # str | the query identifier of a concepts query previously posted by the /concepts endpoint
beacons = [56] # list[int] | set of aggregator indices of beacons whose data are to be retrieved  (optional)
page_number = 56 # int | (1-based) number of the page to be returned in a paged set of query results. Defaults to '1'.  (optional)
page_size = 56 # int | number of concepts per page to be returned in a paged set of query results. Defaults to '10'.  (optional)

try:
    api_response = api_instance.get_concepts(query_id, beacons=beacons, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->get_concepts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| the query identifier of a concepts query previously posted by the /concepts endpoint | 
 **beacons** | [**list[int]**](int.md)| set of aggregator indices of beacons whose data are to be retrieved  | [optional] 
 **page_number** | **int**| (1-based) number of the page to be returned in a paged set of query results. Defaults to &#39;1&#39;.  | [optional] 
 **page_size** | **int**| number of concepts per page to be returned in a paged set of query results. Defaults to &#39;10&#39;.  | [optional] 

### Return type

[**ClientConceptsQueryResult**](ClientConceptsQueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concepts_query_status**
> ClientConceptsQueryStatus get_concepts_query_status(query_id, beacons=beacons)



Retrieves the status of a given keyword search query about the concepts in the system 

### Example
```python
from __future__ import print_function
import time
import kba_client
from kba_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kba_client.ConceptsApi()
query_id = 'query_id_example' # str | an active query identifier as returned by a POST of concept query parameters.
beacons = [56] # list[int] | subset of aggregator indices of beacons whose status is being polled (if omitted, then the status of all beacons from the query are returned)  (optional)

try:
    api_response = api_instance.get_concepts_query_status(query_id, beacons=beacons)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->get_concepts_query_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| an active query identifier as returned by a POST of concept query parameters. | 
 **beacons** | [**list[int]**](int.md)| subset of aggregator indices of beacons whose status is being polled (if omitted, then the status of all beacons from the query are returned)  | [optional] 

### Return type

[**ClientConceptsQueryStatus**](ClientConceptsQueryStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cliques_query**
> ClientCliquesQuery post_cliques_query(ids)



Retrieves the beacon aggregator assigned cliques of equivalent concepts that includes the specified (url-encoded) CURIE identifiers. Note that the clique to which a given concept CURIE belongs may change over time as the aggregator progressively discovers the members of the clique. Any unmatched identifiers will be ignored (e.g. the id couldn't be found in any of the beacons)  

### Example
```python
from __future__ import print_function
import time
import kba_client
from kba_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kba_client.ConceptsApi()
ids = ['ids_example'] # list[str] | an array of [CURIE-encoded](https://www.w3.org/TR/curie/)  identifiers of interest to be resolved to a list of concept cliques

try:
    api_response = api_instance.post_cliques_query(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->post_cliques_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| an array of [CURIE-encoded](https://www.w3.org/TR/curie/)  identifiers of interest to be resolved to a list of concept cliques | 

### Return type

[**ClientCliquesQuery**](ClientCliquesQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_concepts_query**
> ClientConceptsQuery post_concepts_query(keywords, categories=categories, beacons=beacons)



Posts the query parameters to retrieves a list of  concepts from the system 

### Example
```python
from __future__ import print_function
import time
import kba_client
from kba_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kba_client.ConceptsApi()
keywords = ['keywords_example'] # list[str] | an array of keywords or substrings against which to match concept names and synonyms
categories = ['categories_example'] # list[str] | a subset array of concept categories (specified as codes 'gene',  'pathway', etc.) to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of codes)  (optional)
beacons = [56] # list[int] | subset of aggregator indices of beacons to be used as knowledge sources for the query (if omitted, then the all beacons are queried)  (optional)

try:
    api_response = api_instance.post_concepts_query(keywords, categories=categories, beacons=beacons)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->post_concepts_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keywords** | [**list[str]**](str.md)| an array of keywords or substrings against which to match concept names and synonyms | 
 **categories** | [**list[str]**](str.md)| a subset array of concept categories (specified as codes &#39;gene&#39;,  &#39;pathway&#39;, etc.) to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of codes)  | [optional] 
 **beacons** | [**list[int]**](int.md)| subset of aggregator indices of beacons to be used as knowledge sources for the query (if omitted, then the all beacons are queried)  | [optional] 

### Return type

[**ClientConceptsQuery**](ClientConceptsQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

