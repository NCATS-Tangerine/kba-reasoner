# kba_client.MetadataApi

All URIs are relative to *https://kba.ncats.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_beacons**](MetadataApi.md#get_beacons) | **GET** /beacons | 
[**get_concept_categories**](MetadataApi.md#get_concept_categories) | **GET** /categories | 
[**get_errors**](MetadataApi.md#get_errors) | **GET** /errorlog | 
[**get_knowledge_map**](MetadataApi.md#get_knowledge_map) | **GET** /kmap | 
[**get_predicates**](MetadataApi.md#get_predicates) | **GET** /predicates | 


# **get_beacons**
> list[ClientKnowledgeBeacon] get_beacons()



Get a list of all of the knowledge beacons that the aggregator can query 

### Example
```python
from __future__ import print_function
import time
import kba_client
from kba_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kba_client.MetadataApi()

try:
    api_response = api_instance.get_beacons()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_beacons: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ClientKnowledgeBeacon]**](ClientKnowledgeBeacon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concept_categories**
> list[ClientConceptCategory] get_concept_categories(beacons=beacons)



Get a list of semantic categories and number of instances in each  available knowledge beacon, including associated beacon-specific metadata 

### Example
```python
from __future__ import print_function
import time
import kba_client
from kba_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kba_client.MetadataApi()
beacons = [56] # list[int] | set of aggregator indices of beacons to constrain categories returned  (optional)

try:
    api_response = api_instance.get_concept_categories(beacons=beacons)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_concept_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beacons** | [**list[int]**](int.md)| set of aggregator indices of beacons to constrain categories returned  | [optional] 

### Return type

[**list[ClientConceptCategory]**](ClientConceptCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_errors**
> list[ClientLogEntry] get_errors(query_id)



Get a log of the system errors associated with a specified query 

### Example
```python
from __future__ import print_function
import time
import kba_client
from kba_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kba_client.MetadataApi()
query_id = 'query_id_example' # str | query identifier returned from a POSTed query 

try:
    api_response = api_instance.get_errors(query_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| query identifier returned from a POSTed query  | 

### Return type

[**list[ClientLogEntry]**](ClientLogEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knowledge_map**
> list[ClientKnowledgeMap] get_knowledge_map(beacons=beacons)



Get a high level knowledge map of the all the beacons specified by triplets of subject concept category, relationship predicate and concept object category 

### Example
```python
from __future__ import print_function
import time
import kba_client
from kba_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kba_client.MetadataApi()
beacons = [56] # list[int] | set of aggregator indices of beacons constraining knowledge maps returned   (optional)

try:
    api_response = api_instance.get_knowledge_map(beacons=beacons)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_knowledge_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beacons** | [**list[int]**](int.md)| set of aggregator indices of beacons constraining knowledge maps returned   | [optional] 

### Return type

[**list[ClientKnowledgeMap]**](ClientKnowledgeMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_predicates**
> list[ClientPredicate] get_predicates(beacons=beacons)



Get a list of predicates used in statements issued by the knowledge source 

### Example
```python
from __future__ import print_function
import time
import kba_client
from kba_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kba_client.MetadataApi()
beacons = [56] # list[int] | set of aggregator indices of beacons to constrain predicates returned  (optional)

try:
    api_response = api_instance.get_predicates(beacons=beacons)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_predicates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beacons** | [**list[int]**](int.md)| set of aggregator indices of beacons to constrain predicates returned  | [optional] 

### Return type

[**list[ClientPredicate]**](ClientPredicate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

