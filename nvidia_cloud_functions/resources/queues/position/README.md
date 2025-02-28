
### list <a name="list"></a>
Queue Position

Using the specified function invocation request id, returns the estimated  position of the corresponding message up to 1000 in the queue. Requires a bearer token or an api-key with 'queue_details' scope in the HTTP  Authorization header. 

**API Endpoint**: `GET /v2/nvcf/queues/{requestId}/position`

#### Synchronous Client

```python
from nvidia_cloud_functions import Client

client = Client()
res = client.queues.position.list(request_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
```

#### Asynchronous Client

```python
from nvidia_cloud_functions import AsyncClient

client = AsyncClient()
res = await client.queues.position.list(
    request_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```
