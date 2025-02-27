
### delete <a name="delete"></a>
Delete All Extra Authorizations For Function Version

Deletes all the authorized accounts that are directly associated with the  specified function version. Authorized parties that are inherited by the  function version are not deleted. If the specified function version is public,  then Account Admin cannot perform this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

**API Endpoint**: `DELETE /v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.authorizations.functions.versions.delete(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.authorizations.functions.versions.delete(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### get <a name="get"></a>
Get Account Authorizations For Function Version

Gets NVIDIA Cloud Account IDs that are authorized to invoke specified function  version. Response includes authorized accounts that were added specifically  to the function version and the inherited authorized accounts that were  added at the function level. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

**API Endpoint**: `GET /v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.authorizations.functions.versions.get(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.authorizations.functions.versions.get(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### create <a name="create"></a>
Authorize Accounts To Invoke Function Version

Authorizes additional NVIDIA Cloud Accounts to invoke a specific function  version. By default, a function belongs to the NVIDIA Cloud Account that  created it, and the credentials used for function invocation must reference  the same NVIDIA Cloud Account. Upon invocation of this endpoint, any existing  authorized accounts will be overwritten by the newly specified authorized  accounts. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

**API Endpoint**: `POST /v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.authorizations.functions.versions.create(
    authorized_parties=[{"nca_id": "string"}],
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.authorizations.functions.versions.create(
    authorized_parties=[{"nca_id": "string"}],
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```
