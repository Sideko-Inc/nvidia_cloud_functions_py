from nvidia_cloud_functions.core import AsyncBaseClient, SyncBaseClient
from nvidia_cloud_functions.resources.queues.functions import (
    AsyncFunctionsClient,
    FunctionsClient,
)
from nvidia_cloud_functions.resources.queues.position import (
    AsyncPositionClient,
    PositionClient,
)


class QueuesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

        self.functions = FunctionsClient(base_client=self._base_client)

        self.position = PositionClient(base_client=self._base_client)


class AsyncQueuesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

        self.functions = AsyncFunctionsClient(base_client=self._base_client)

        self.position = AsyncPositionClient(base_client=self._base_client)
