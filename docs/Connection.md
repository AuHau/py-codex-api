# Connection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peer_id** | **str** | Peer Identity reference as specified at https://docs.libp2p.io/concepts/fundamentals/peers/ | 
**direct** | **bool** | Whether at least one connection to this peer is direct (not relayed) | 

## Example

```python
from codex_api_client.models.connection import Connection

# TODO update the JSON string below
json = "{}"
# create an instance of Connection from a JSON string
connection_instance = Connection.from_json(json)
# print the JSON string representation of the object
print(Connection.to_json())

# convert the object into a dict
connection_dict = connection_instance.to_dict()
# create an instance of Connection from a dict
connection_from_dict = Connection.from_dict(connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


