import typing

from nvidia_cloud_functions.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from nvidia_cloud_functions.types import models


class PositionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list_fn(
        self,
        *,
        request_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetPositionInQueueResponse:
        """
        Queue Position

        Using the specified function invocation request id, returns the estimated  position of the corresponding message up to 1000 in the queue. Requires a bearer token or an api-key with 'queue_details' scope in the HTTP  Authorization header.

        GET /v2/nvcf/queues/{requestId}/position

        Args:
            requestId: Function invocation request id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.queues.position.list_fn(
            request_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```

        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/queues/{request_id}/position",
            cast_to=models.GetPositionInQueueResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncPositionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list_fn(
        self,
        *,
        request_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetPositionInQueueResponse:
        """
        Queue Position

        Using the specified function invocation request id, returns the estimated  position of the corresponding message up to 1000 in the queue. Requires a bearer token or an api-key with 'queue_details' scope in the HTTP  Authorization header.

        GET /v2/nvcf/queues/{requestId}/position

        Args:
            requestId: Function invocation request id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.queues.position.list_fn(
            request_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```

        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/queues/{request_id}/position",
            cast_to=models.GetPositionInQueueResponse,
            request_options=request_options or default_request_options(),
        )
