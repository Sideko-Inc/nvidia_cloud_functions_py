from nvidia_cloud_functions_py.core import AsyncBaseClient, SyncBaseClient
from nvidia_cloud_functions_py.resources.nvcf.assets import (
    AssetsClient,
    AsyncAssetsClient,
)
from nvidia_cloud_functions_py.resources.nvcf.authorizations import (
    AsyncAuthorizationsClient,
    AuthorizationsClient,
)
from nvidia_cloud_functions_py.resources.nvcf.deployments import (
    AsyncDeploymentsClient,
    DeploymentsClient,
)
from nvidia_cloud_functions_py.resources.nvcf.functions import (
    AsyncFunctionsClient,
    FunctionsClient,
)
from nvidia_cloud_functions_py.resources.nvcf.cluster_groups import (
    AsyncClusterGroupsClient,
    ClusterGroupsClient,
)
from nvidia_cloud_functions_py.resources.nvcf.exec import AsyncExecClient, ExecClient
from nvidia_cloud_functions_py.resources.nvcf.pexec import AsyncPexecClient, PexecClient
from nvidia_cloud_functions_py.resources.nvcf.queues import (
    AsyncQueuesClient,
    QueuesClient,
)


class NvcfClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

        self.assets = AssetsClient(base_client=self._base_client)

        self.authorizations = AuthorizationsClient(base_client=self._base_client)

        self.deployments = DeploymentsClient(base_client=self._base_client)

        self.functions = FunctionsClient(base_client=self._base_client)

        self.cluster_groups = ClusterGroupsClient(base_client=self._base_client)

        self.exec = ExecClient(base_client=self._base_client)

        self.pexec = PexecClient(base_client=self._base_client)

        self.queues = QueuesClient(base_client=self._base_client)


class AsyncNvcfClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

        self.assets = AsyncAssetsClient(base_client=self._base_client)

        self.authorizations = AsyncAuthorizationsClient(base_client=self._base_client)

        self.deployments = AsyncDeploymentsClient(base_client=self._base_client)

        self.functions = AsyncFunctionsClient(base_client=self._base_client)

        self.cluster_groups = AsyncClusterGroupsClient(base_client=self._base_client)

        self.exec = AsyncExecClient(base_client=self._base_client)

        self.pexec = AsyncPexecClient(base_client=self._base_client)

        self.queues = AsyncQueuesClient(base_client=self._base_client)
