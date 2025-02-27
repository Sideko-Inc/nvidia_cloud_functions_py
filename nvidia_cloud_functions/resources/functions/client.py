import typing
import typing_extensions

from nvidia_cloud_functions.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from nvidia_cloud_functions.resources.functions.versions import (
    AsyncVersionsClient,
    VersionsClient,
)
from nvidia_cloud_functions.resources.functions.ids import AsyncIdsClient, IdsClient
from nvidia_cloud_functions.types import models, params


class FunctionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

        self.versions = VersionsClient(base_client=self._base_client)

        self.ids = IdsClient(base_client=self._base_client)

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
    ) -> models.ListFunctionsResponse:
        """
        List Functions

        Lists all the functions associated with the authenticated NVIDIA Cloud Account.  Requires either a bearer token or an api-key with 'list_functions' or  'list_functions_details' scopes in the HTTP Authorization header.

        GET /v2/nvcf/functions

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
        client.functions.list_fn()
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
            path="/v2/nvcf/functions",
            query_params=_query,
            cast_to=models.ListFunctionsResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
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
        models_field: typing.Union[
            typing.Optional[typing.List[params.ArtifactDto]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resources: typing.Union[
            typing.Optional[typing.List[params.ArtifactDto]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateFunctionResponse:
        """
        Create Function

        Creates a new function within the authenticated NVIDIA Cloud Account. Requires a  bearer token with 'register_function' scope in the HTTP Authorization header.

        POST /v2/nvcf/functions

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
        client.functions.create(inference_url="http://www.example.com", name="string")
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
                "models_field": models_field,
                "resources": resources,
                "inference_url": inference_url,
                "name": name,
            },
            dump_with=params._SerializerCreateFunctionRequest,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/nvcf/functions",
            json=_json,
            cast_to=models.CreateFunctionResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncFunctionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

        self.versions = AsyncVersionsClient(base_client=self._base_client)

        self.ids = AsyncIdsClient(base_client=self._base_client)

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
    ) -> models.ListFunctionsResponse:
        """
        List Functions

        Lists all the functions associated with the authenticated NVIDIA Cloud Account.  Requires either a bearer token or an api-key with 'list_functions' or  'list_functions_details' scopes in the HTTP Authorization header.

        GET /v2/nvcf/functions

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
        await client.functions.list_fn()
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
            path="/v2/nvcf/functions",
            query_params=_query,
            cast_to=models.ListFunctionsResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
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
        models_field: typing.Union[
            typing.Optional[typing.List[params.ArtifactDto]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resources: typing.Union[
            typing.Optional[typing.List[params.ArtifactDto]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateFunctionResponse:
        """
        Create Function

        Creates a new function within the authenticated NVIDIA Cloud Account. Requires a  bearer token with 'register_function' scope in the HTTP Authorization header.

        POST /v2/nvcf/functions

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
        await client.functions.create(
            inference_url="http://www.example.com", name="string"
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
                "models_field": models_field,
                "resources": resources,
                "inference_url": inference_url,
                "name": name,
            },
            dump_with=params._SerializerCreateFunctionRequest,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/nvcf/functions",
            json=_json,
            cast_to=models.CreateFunctionResponse,
            request_options=request_options or default_request_options(),
        )
