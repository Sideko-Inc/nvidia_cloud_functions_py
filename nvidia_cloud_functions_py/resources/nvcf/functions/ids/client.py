import typing
import typing_extensions

from nvidia_cloud_functions_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from nvidia_cloud_functions_py.types import models


class IdsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list_fn(
        self,
        *,
        visibility: typing.Union[
            typing.Optional[
                typing.List[
                    typing_extensions.Literal["authorized", "private", "public"]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ListFunctionIdsResponse:
        """
        List Function Ids

        Lists ids of all the functions in the authenticated NVIDIA Cloud Account.  Requires either a bearer token or an api-key with 'list_functions' or  'list_functions_details' scopes in the HTTP Authorization header.

        GET /v2/nvcf/functions/ids

        Args:
            visibility: Query param 'visibility' indicates the kind of functions to be included  in the response.
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.nvcf.functions.ids.list_fn()
        ```

        """
        _query: QueryParams = {}
        if not isinstance(visibility, type_utils.NotGiven):
            encode_query_param(
                _query,
                "visibility",
                to_encodable(
                    item=visibility,
                    dump_with=typing.List[
                        typing_extensions.Literal["authorized", "private", "public"]
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v2/nvcf/functions/ids",
            query_params=_query,
            cast_to=models.ListFunctionIdsResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncIdsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list_fn(
        self,
        *,
        visibility: typing.Union[
            typing.Optional[
                typing.List[
                    typing_extensions.Literal["authorized", "private", "public"]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ListFunctionIdsResponse:
        """
        List Function Ids

        Lists ids of all the functions in the authenticated NVIDIA Cloud Account.  Requires either a bearer token or an api-key with 'list_functions' or  'list_functions_details' scopes in the HTTP Authorization header.

        GET /v2/nvcf/functions/ids

        Args:
            visibility: Query param 'visibility' indicates the kind of functions to be included  in the response.
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.nvcf.functions.ids.list_fn()
        ```

        """
        _query: QueryParams = {}
        if not isinstance(visibility, type_utils.NotGiven):
            encode_query_param(
                _query,
                "visibility",
                to_encodable(
                    item=visibility,
                    dump_with=typing.List[
                        typing_extensions.Literal["authorized", "private", "public"]
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v2/nvcf/functions/ids",
            query_params=_query,
            cast_to=models.ListFunctionIdsResponse,
            request_options=request_options or default_request_options(),
        )
