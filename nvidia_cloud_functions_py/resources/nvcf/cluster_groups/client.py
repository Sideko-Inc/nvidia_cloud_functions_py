import typing

from nvidia_cloud_functions_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from nvidia_cloud_functions_py.types import models


class ClusterGroupsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list_fn(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ClusterGroupsResponse:
        """
        List Cluster Groups

        Lists Cluster Groups for the current account. The response includes cluster  groups defined specifically in the current account and publicly available  cluster groups such as GFN, OCI, etc. Requires a bearer token with 'list_cluster_groups' scope in HTTP Authorization header.

        GET /v2/nvcf/clusterGroups

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.nvcf.cluster_groups.list_fn()
        ```

        """
        return self._base_client.request(
            method="GET",
            path="/v2/nvcf/clusterGroups",
            cast_to=models.ClusterGroupsResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncClusterGroupsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list_fn(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ClusterGroupsResponse:
        """
        List Cluster Groups

        Lists Cluster Groups for the current account. The response includes cluster  groups defined specifically in the current account and publicly available  cluster groups such as GFN, OCI, etc. Requires a bearer token with 'list_cluster_groups' scope in HTTP Authorization header.

        GET /v2/nvcf/clusterGroups

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.nvcf.cluster_groups.list_fn()
        ```

        """
        return await self._base_client.request(
            method="GET",
            path="/v2/nvcf/clusterGroups",
            cast_to=models.ClusterGroupsResponse,
            request_options=request_options or default_request_options(),
        )
