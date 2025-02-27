
### list <a name="list"></a>
List Functions

Lists all the functions associated with the authenticated NVIDIA Cloud Account.  Requires either a bearer token or an api-key with 'list_functions' or  'list_functions_details' scopes in the HTTP Authorization header.

**API Endpoint**: `GET /v2/nvcf/functions`

#### Synchronous Client

```python
from nvidia_cloud_functions import Client

client = Client()
res = client.functions.list()
```

#### Asynchronous Client

```python
from nvidia_cloud_functions import AsyncClient

client = AsyncClient()
res = await client.functions.list()
```

### create <a name="create"></a>
Create Function

Creates a new function within the authenticated NVIDIA Cloud Account. Requires a  bearer token with 'register_function' scope in the HTTP Authorization header. 

**API Endpoint**: `POST /v2/nvcf/functions`

#### Synchronous Client

```python
from nvidia_cloud_functions import Client

client = Client()
res = client.functions.create(inference_url="http://www.example.com", name="string")
```

#### Asynchronous Client

```python
from nvidia_cloud_functions import AsyncClient

client = AsyncClient()
res = await client.functions.create(
    inference_url="http://www.example.com", name="string"
)
```
