import typing

from nvidia_cloud_functions_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from nvidia_cloud_functions_py.resources.nvcf.queues.functions.versions import (
    AsyncVersionsClient,
    VersionsClient,
)
from nvidia_cloud_functions_py.types import models


class FunctionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

        self.versions = VersionsClient(base_client=self._base_client)

    def get(
        self,
        *,
        function_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetQueuesResponse:
        """
        Queue Details

        Provides details of all the queues associated with the specified function.  If a function has multiple versions and they are all deployed, then the  response includes details of all the queues. If the specified function  is public, then Account Admin cannot perform this operation. Requires a bearer token or an api-key with 'queue_details' scope in the HTTP  Authorization header.

        GET /v2/nvcf/queues/functions/{functionId}

        Args:
            functionId: Function id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.nvcf.queues.functions.get(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```

        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/queues/functions/{function_id}",
            cast_to=models.GetQueuesResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncFunctionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

        self.versions = AsyncVersionsClient(base_client=self._base_client)

    async def get(
        self,
        *,
        function_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetQueuesResponse:
        """
        Queue Details

        Provides details of all the queues associated with the specified function.  If a function has multiple versions and they are all deployed, then the  response includes details of all the queues. If the specified function  is public, then Account Admin cannot perform this operation. Requires a bearer token or an api-key with 'queue_details' scope in the HTTP  Authorization header.

        GET /v2/nvcf/queues/functions/{functionId}

        Args:
            functionId: Function id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.nvcf.queues.functions.get(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```

        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/queues/functions/{function_id}",
            cast_to=models.GetQueuesResponse,
            request_options=request_options or default_request_options(),
        )
