import typing

from nvidia_cloud_functions_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from nvidia_cloud_functions_py.types import models


class StatusClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        request_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvokeFunctionResponse:
        """
        Poll For Result Using Function Invocation Request

        Retrieves the status of an in-progress or pending request using its unique  invocation request ID. If the result is available, it will be included in  the response, marking the request as fulfilled. Conversely, if the result is  not yet available, the request is deemed pending. Access to this endpoint  mandates inclusion of either a bearer token or an api-key with  'invoke_function' scope in the HTTP Authorization header. In-progress responses are returned in order. If no in-progress response is received  during polling you will receive the most recent in-progress response. Only the first  256 unread in-progress messages are kept.

        GET /v2/nvcf/exec/status/{requestId}

        Args:
            requestId: Function invocation request id
            request_options: Additional options to customize the HTTP request

        Returns:
            Invocation is fulfilled

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.nvcf.exec.status.get(request_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
        ```

        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/exec/status/{request_id}",
            cast_to=models.InvokeFunctionResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncStatusClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        request_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvokeFunctionResponse:
        """
        Poll For Result Using Function Invocation Request

        Retrieves the status of an in-progress or pending request using its unique  invocation request ID. If the result is available, it will be included in  the response, marking the request as fulfilled. Conversely, if the result is  not yet available, the request is deemed pending. Access to this endpoint  mandates inclusion of either a bearer token or an api-key with  'invoke_function' scope in the HTTP Authorization header. In-progress responses are returned in order. If no in-progress response is received  during polling you will receive the most recent in-progress response. Only the first  256 unread in-progress messages are kept.

        GET /v2/nvcf/exec/status/{requestId}

        Args:
            requestId: Function invocation request id
            request_options: Additional options to customize the HTTP request

        Returns:
            Invocation is fulfilled

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.nvcf.exec.status.get(
            request_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```

        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/exec/status/{request_id}",
            cast_to=models.InvokeFunctionResponse,
            request_options=request_options or default_request_options(),
        )
