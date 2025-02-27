
### patch <a name="patch"></a>
Unauthorize Account From Invoking Function Version

Removes the specified NVIDIA Cloud Account from the set of authorized accounts  that are directly associated with specified function version. If the specified  function version does not have any of its own(not inherited) authorized  accounts, it results in a response with status 404. Also, if the specified  authorized account is not in the set of existing authorized parties that are  directly associated with the specified function version, it results in a  response with status code 400. If the specified function version is public,  then Account Admin cannot perform this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

**API Endpoint**: `PATCH /v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}/remove`

#### Synchronous Client

```python
from nvidia_cloud_functions import Client

client = Client()
res = client.authorizations.functions.versions.remove.patch(
    authorized_party={"nca_id": "string"},
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions import AsyncClient

client = AsyncClient()
res = await client.authorizations.functions.versions.remove.patch(
    authorized_party={"nca_id": "string"},
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```
