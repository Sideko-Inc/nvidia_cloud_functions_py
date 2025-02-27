
### delete <a name="delete"></a>
Delete Asset

Deletes asset belonging to the current NVIDIA Cloud Account. Requires either  a bearer token or an api-key with 'invoke_function' scope in the HTTP  Authorization header.

**API Endpoint**: `DELETE /v2/nvcf/assets/{assetId}`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.assets.delete(asset_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.assets.delete(asset_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
```

### list <a name="list"></a>
List Assets

List assets owned by the current NVIDIA Cloud Account. Requires either a  bearer token or an api-key with invoke_function scope in the HTTP Authorization  header. 

**API Endpoint**: `GET /v2/nvcf/assets`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.assets.list_fn()
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.assets.list_fn()
```

### get <a name="get"></a>
Show Asset Details

Returns details for the specified asset-id belonging to the current NVIDIA  Cloud Account. Requires either a bearer token or an api-key with  'invoke_function' scope in the HTTP Authorization header. 

**API Endpoint**: `GET /v2/nvcf/assets/{assetId}`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.assets.get(asset_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.assets.get(asset_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
```

### create <a name="create"></a>
Create Asset

Creates a unique id representing an asset and a pre-signed URL to upload the  asset artifact to AWS S3 bucket for the NVIDIA Cloud Account. Requires either  a bearer token or an api-key with 'invoke_function' scope in the HTTP  Authorization header.

**API Endpoint**: `POST /v2/nvcf/assets`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.nvcf.assets.create(content_type="string", description="string")
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.nvcf.assets.create(content_type="string", description="string")
```
