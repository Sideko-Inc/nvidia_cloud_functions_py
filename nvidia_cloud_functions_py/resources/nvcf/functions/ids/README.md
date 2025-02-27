
### list <a name="list"></a>
List Function Ids

Lists ids of all the functions in the authenticated NVIDIA Cloud Account.  Requires either a bearer token or an api-key with 'list_functions' or  'list_functions_details' scopes in the HTTP Authorization header. 

**API Endpoint**: `GET /v2/nvcf/functions/ids`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.functions.ids.list()
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.functions.ids.list()
```
