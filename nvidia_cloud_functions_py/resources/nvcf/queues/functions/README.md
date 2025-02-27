
### get <a name="get"></a>
Queue Details

Provides details of all the queues associated with the specified function.  If a function has multiple versions and they are all deployed, then the  response includes details of all the queues. If the specified function  is public, then Account Admin cannot perform this operation. Requires a bearer token or an api-key with 'queue_details' scope in the HTTP  Authorization header. 

**API Endpoint**: `GET /v2/nvcf/queues/functions/{functionId}`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.queues.functions.get(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.queues.functions.get(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```
