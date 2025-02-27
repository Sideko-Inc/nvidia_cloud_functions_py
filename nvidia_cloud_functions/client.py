import httpx
import typing

from nvidia_cloud_functions.resources.exec import AsyncExecClient, ExecClient
from nvidia_cloud_functions.resources.assets import AssetsClient, AsyncAssetsClient
from nvidia_cloud_functions.resources.deployments import (
    AsyncDeploymentsClient,
    DeploymentsClient,
)
from nvidia_cloud_functions.resources.cluster_groups import (
    AsyncClusterGroupsClient,
    ClusterGroupsClient,
)
from nvidia_cloud_functions.environment import Environment
from nvidia_cloud_functions.resources.functions import (
    AsyncFunctionsClient,
    FunctionsClient,
)
from nvidia_cloud_functions.resources.authorizations import (
    AsyncAuthorizationsClient,
    AuthorizationsClient,
)
from nvidia_cloud_functions.core import AsyncBaseClient, SyncBaseClient
from nvidia_cloud_functions.resources.queues import AsyncQueuesClient, QueuesClient
from nvidia_cloud_functions.resources.pexec import AsyncPexecClient, PexecClient


class Client:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        environment: Environment = Environment.PRODUCTION,
    ):
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=(
                httpx.Client(timeout=timeout) if httpx_client is None else httpx_client
            ),
        )

        self.assets = AssetsClient(base_client=self._base_client)

        self.authorizations = AuthorizationsClient(base_client=self._base_client)

        self.deployments = DeploymentsClient(base_client=self._base_client)

        self.functions = FunctionsClient(base_client=self._base_client)

        self.cluster_groups = ClusterGroupsClient(base_client=self._base_client)

        self.exec = ExecClient(base_client=self._base_client)

        self.pexec = PexecClient(base_client=self._base_client)

        self.queues = QueuesClient(base_client=self._base_client)


class AsyncClient:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        environment: Environment = Environment.PRODUCTION,
    ):
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=(
                httpx.AsyncClient(timeout=timeout)
                if httpx_client is None
                else httpx_client
            ),
        )

        self.assets = AsyncAssetsClient(base_client=self._base_client)

        self.authorizations = AsyncAuthorizationsClient(base_client=self._base_client)

        self.deployments = AsyncDeploymentsClient(base_client=self._base_client)

        self.functions = AsyncFunctionsClient(base_client=self._base_client)

        self.cluster_groups = AsyncClusterGroupsClient(base_client=self._base_client)

        self.exec = AsyncExecClient(base_client=self._base_client)

        self.pexec = AsyncPexecClient(base_client=self._base_client)

        self.queues = AsyncQueuesClient(base_client=self._base_client)


def _get_base_url(
    *, base_url: typing.Optional[str] = None, environment: Environment
) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Must include a base_url or environment arguments")
