
### list <a name="list"></a>
List Function Ids

Lists ids of all the functions in the authenticated NVIDIA Cloud Account.  Requires either a bearer token or an api-key with 'list_functions' or  'list_functions_details' scopes in the HTTP Authorization header. 

**API Endpoint**: `GET /v2/nvcf/functions/ids`

#### Synchronous Client

```python
from nvidia_cloud_functions import Client

client = Client()
res = client.functions.ids.list_fn()
```

#### Asynchronous Client

```python
from nvidia_cloud_functions import AsyncClient

client = AsyncClient()
res = await client.functions.ids.list_fn()
```
