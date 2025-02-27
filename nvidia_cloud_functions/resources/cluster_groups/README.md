
### list <a name="list"></a>
List Cluster Groups

Lists Cluster Groups for the current account. The response includes cluster  groups defined specifically in the current account and publicly available  cluster groups such as GFN, OCI, etc. Requires a bearer token with 'list_cluster_groups' scope in HTTP Authorization header. 

**API Endpoint**: `GET /v2/nvcf/clusterGroups`

#### Synchronous Client

```python
from nvidia_cloud_functions import Client

client = Client()
res = client.cluster_groups.list_fn()
```

#### Asynchronous Client

```python
from nvidia_cloud_functions import AsyncClient

client = AsyncClient()
res = await client.cluster_groups.list_fn()
```
