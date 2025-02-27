
### get <a name="get"></a>
Poll For Result Using Function Invocation Request

Retrieves the status of an in-progress or pending request using its unique  invocation request ID. If the result is available, it will be included in  the response, marking the request as fulfilled. Conversely, if the result is  not yet available, the request is deemed pending. Access to this endpoint  mandates inclusion of either a bearer token or an api-key with  'invoke_function' scope in the HTTP Authorization header. In-progress responses are returned in order. If no in-progress response is received  during polling you will receive the most recent in-progress response. Only the first  256 unread in-progress messages are kept. 

**API Endpoint**: `GET /v2/nvcf/pexec/status/{requestId}`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.pexec.status.get(request_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.pexec.status.get(
    request_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```
