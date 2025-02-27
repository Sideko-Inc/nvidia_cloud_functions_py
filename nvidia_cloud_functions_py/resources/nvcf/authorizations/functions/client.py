import typing

from nvidia_cloud_functions_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)
from nvidia_cloud_functions_py.resources.nvcf.authorizations.functions.versions import (
    AsyncVersionsClient,
    VersionsClient,
)
from nvidia_cloud_functions_py.resources.nvcf.authorizations.functions.add import (
    AddClient,
    AsyncAddClient,
)
from nvidia_cloud_functions_py.resources.nvcf.authorizations.functions.remove import (
    AsyncRemoveClient,
    RemoveClient,
)
from nvidia_cloud_functions_py.types import models, params


class FunctionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

        self.versions = VersionsClient(base_client=self._base_client)

        self.add = AddClient(base_client=self._base_client)

        self.remove = RemoveClient(base_client=self._base_client)

    def delete(
        self,
        *,
        function_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AuthorizedPartiesResponse:
        """
        Delete All Extra Authorizations For Function

        Deletes all the extra NVIDIA Cloud Accounts that were authorized to invoke the  function and all its versions. If a function version has its own set of  authorized accounts, those are not deleted. If the specified function is  public, then Account Admin cannot perform this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header

        DELETE /v2/nvcf/authorizations/functions/{functionId}

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
        client.nvcf.authorizations.functions.delete(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```

        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/nvcf/authorizations/functions/{function_id}",
            cast_to=models.AuthorizedPartiesResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        function_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ListAuthorizedPartiesResponse:
        """
        List Account Authorizations For Function

        Lists NVIDIA Cloud Account IDs that are authorized to invoke any version of the  specified function. The response includes an array showing authorized accounts  for each version. Individual versions of a function can have their own  authorized accounts. So, each object in the array can have different  authorized accounts listed. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header

        GET /v2/nvcf/authorizations/functions/{functionId}

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
        client.nvcf.authorizations.functions.get(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```

        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/authorizations/functions/{function_id}",
            cast_to=models.ListAuthorizedPartiesResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        authorized_parties: typing.List[params.AuthorizedPartyDto],
        function_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AuthorizedPartiesResponse:
        """
        Authorize Accounts To Invoke Function

        Authorizes additional NVIDIA Cloud Accounts to invoke any version of the  specified function. By default, a function belongs to the NVIDIA Cloud Account  that created it, and the credentials used for function invocation must  reference the same NVIDIA Cloud Account. Upon invocation of this endpoint, any  existing authorized accounts will be overwritten by the newly specified  authorized accounts. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header

        POST /v2/nvcf/authorizations/functions/{functionId}

        Args:
            authorizedParties: Parties authorized to invoke function
            functionId: Function id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.nvcf.authorizations.functions.create(
            authorized_parties=[{"nca_id": "string"}],
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        _json = to_encodable(
            item={"authorized_parties": authorized_parties},
            dump_with=params._SerializerAuthorizedPartiesRequest,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/nvcf/authorizations/functions/{function_id}",
            json=_json,
            cast_to=models.AuthorizedPartiesResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncFunctionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

        self.versions = AsyncVersionsClient(base_client=self._base_client)

        self.add = AsyncAddClient(base_client=self._base_client)

        self.remove = AsyncRemoveClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        function_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AuthorizedPartiesResponse:
        """
        Delete All Extra Authorizations For Function

        Deletes all the extra NVIDIA Cloud Accounts that were authorized to invoke the  function and all its versions. If a function version has its own set of  authorized accounts, those are not deleted. If the specified function is  public, then Account Admin cannot perform this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header

        DELETE /v2/nvcf/authorizations/functions/{functionId}

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
        await client.nvcf.authorizations.functions.delete(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```

        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/nvcf/authorizations/functions/{function_id}",
            cast_to=models.AuthorizedPartiesResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        function_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ListAuthorizedPartiesResponse:
        """
        List Account Authorizations For Function

        Lists NVIDIA Cloud Account IDs that are authorized to invoke any version of the  specified function. The response includes an array showing authorized accounts  for each version. Individual versions of a function can have their own  authorized accounts. So, each object in the array can have different  authorized accounts listed. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header

        GET /v2/nvcf/authorizations/functions/{functionId}

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
        await client.nvcf.authorizations.functions.get(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```

        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/authorizations/functions/{function_id}",
            cast_to=models.ListAuthorizedPartiesResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        authorized_parties: typing.List[params.AuthorizedPartyDto],
        function_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AuthorizedPartiesResponse:
        """
        Authorize Accounts To Invoke Function

        Authorizes additional NVIDIA Cloud Accounts to invoke any version of the  specified function. By default, a function belongs to the NVIDIA Cloud Account  that created it, and the credentials used for function invocation must  reference the same NVIDIA Cloud Account. Upon invocation of this endpoint, any  existing authorized accounts will be overwritten by the newly specified  authorized accounts. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header

        POST /v2/nvcf/authorizations/functions/{functionId}

        Args:
            authorizedParties: Parties authorized to invoke function
            functionId: Function id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.nvcf.authorizations.functions.create(
            authorized_parties=[{"nca_id": "string"}],
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        _json = to_encodable(
            item={"authorized_parties": authorized_parties},
            dump_with=params._SerializerAuthorizedPartiesRequest,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/nvcf/authorizations/functions/{function_id}",
            json=_json,
            cast_to=models.AuthorizedPartiesResponse,
            request_options=request_options or default_request_options(),
        )
