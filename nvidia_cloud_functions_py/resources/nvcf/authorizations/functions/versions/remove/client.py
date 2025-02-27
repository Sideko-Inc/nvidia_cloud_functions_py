import typing

from nvidia_cloud_functions_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)
from nvidia_cloud_functions_py.types import models, params


class RemoveClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def patch(
        self,
        *,
        authorized_party: params.AuthorizedPartyDto,
        function_id: str,
        function_version_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AuthorizedPartiesResponse:
        """
        Unauthorize Account From Invoking Function Version

        Removes the specified NVIDIA Cloud Account from the set of authorized accounts  that are directly associated with specified function version. If the specified  function version does not have any of its own(not inherited) authorized  accounts, it results in a response with status 404. Also, if the specified  authorized account is not in the set of existing authorized parties that are  directly associated with the specified function version, it results in a  response with status code 400. If the specified function version is public,  then Account Admin cannot perform this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header

        PATCH /v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}/remove

        Args:
            authorizedParty: Data Transfer Object(DTO) representing an authorized party.
            functionId: Function id
            functionVersionId: Function version
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.nvcf.authorizations.functions.versions.remove.patch(
            authorized_party={"nca_id": "string"},
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        _json = to_encodable(
            item={"authorized_party": authorized_party},
            dump_with=params._SerializerPatchAuthorizedPartyRequest,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/nvcf/authorizations/functions/{function_id}/versions/{function_version_id}/remove",
            json=_json,
            cast_to=models.AuthorizedPartiesResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncRemoveClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def patch(
        self,
        *,
        authorized_party: params.AuthorizedPartyDto,
        function_id: str,
        function_version_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AuthorizedPartiesResponse:
        """
        Unauthorize Account From Invoking Function Version

        Removes the specified NVIDIA Cloud Account from the set of authorized accounts  that are directly associated with specified function version. If the specified  function version does not have any of its own(not inherited) authorized  accounts, it results in a response with status 404. Also, if the specified  authorized account is not in the set of existing authorized parties that are  directly associated with the specified function version, it results in a  response with status code 400. If the specified function version is public,  then Account Admin cannot perform this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header

        PATCH /v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}/remove

        Args:
            authorizedParty: Data Transfer Object(DTO) representing an authorized party.
            functionId: Function id
            functionVersionId: Function version
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.nvcf.authorizations.functions.versions.remove.patch(
            authorized_party={"nca_id": "string"},
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        _json = to_encodable(
            item={"authorized_party": authorized_party},
            dump_with=params._SerializerPatchAuthorizedPartyRequest,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/nvcf/authorizations/functions/{function_id}/versions/{function_version_id}/remove",
            json=_json,
            cast_to=models.AuthorizedPartiesResponse,
            request_options=request_options or default_request_options(),
        )
