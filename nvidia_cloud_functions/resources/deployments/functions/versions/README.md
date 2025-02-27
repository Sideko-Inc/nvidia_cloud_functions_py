
### delete <a name="delete"></a>
Delete Function Deployment

Deletes the deployment associated with the specified function. Upon  deletion, any active instances will be terminated, and the function's status  will transition to 'INACTIVE'. To undeploy a function version gracefully,  specify 'graceful=true' query parameter, allowing current tasks to complete  before terminating the instances. If the specified function version is public,  then Account Admin cannot perform this operation. Access to this endpoint mandates a bearer token with 'deploy_function' scope in the  HTTP Authorization header. 

**API Endpoint**: `DELETE /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}`

#### Synchronous Client

```python
from nvidia_cloud_functions import Client

client = Client()
res = client.deployments.functions.versions.delete(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions import AsyncClient

client = AsyncClient()
res = await client.deployments.functions.versions.delete(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### get <a name="get"></a>
Get Function Deployment Details

Allows Account Admins to retrieve the deployment details of the specified  function version. Access to this endpoint mandates a bearer token with 'deploy_function' scope in the  HTTP Authorization header. 

**API Endpoint**: `GET /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}`

#### Synchronous Client

```python
from nvidia_cloud_functions import Client

client = Client()
res = client.deployments.functions.versions.get(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions import AsyncClient

client = AsyncClient()
res = await client.deployments.functions.versions.get(
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### create <a name="create"></a>
Deploy Function

Initiates deployment for the specified function version. Upon invocation of  this endpoint, the function's status transitions to 'DEPLOYING'. If the  specified function version is public, then Account Admin cannot perform this  operation. Access to this endpoint mandates a bearer token with 'deploy_function' scope in the  HTTP Authorization header. 

**API Endpoint**: `POST /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}`

#### Synchronous Client

```python
from nvidia_cloud_functions import Client

client = Client()
res = client.deployments.functions.versions.create(
    deployment_specifications=[
        {
            "backend": "string",
            "gpu": "string",
            "max_instances": 123,
            "min_instances": 123,
        }
    ],
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions import AsyncClient

client = AsyncClient()
res = await client.deployments.functions.versions.create(
    deployment_specifications=[
        {
            "backend": "string",
            "gpu": "string",
            "max_instances": 123,
            "min_instances": 123,
        }
    ],
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### update <a name="update"></a>
Update Function Deployment

Updates the deployment specs of the specified function version. It's important  to note that GPU type and backend configurations cannot be modified through  this endpoint. If the specified function is public, then Account Admin cannot  perform this operation. Access to this endpoint mandates a bearer token with 'deploy_function' scope in the  HTTP Authorization header. 

**API Endpoint**: `PUT /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}`

#### Synchronous Client

```python
from nvidia_cloud_functions import Client

client = Client()
res = client.deployments.functions.versions.update(
    deployment_specifications=[
        {
            "backend": "string",
            "gpu": "string",
            "max_instances": 123,
            "min_instances": 123,
        }
    ],
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

#### Asynchronous Client

```python
from nvidia_cloud_functions import AsyncClient

client = AsyncClient()
res = await client.deployments.functions.versions.update(
    deployment_specifications=[
        {
            "backend": "string",
            "gpu": "string",
            "max_instances": 123,
            "min_instances": 123,
        }
    ],
    function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```
