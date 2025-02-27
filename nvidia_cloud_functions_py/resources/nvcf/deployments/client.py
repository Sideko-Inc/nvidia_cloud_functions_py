from nvidia_cloud_functions_py.core import AsyncBaseClient, SyncBaseClient
from nvidia_cloud_functions_py.resources.nvcf.deployments.functions import (
    AsyncFunctionsClient,
    FunctionsClient,
)


class DeploymentsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

        self.functions = FunctionsClient(base_client=self._base_client)


class AsyncDeploymentsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

        self.functions = AsyncFunctionsClient(base_client=self._base_client)
