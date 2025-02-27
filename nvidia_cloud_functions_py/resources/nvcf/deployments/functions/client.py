from nvidia_cloud_functions_py.core import AsyncBaseClient, SyncBaseClient
from nvidia_cloud_functions_py.resources.nvcf.deployments.functions.versions import (
    AsyncVersionsClient,
    VersionsClient,
)


class FunctionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

        self.versions = VersionsClient(base_client=self._base_client)


class AsyncFunctionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

        self.versions = AsyncVersionsClient(base_client=self._base_client)
