
### patch <a name="patch"></a>
Authorize Additional Account To Invoke Function

Adds the specified NVIDIA Cloud Account to the set of authorized accounts that  are can invoke all the versions of the specified function. If the specified  function does not have any existing inheritable authorized accounts, it results  in a response with status 404. If the specified account is already in the set  of existing inheritable authorized accounts, it results in a response with  status code 409. If a function is public, then Account Admin cannot perform  this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

**API Endpoint**: `PATCH /v2/nvcf/authorizations/functions/{functionId}/add`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.authorizations.functions.add.patch(
    authorized_party={"nca_id": "string"},
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.authorizations.functions.add.patch(
    authorized_party={"nca_id": "string"},
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```
