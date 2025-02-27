
# Cloud Functions Python SDK

## Overview
nvidia-cloud-functions (2.87.3)

### Synchronous Client

```python
from nvidia_cloud_functions_py import Client

client = Client()
```

### Asynchronous Client

```python
from nvidia_cloud_functions_py import AsyncClient

client = AsyncClient()
```

## Module Documentation and Snippets

### [assets](nvidia_cloud_functions/resources/assets/README.md)

* [create](nvidia_cloud_functions/resources/assets/README.md#create) - Create Asset
* [delete](nvidia_cloud_functions/resources/assets/README.md#delete) - Delete Asset
* [get](nvidia_cloud_functions/resources/assets/README.md#get) - Show Asset Details
* [list](nvidia_cloud_functions/resources/assets/README.md#list) - List Assets

### [authorizations.functions](nvidia_cloud_functions/resources/authorizations/functions/README.md)

* [create](nvidia_cloud_functions/resources/authorizations/functions/README.md#create) - Authorize Accounts To Invoke Function
* [delete](nvidia_cloud_functions/resources/authorizations/functions/README.md#delete) - Delete All Extra Authorizations For Function
* [get](nvidia_cloud_functions/resources/authorizations/functions/README.md#get) - List Account Authorizations For Function

### [authorizations.functions.add](nvidia_cloud_functions/resources/authorizations/functions/add/README.md)

* [patch](nvidia_cloud_functions/resources/authorizations/functions/add/README.md#patch) - Authorize Additional Account To Invoke Function

### [authorizations.functions.remove](nvidia_cloud_functions/resources/authorizations/functions/remove/README.md)

* [patch](nvidia_cloud_functions/resources/authorizations/functions/remove/README.md#patch) - Unauthorize Account From Invoking Function

### [authorizations.functions.versions](nvidia_cloud_functions/resources/authorizations/functions/versions/README.md)

* [create](nvidia_cloud_functions/resources/authorizations/functions/versions/README.md#create) - Authorize Accounts To Invoke Function Version
* [delete](nvidia_cloud_functions/resources/authorizations/functions/versions/README.md#delete) - Delete All Extra Authorizations For Function Version
* [get](nvidia_cloud_functions/resources/authorizations/functions/versions/README.md#get) - Get Account Authorizations For Function Version

### [authorizations.functions.versions.add](nvidia_cloud_functions/resources/authorizations/functions/versions/add/README.md)

* [patch](nvidia_cloud_functions/resources/authorizations/functions/versions/add/README.md#patch) - Authorize Additional Account To Invoke Function Version

### [authorizations.functions.versions.remove](nvidia_cloud_functions/resources/authorizations/functions/versions/remove/README.md)

* [patch](nvidia_cloud_functions/resources/authorizations/functions/versions/remove/README.md#patch) - Unauthorize Account From Invoking Function Version

### [cluster_groups](nvidia_cloud_functions/resources/cluster_groups/README.md)

* [list](nvidia_cloud_functions/resources/cluster_groups/README.md#list) - List Cluster Groups

### [deployments.functions.versions](nvidia_cloud_functions/resources/deployments/functions/versions/README.md)

* [create](nvidia_cloud_functions/resources/deployments/functions/versions/README.md#create) - Deploy Function
* [delete](nvidia_cloud_functions/resources/deployments/functions/versions/README.md#delete) - Delete Function Deployment
* [get](nvidia_cloud_functions/resources/deployments/functions/versions/README.md#get) - Get Function Deployment Details
* [update](nvidia_cloud_functions/resources/deployments/functions/versions/README.md#update) - Update Function Deployment

### [exec.functions](nvidia_cloud_functions/resources/exec/functions/README.md)

* [create](nvidia_cloud_functions/resources/exec/functions/README.md#create) - Call Function

### [exec.functions.versions](nvidia_cloud_functions/resources/exec/functions/versions/README.md)

* [create](nvidia_cloud_functions/resources/exec/functions/versions/README.md#create) - Call Function

### [exec.status](nvidia_cloud_functions/resources/exec/status/README.md)

* [get](nvidia_cloud_functions/resources/exec/status/README.md#get) - Poll For Result Using Function Invocation Request

### [functions](nvidia_cloud_functions/resources/functions/README.md)

* [create](nvidia_cloud_functions/resources/functions/README.md#create) - Create Function
* [list](nvidia_cloud_functions/resources/functions/README.md#list) - List Functions

### [functions.ids](nvidia_cloud_functions/resources/functions/ids/README.md)

* [list](nvidia_cloud_functions/resources/functions/ids/README.md#list) - List Function Ids

### [functions.versions](nvidia_cloud_functions/resources/functions/versions/README.md)

* [create](nvidia_cloud_functions/resources/functions/versions/README.md#create) - Create Function Version
* [delete](nvidia_cloud_functions/resources/functions/versions/README.md#delete) - Delete Function
* [get](nvidia_cloud_functions/resources/functions/versions/README.md#get) - Get Function Version Details
* [list](nvidia_cloud_functions/resources/functions/versions/README.md#list) - List Function Versions

### [health](nvidia_cloud_functions/resources/health/README.md)

* [list](nvidia_cloud_functions/resources/health/README.md#list) - Get Health Information

### [pexec.functions](nvidia_cloud_functions/resources/pexec/functions/README.md)

* [create](nvidia_cloud_functions/resources/pexec/functions/README.md#create) - Call Function

### [pexec.functions.versions](nvidia_cloud_functions/resources/pexec/functions/versions/README.md)

* [create](nvidia_cloud_functions/resources/pexec/functions/versions/README.md#create) - Call Function

### [pexec.status](nvidia_cloud_functions/resources/pexec/status/README.md)

* [get](nvidia_cloud_functions/resources/pexec/status/README.md#get) - Poll For Result Using Function Invocation Request

### [queues.functions](nvidia_cloud_functions/resources/queues/functions/README.md)

* [get](nvidia_cloud_functions/resources/queues/functions/README.md#get) - Queue Details

### [queues.functions.versions](nvidia_cloud_functions/resources/queues/functions/versions/README.md)

* [get](nvidia_cloud_functions/resources/queues/functions/versions/README.md#get) - Queue Details

### [queues.position](nvidia_cloud_functions/resources/queues/position/README.md)

* [list](nvidia_cloud_functions/resources/queues/position/README.md#list) - Queue Position

<!-- MODULE DOCS END -->
