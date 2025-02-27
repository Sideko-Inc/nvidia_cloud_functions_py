from nvidia_cloud_functions.core import AsyncBaseClient, SyncBaseClient
from nvidia_cloud_functions.resources.authorizations.functions import (
    AsyncFunctionsClient,
    FunctionsClient,
)


class AuthorizationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

        self.functions = FunctionsClient(base_client=self._base_client)


class AsyncAuthorizationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

        self.functions = AsyncFunctionsClient(base_client=self._base_client)
