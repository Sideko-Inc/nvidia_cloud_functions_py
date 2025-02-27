
### patch <a name="patch"></a>
Unauthorize Account From Invoking Function

Removes the specified NVIDIA Cloud Account from the set of authorized accounts  that can invoke all the versions of the specified function. If the specified  function does not have any existing inheritable authorized parties, it results  in a response with status 404. Also, if the specified account is not in the  existing set of inheritable authorized accounts, it results in a response with  status 400. If the specified function is public, then Account Admin cannot  perform this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

**API Endpoint**: `PATCH /v2/nvcf/authorizations/functions/{functionId}/remove`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.authorizations.functions.remove.patch(
    authorized_party={"nca_id": "string"},
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.authorizations.functions.remove.patch(
    authorized_party={"nca_id": "string"},
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```
