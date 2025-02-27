import typing

from nvidia_cloud_functions.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)
from nvidia_cloud_functions.types import models, params


class AssetsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, asset_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete Asset

        Deletes asset belonging to the current NVIDIA Cloud Account. Requires either  a bearer token or an api-key with 'invoke_function' scope in the HTTP  Authorization header.

        DELETE /v2/nvcf/assets/{assetId}

        Args:
            assetId: Id of the asset to be deleted
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.assets.delete(asset_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
        ```

        """
        self._base_client.request(
            method="DELETE",
            path=f"/v2/nvcf/assets/{asset_id}",
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list_fn(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ListAssetsResponse:
        """
        List Assets

        List assets owned by the current NVIDIA Cloud Account. Requires either a  bearer token or an api-key with invoke_function scope in the HTTP Authorization  header.

        GET /v2/nvcf/assets

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.assets.list_fn()
        ```

        """
        return self._base_client.request(
            method="GET",
            path="/v2/nvcf/assets",
            cast_to=models.ListAssetsResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, asset_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.AssetResponse:
        """
        Show Asset Details

        Returns details for the specified asset-id belonging to the current NVIDIA  Cloud Account. Requires either a bearer token or an api-key with  'invoke_function' scope in the HTTP Authorization header.

        GET /v2/nvcf/assets/{assetId}

        Args:
            assetId: Asset id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.assets.get(asset_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
        ```

        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/assets/{asset_id}",
            cast_to=models.AssetResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        content_type: str,
        description: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateAssetResponse:
        """
        Create Asset

        Creates a unique id representing an asset and a pre-signed URL to upload the  asset artifact to AWS S3 bucket for the NVIDIA Cloud Account. Requires either  a bearer token or an api-key with 'invoke_function' scope in the HTTP  Authorization header.

        POST /v2/nvcf/assets

        Args:
            contentType: Content type of the asset such image/png, image/jpeg, etc.
            description: Asset description
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.assets.create(content_type="string", description="string")
        ```

        """
        _json = to_encodable(
            item={"content_type": content_type, "description": description},
            dump_with=params._SerializerCreateAssetRequest,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/nvcf/assets",
            json=_json,
            cast_to=models.CreateAssetResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAssetsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, asset_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete Asset

        Deletes asset belonging to the current NVIDIA Cloud Account. Requires either  a bearer token or an api-key with 'invoke_function' scope in the HTTP  Authorization header.

        DELETE /v2/nvcf/assets/{assetId}

        Args:
            assetId: Id of the asset to be deleted
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.assets.delete(asset_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
        ```

        """
        await self._base_client.request(
            method="DELETE",
            path=f"/v2/nvcf/assets/{asset_id}",
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list_fn(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ListAssetsResponse:
        """
        List Assets

        List assets owned by the current NVIDIA Cloud Account. Requires either a  bearer token or an api-key with invoke_function scope in the HTTP Authorization  header.

        GET /v2/nvcf/assets

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.assets.list_fn()
        ```

        """
        return await self._base_client.request(
            method="GET",
            path="/v2/nvcf/assets",
            cast_to=models.ListAssetsResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, asset_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.AssetResponse:
        """
        Show Asset Details

        Returns details for the specified asset-id belonging to the current NVIDIA  Cloud Account. Requires either a bearer token or an api-key with  'invoke_function' scope in the HTTP Authorization header.

        GET /v2/nvcf/assets/{assetId}

        Args:
            assetId: Asset id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.assets.get(asset_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
        ```

        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/assets/{asset_id}",
            cast_to=models.AssetResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        content_type: str,
        description: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateAssetResponse:
        """
        Create Asset

        Creates a unique id representing an asset and a pre-signed URL to upload the  asset artifact to AWS S3 bucket for the NVIDIA Cloud Account. Requires either  a bearer token or an api-key with 'invoke_function' scope in the HTTP  Authorization header.

        POST /v2/nvcf/assets

        Args:
            contentType: Content type of the asset such image/png, image/jpeg, etc.
            description: Asset description
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.assets.create(content_type="string", description="string")
        ```

        """
        _json = to_encodable(
            item={"content_type": content_type, "description": description},
            dump_with=params._SerializerCreateAssetRequest,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/nvcf/assets",
            json=_json,
            cast_to=models.CreateAssetResponse,
            request_options=request_options or default_request_options(),
        )
