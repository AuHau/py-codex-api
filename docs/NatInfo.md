# NatInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reachability** | **str** | AutoNAT reachability status | 
**client_mode** | **bool** | Whether the DHT is running in client mode (not added to remote routing tables) | 
**relay_running** | **bool** | Whether the AutoRelay service is currently running | 
**port_mapping** | **str** | Active NAT port mapping type | 

## Example

```python
from codex_api_client.models.nat_info import NatInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NatInfo from a JSON string
nat_info_instance = NatInfo.from_json(json)
# print the JSON string representation of the object
print(NatInfo.to_json())

# convert the object into a dict
nat_info_dict = nat_info_instance.to_dict()
# create an instance of NatInfo from a dict
nat_info_from_dict = NatInfo.from_dict(nat_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


