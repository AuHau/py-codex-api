# StorageVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**revision** | **str** |  | [optional] 

## Example

```python
from codex_api_client.models.storage_version import StorageVersion

# TODO update the JSON string below
json = "{}"
# create an instance of StorageVersion from a JSON string
storage_version_instance = StorageVersion.from_json(json)
# print the JSON string representation of the object
print(StorageVersion.to_json())

# convert the object into a dict
storage_version_dict = storage_version_instance.to_dict()
# create an instance of StorageVersion from a dict
storage_version_from_dict = StorageVersion.from_dict(storage_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


