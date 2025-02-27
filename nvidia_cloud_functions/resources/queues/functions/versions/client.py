import typing

from nvidia_cloud_functions.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from nvidia_cloud_functions.types import models


class VersionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        function_id: str,
        version_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetQueuesResponse:
        """
        Queue Details

        Provides details of all the queues associated with the specified function.  If a function has multiple versions and they are all deployed, then the  response includes details of all the queues. If the specified function  is public, then Account Admin cannot perform this operation. Requires a bearer token or an api-key with 'queue_details' scope in the HTTP  Authorization header.

        GET /v2/nvcf/queues/functions/{functionId}/versions/{versionId}

        Args:
            functionId: Function id
            versionId: Function version id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.queues.functions.versions.get(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/queues/functions/{function_id}/versions/{version_id}",
            cast_to=models.GetQueuesResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncVersionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        function_id: str,
        version_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetQueuesResponse:
        """
        Queue Details

        Provides details of all the queues associated with the specified function.  If a function has multiple versions and they are all deployed, then the  response includes details of all the queues. If the specified function  is public, then Account Admin cannot perform this operation. Requires a bearer token or an api-key with 'queue_details' scope in the HTTP  Authorization header.

        GET /v2/nvcf/queues/functions/{functionId}/versions/{versionId}

        Args:
            functionId: Function id
            versionId: Function version id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.queues.functions.versions.get(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/queues/functions/{function_id}/versions/{version_id}",
            cast_to=models.GetQueuesResponse,
            request_options=request_options or default_request_options(),
        )
