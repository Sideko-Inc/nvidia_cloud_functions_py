import typing

from nvidia_cloud_functions.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)
from nvidia_cloud_functions.types import models, params


class AddClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def patch(
        self,
        *,
        authorized_party: params.AuthorizedPartyDto,
        function_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AuthorizedPartiesResponse:
        """
        Authorize Additional Account To Invoke Function

        Adds the specified NVIDIA Cloud Account to the set of authorized accounts that  are can invoke all the versions of the specified function. If the specified  function does not have any existing inheritable authorized accounts, it results  in a response with status 404. If the specified account is already in the set  of existing inheritable authorized accounts, it results in a response with  status code 409. If a function is public, then Account Admin cannot perform  this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header

        PATCH /v2/nvcf/authorizations/functions/{functionId}/add

        Args:
            authorizedParty: Data Transfer Object(DTO) representing an authorized party.
            functionId: Function id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.authorizations.functions.add.patch(
            authorized_party={"nca_id": "string"},
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        _json = to_encodable(
            item={"authorized_party": authorized_party},
            dump_with=params._SerializerPatchAuthorizedPartyRequest,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/nvcf/authorizations/functions/{function_id}/add",
            json=_json,
            cast_to=models.AuthorizedPartiesResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAddClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def patch(
        self,
        *,
        authorized_party: params.AuthorizedPartyDto,
        function_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AuthorizedPartiesResponse:
        """
        Authorize Additional Account To Invoke Function

        Adds the specified NVIDIA Cloud Account to the set of authorized accounts that  are can invoke all the versions of the specified function. If the specified  function does not have any existing inheritable authorized accounts, it results  in a response with status 404. If the specified account is already in the set  of existing inheritable authorized accounts, it results in a response with  status code 409. If a function is public, then Account Admin cannot perform  this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header

        PATCH /v2/nvcf/authorizations/functions/{functionId}/add

        Args:
            authorizedParty: Data Transfer Object(DTO) representing an authorized party.
            functionId: Function id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.authorizations.functions.add.patch(
            authorized_party={"nca_id": "string"},
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        _json = to_encodable(
            item={"authorized_party": authorized_party},
            dump_with=params._SerializerPatchAuthorizedPartyRequest,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/nvcf/authorizations/functions/{function_id}/add",
            json=_json,
            cast_to=models.AuthorizedPartiesResponse,
            request_options=request_options or default_request_options(),
        )
