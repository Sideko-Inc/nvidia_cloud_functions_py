
### delete <a name="delete"></a>
Delete Function

Deletes the specified function version in the authenticated NVIDIA Cloud  Account. Requires a bearer token with 'delete_function' scope in the HTTP  Authorization header. If the function version is public, then Account Admin  cannot delete the function. 

**API Endpoint**: `DELETE /v2/nvcf/functions/{functionId}/versions/{functionVersionId}`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.functions.versions.delete(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.functions.versions.delete(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### list <a name="list"></a>
List Function Versions

Lists details of all the versions of the specified function in the authenticated  NVIDIA Cloud Account. Requires either a bearer token or an api-key with  'list_functions' or 'list_functions_details' scopes in the HTTP Authorization  header. 

**API Endpoint**: `GET /v2/nvcf/functions/{functionId}/versions`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.functions.versions.list(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.functions.versions.list(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```

### get <a name="get"></a>
Get Function Version Details

Retrieves detailed information of the specified function version in the  authenticated NVIDIA Cloud Account. Requires either a bearer token or an  api-key with 'list_functions' or 'list_functions_details' scopes in the HTTP  Authorization header. 

**API Endpoint**: `GET /v2/nvcf/functions/{functionId}/versions/{functionVersionId}`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.functions.versions.get(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.functions.versions.get(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### create <a name="create"></a>
Create Function Version

Creates a version of the specified function within the authenticated NVIDIA  Cloud Account. Requires a bearer token with 'register_function' scope in the  HTTP Authorization header. 

**API Endpoint**: `POST /v2/nvcf/functions/{functionId}/versions`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.functions.versions.create(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    inference_url="http://www.example.com",
    name="string",
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.functions.versions.create(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    inference_url="http://www.example.com",
    name="string",
)
```
