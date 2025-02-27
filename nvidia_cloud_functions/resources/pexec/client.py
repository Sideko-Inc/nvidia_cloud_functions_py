from nvidia_cloud_functions.core import AsyncBaseClient, SyncBaseClient
from nvidia_cloud_functions.resources.pexec.status import (
    AsyncStatusClient,
    StatusClient,
)
from nvidia_cloud_functions.resources.pexec.functions import (
    AsyncFunctionsClient,
    FunctionsClient,
)


class PexecClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

        self.status = StatusClient(base_client=self._base_client)

        self.functions = FunctionsClient(base_client=self._base_client)


class AsyncPexecClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

        self.status = AsyncStatusClient(base_client=self._base_client)

        self.functions = AsyncFunctionsClient(base_client=self._base_client)
