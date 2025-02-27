
### delete <a name="delete"></a>
Delete All Extra Authorizations For Function

Deletes all the extra NVIDIA Cloud Accounts that were authorized to invoke the  function and all its versions. If a function version has its own set of  authorized accounts, those are not deleted. If the specified function is  public, then Account Admin cannot perform this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

**API Endpoint**: `DELETE /v2/nvcf/authorizations/functions/{functionId}`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.authorizations.functions.delete(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.authorizations.functions.delete(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```

### get <a name="get"></a>
List Account Authorizations For Function

Lists NVIDIA Cloud Account IDs that are authorized to invoke any version of the  specified function. The response includes an array showing authorized accounts  for each version. Individual versions of a function can have their own  authorized accounts. So, each object in the array can have different  authorized accounts listed. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

**API Endpoint**: `GET /v2/nvcf/authorizations/functions/{functionId}`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.authorizations.functions.get(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.authorizations.functions.get(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```

### create <a name="create"></a>
Authorize Accounts To Invoke Function

Authorizes additional NVIDIA Cloud Accounts to invoke any version of the  specified function. By default, a function belongs to the NVIDIA Cloud Account  that created it, and the credentials used for function invocation must  reference the same NVIDIA Cloud Account. Upon invocation of this endpoint, any  existing authorized accounts will be overwritten by the newly specified  authorized accounts. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

**API Endpoint**: `POST /v2/nvcf/authorizations/functions/{functionId}`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.authorizations.functions.create(
    authorized_parties=[{"nca_id": "string"}],
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.authorizations.functions.create(
    authorized_parties=[{"nca_id": "string"}],
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```
