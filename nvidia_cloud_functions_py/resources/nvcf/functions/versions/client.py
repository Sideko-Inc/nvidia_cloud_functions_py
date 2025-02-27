import typing
import typing_extensions

from nvidia_cloud_functions_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from nvidia_cloud_functions_py.types import models, params


class VersionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        function_id: str,
        function_version_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Function

        Deletes the specified function version in the authenticated NVIDIA Cloud  Account. Requires a bearer token with 'delete_function' scope in the HTTP  Authorization header. If the function version is public, then Account Admin  cannot delete the function.

        DELETE /v2/nvcf/functions/{functionId}/versions/{functionVersionId}

        Args:
            functionId: Function id
            functionVersionId: Version id
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.nvcf.functions.versions.delete(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        self._base_client.request(
            method="DELETE",
            path=f"/v2/nvcf/functions/{function_id}/versions/{function_version_id}",
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        function_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ListFunctionsResponse:
        """
        List Function Versions

        Lists details of all the versions of the specified function in the authenticated  NVIDIA Cloud Account. Requires either a bearer token or an api-key with  'list_functions' or 'list_functions_details' scopes in the HTTP Authorization  header.

        GET /v2/nvcf/functions/{functionId}/versions

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
        client.nvcf.functions.versions.list(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```

        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/functions/{function_id}/versions",
            cast_to=models.ListFunctionsResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        function_id: str,
        function_version_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FunctionResponse:
        """
        Get Function Version Details

        Retrieves detailed information of the specified function version in the  authenticated NVIDIA Cloud Account. Requires either a bearer token or an  api-key with 'list_functions' or 'list_functions_details' scopes in the HTTP  Authorization header.

        GET /v2/nvcf/functions/{functionId}/versions/{functionVersionId}

        Args:
            functionId: Function id
            functionVersionId: Version id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.nvcf.functions.versions.get(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/functions/{function_id}/versions/{function_version_id}",
            cast_to=models.FunctionResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        function_id: str,
        inference_url: str,
        name: str,
        api_body_format: typing.Union[
            typing.Optional[typing_extensions.Literal["CUSTOM", "PREDICT_V2"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        container_args: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        container_environment: typing.Union[
            typing.Optional[typing.List[params.ContainerEnvironmentEntryDto]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        container_image: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        health_uri: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        helm_chart: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        helm_chart_service_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        inference_port: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        models: typing.Union[
            typing.Optional[typing.List[params.ArtifactDto]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resources: typing.Union[
            typing.Optional[typing.List[params.ArtifactDto]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateFunctionResponse:
        """
        Create Function Version

        Creates a version of the specified function within the authenticated NVIDIA  Cloud Account. Requires a bearer token with 'register_function' scope in the  HTTP Authorization header.

        POST /v2/nvcf/functions/{functionId}/versions

        Args:
            apiBodyFormat: Invocation request body format
            containerArgs: Args to be passed when launching the container
            containerEnvironment: Environment settings for launching the container
            containerImage: Optional custom container image
            healthUri: Health endpoint for the container or the helmChart
            helmChart: Optional Helm Chart
            helmChartServiceName: Helm Chart Service Name is required when helmChart property is specified
            inferencePort: Optional port number where the inference listener is running. Defaults to 8000  for Triton.
            models: Optional set of models
            resources: Optional set of resources
            functionId: Function id
            inferenceUrl: Entrypoint for invoking the container to process a request
            name: Function name must start with lowercase/uppercase/digit and can only contain lowercase, uppercase, digit, hyphen, and underscore characters
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.nvcf.functions.versions.create(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            inference_url="http://www.example.com",
            name="string",
        )
        ```

        """
        _json = to_encodable(
            item={
                "api_body_format": api_body_format,
                "container_args": container_args,
                "container_environment": container_environment,
                "container_image": container_image,
                "health_uri": health_uri,
                "helm_chart": helm_chart,
                "helm_chart_service_name": helm_chart_service_name,
                "inference_port": inference_port,
                "models": models,
                "resources": resources,
                "inference_url": inference_url,
                "name": name,
            },
            dump_with=params._SerializerCreateFunctionRequest,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/nvcf/functions/{function_id}/versions",
            json=_json,
            cast_to=models.CreateFunctionResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncVersionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        function_id: str,
        function_version_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Function

        Deletes the specified function version in the authenticated NVIDIA Cloud  Account. Requires a bearer token with 'delete_function' scope in the HTTP  Authorization header. If the function version is public, then Account Admin  cannot delete the function.

        DELETE /v2/nvcf/functions/{functionId}/versions/{functionVersionId}

        Args:
            functionId: Function id
            functionVersionId: Version id
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.nvcf.functions.versions.delete(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        await self._base_client.request(
            method="DELETE",
            path=f"/v2/nvcf/functions/{function_id}/versions/{function_version_id}",
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        function_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ListFunctionsResponse:
        """
        List Function Versions

        Lists details of all the versions of the specified function in the authenticated  NVIDIA Cloud Account. Requires either a bearer token or an api-key with  'list_functions' or 'list_functions_details' scopes in the HTTP Authorization  header.

        GET /v2/nvcf/functions/{functionId}/versions

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
        await client.nvcf.functions.versions.list(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```

        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/functions/{function_id}/versions",
            cast_to=models.ListFunctionsResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        function_id: str,
        function_version_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FunctionResponse:
        """
        Get Function Version Details

        Retrieves detailed information of the specified function version in the  authenticated NVIDIA Cloud Account. Requires either a bearer token or an  api-key with 'list_functions' or 'list_functions_details' scopes in the HTTP  Authorization header.

        GET /v2/nvcf/functions/{functionId}/versions/{functionVersionId}

        Args:
            functionId: Function id
            functionVersionId: Version id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.nvcf.functions.versions.get(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/functions/{function_id}/versions/{function_version_id}",
            cast_to=models.FunctionResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        function_id: str,
        inference_url: str,
        name: str,
        api_body_format: typing.Union[
            typing.Optional[typing_extensions.Literal["CUSTOM", "PREDICT_V2"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        container_args: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        container_environment: typing.Union[
            typing.Optional[typing.List[params.ContainerEnvironmentEntryDto]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        container_image: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        health_uri: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        helm_chart: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        helm_chart_service_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        inference_port: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        models: typing.Union[
            typing.Optional[typing.List[params.ArtifactDto]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resources: typing.Union[
            typing.Optional[typing.List[params.ArtifactDto]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateFunctionResponse:
        """
        Create Function Version

        Creates a version of the specified function within the authenticated NVIDIA  Cloud Account. Requires a bearer token with 'register_function' scope in the  HTTP Authorization header.

        POST /v2/nvcf/functions/{functionId}/versions

        Args:
            apiBodyFormat: Invocation request body format
            containerArgs: Args to be passed when launching the container
            containerEnvironment: Environment settings for launching the container
            containerImage: Optional custom container image
            healthUri: Health endpoint for the container or the helmChart
            helmChart: Optional Helm Chart
            helmChartServiceName: Helm Chart Service Name is required when helmChart property is specified
            inferencePort: Optional port number where the inference listener is running. Defaults to 8000  for Triton.
            models: Optional set of models
            resources: Optional set of resources
            functionId: Function id
            inferenceUrl: Entrypoint for invoking the container to process a request
            name: Function name must start with lowercase/uppercase/digit and can only contain lowercase, uppercase, digit, hyphen, and underscore characters
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.nvcf.functions.versions.create(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            inference_url="http://www.example.com",
            name="string",
        )
        ```

        """
        _json = to_encodable(
            item={
                "api_body_format": api_body_format,
                "container_args": container_args,
                "container_environment": container_environment,
                "container_image": container_image,
                "health_uri": health_uri,
                "helm_chart": helm_chart,
                "helm_chart_service_name": helm_chart_service_name,
                "inference_port": inference_port,
                "models": models,
                "resources": resources,
                "inference_url": inference_url,
                "name": name,
            },
            dump_with=params._SerializerCreateFunctionRequest,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/nvcf/functions/{function_id}/versions",
            json=_json,
            cast_to=models.CreateFunctionResponse,
            request_options=request_options or default_request_options(),
        )
