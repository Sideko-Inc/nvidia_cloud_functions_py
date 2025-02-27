import typing

from nvidia_cloud_functions_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from nvidia_cloud_functions_py.types import models


class HealthClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list_fn(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.HealthComponent:
        """
        Get Health Information

        Get Health Information about this service

        GET /health/**

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.health.list_fn()
        ```

        """
        return self._base_client.request(
            method="GET",
            path="/health/**",
            cast_to=models.HealthComponent,
            request_options=request_options or default_request_options(),
        )


class AsyncHealthClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list_fn(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.HealthComponent:
        """
        Get Health Information

        Get Health Information about this service

        GET /health/**

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.health.list_fn()
        ```

        """
        return await self._base_client.request(
            method="GET",
            path="/health/**",
            cast_to=models.HealthComponent,
            request_options=request_options or default_request_options(),
        )
