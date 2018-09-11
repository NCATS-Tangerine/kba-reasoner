# ClientConceptsQueryBeaconStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beacon** | **int** | Index number of beacon providing these concept details  | [optional] 
**count** | **int** | When a 200 status code is returned, this integer designates  the number of concepts matched by the query for the given beacon.  | [optional] 
**status** | **int** | Http code status of beacon API - 200 means &#39;data ready&#39;, 102 means &#39;query in progress&#39;, other codes (e.g. 500) are server errors. Once a beacon has a &#39;200&#39; success code, then the /concepts/data  endpoint may be used to retrieve it.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


