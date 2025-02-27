
### create <a name="create"></a>
Call Function

Invokes the specified function that was successfully deployed. If the version  is not specified, any active function versions will handle the request. If  the version is specified in the URI, then the request is exclusively processed  by the designated version of the function. By default, this endpoint will block  for 5 seconds. If the request is not fulfilled before the timeout, it's status  is considered in-progress or pending and the response includes HTTP status code  202 with an invocation request ID, indicating that the client should commence  polling for the result using the invocation request ID. Access to this endpoint  mandates inclusion of either a bearer token or an api-key with 'invoke_function'  scope in the HTTP Authorization header. Additionally, this endpoint has the  capability to provide updates on the progress of the request, contingent  upon the workload's provision of such information. In-progress responses are returned in order. If no in-progress response is received  during polling you will receive the most recent in-progress response. Only the first  256 unread in-progress messages are kept. 

**API Endpoint**: `POST /v2/nvcf/exec/functions/{functionId}/versions/{versionId}`

#### Synchronous Client

```python
from nvidia_cloud_functions import Client

client = Client()
res = client.exec.functions.versions.create(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    request_body={},
    version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions import AsyncClient

client = AsyncClient()
res = await client.exec.functions.versions.create(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    request_body={},
    version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```
