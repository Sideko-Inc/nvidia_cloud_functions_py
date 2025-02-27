import typing

from nvidia_cloud_functions_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)
from nvidia_cloud_functions_py.types import models


class VersionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        data: typing.Dict[str, typing.Any],
        function_id: str,
        version_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[
        models.NvcfPexecFunctionsVersionsCreateResponseObj,
        typing.List[models.NvcfPexecFunctionsVersionsCreateResponseArrItem],
    ]:
        """
        Call Function

        Invokes the specified function that was successfully deployed. If the version  is not specified, any active function versions will handle the request. If  the version is specified in the URI, then the request is exclusively processed  by the designated version of the function. By default, this endpoint will block  for 5 seconds. If the request is not fulfilled before the timeout, it's status  is considered in-progress or pending and the response includes HTTP status code  202 with an invocation request ID, indicating that the client should commence  polling for the result using the invocation request ID. Access to this endpoint  mandates inclusion of either a bearer token or an api-key with 'invoke_function'  scope in the HTTP Authorization header. Additionally, this endpoint has the  capability to provide updates on the progress of the request, contingent  upon the workload's provision of such information. In-progress responses are returned in order. If no in-progress response is received  during polling you will receive the most recent in-progress response. Only the first  256 unread in-progress messages are kept.

        POST /v2/nvcf/pexec/functions/{functionId}/versions/{versionId}

        Args:
            data: typing.Dict[str, typing.Any]
            functionId: str
            versionId: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Invocation is fulfilled

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.nvcf.pexec.functions.versions.create(
            data={},
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        _json = to_encodable(item=data, dump_with=typing.Dict[str, typing.Any])
        return self._base_client.request(
            method="POST",
            path=f"/v2/nvcf/pexec/functions/{function_id}/versions/{version_id}",
            json=_json,
            cast_to=typing.Union[
                models.NvcfPexecFunctionsVersionsCreateResponseObj,
                typing.List[models.NvcfPexecFunctionsVersionsCreateResponseArrItem],
            ],
            request_options=request_options or default_request_options(),
        )


class AsyncVersionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        data: typing.Dict[str, typing.Any],
        function_id: str,
        version_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[
        models.NvcfPexecFunctionsVersionsCreateResponseObj,
        typing.List[models.NvcfPexecFunctionsVersionsCreateResponseArrItem],
    ]:
        """
        Call Function

        Invokes the specified function that was successfully deployed. If the version  is not specified, any active function versions will handle the request. If  the version is specified in the URI, then the request is exclusively processed  by the designated version of the function. By default, this endpoint will block  for 5 seconds. If the request is not fulfilled before the timeout, it's status  is considered in-progress or pending and the response includes HTTP status code  202 with an invocation request ID, indicating that the client should commence  polling for the result using the invocation request ID. Access to this endpoint  mandates inclusion of either a bearer token or an api-key with 'invoke_function'  scope in the HTTP Authorization header. Additionally, this endpoint has the  capability to provide updates on the progress of the request, contingent  upon the workload's provision of such information. In-progress responses are returned in order. If no in-progress response is received  during polling you will receive the most recent in-progress response. Only the first  256 unread in-progress messages are kept.

        POST /v2/nvcf/pexec/functions/{functionId}/versions/{versionId}

        Args:
            data: typing.Dict[str, typing.Any]
            functionId: str
            versionId: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Invocation is fulfilled

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.nvcf.pexec.functions.versions.create(
            data={},
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        _json = to_encodable(item=data, dump_with=typing.Dict[str, typing.Any])
        return await self._base_client.request(
            method="POST",
            path=f"/v2/nvcf/pexec/functions/{function_id}/versions/{version_id}",
            json=_json,
            cast_to=typing.Union[
                models.NvcfPexecFunctionsVersionsCreateResponseObj,
                typing.List[models.NvcfPexecFunctionsVersionsCreateResponseArrItem],
            ],
            request_options=request_options or default_request_options(),
        )
