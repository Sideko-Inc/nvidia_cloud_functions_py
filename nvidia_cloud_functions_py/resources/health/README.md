
### list <a name="list"></a>
Get Health Information

Get Health Information about this service

**API Endpoint**: `GET /health/**`

#### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
res = client.health.list()
```

#### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
res = await client.health.list()
```
