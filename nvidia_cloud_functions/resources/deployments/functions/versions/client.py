import typing

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
from nvidia_cloud_functions.types import models, params


class VersionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        function_id: str,
        function_version_id: str,
        graceful: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FunctionResponse:
        """
        Delete Function Deployment

        Deletes the deployment associated with the specified function. Upon  deletion, any active instances will be terminated, and the function's status  will transition to 'INACTIVE'. To undeploy a function version gracefully,  specify 'graceful=true' query parameter, allowing current tasks to complete  before terminating the instances. If the specified function version is public,  then Account Admin cannot perform this operation. Access to this endpoint mandates a bearer token with 'deploy_function' scope in the  HTTP Authorization header.

        DELETE /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}

        Args:
            graceful: Query param to deactivate function for graceful shutdown
            functionId: Function id
            functionVersionId: Function version id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.deployments.functions.versions.delete(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        _query: QueryParams = {}
        if not isinstance(graceful, type_utils.NotGiven):
            encode_query_param(
                _query,
                "graceful",
                to_encodable(item=graceful, dump_with=bool),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/nvcf/deployments/functions/{function_id}/versions/{function_version_id}",
            query_params=_query,
            cast_to=models.FunctionResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        function_id: str,
        function_version_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeploymentResponse:
        """
        Get Function Deployment Details

        Allows Account Admins to retrieve the deployment details of the specified  function version. Access to this endpoint mandates a bearer token with 'deploy_function' scope in the  HTTP Authorization header.

        GET /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}

        Args:
            functionId: Function id
            functionVersionId: Function version id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.deployments.functions.versions.get(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/deployments/functions/{function_id}/versions/{function_version_id}",
            cast_to=models.DeploymentResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        deployment_specifications: typing.List[params.GpuSpecificationDto],
        function_id: str,
        function_version_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeploymentResponse:
        """
        Deploy Function

        Initiates deployment for the specified function version. Upon invocation of  this endpoint, the function's status transitions to 'DEPLOYING'. If the  specified function version is public, then Account Admin cannot perform this  operation. Access to this endpoint mandates a bearer token with 'deploy_function' scope in the  HTTP Authorization header.

        POST /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}

        Args:
            deploymentSpecifications: Deployment specs with Backend, GPU, instance-type, etc. details
            functionId: Function id
            functionVersionId: Function version id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.deployments.functions.versions.create(
            deployment_specifications=[
                {
                    "backend": "string",
                    "gpu": "string",
                    "max_instances": 123,
                    "min_instances": 123,
                }
            ],
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        _json = to_encodable(
            item={"deployment_specifications": deployment_specifications},
            dump_with=params._SerializerFunctionDeploymentRequest,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/nvcf/deployments/functions/{function_id}/versions/{function_version_id}",
            json=_json,
            cast_to=models.DeploymentResponse,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        deployment_specifications: typing.List[params.GpuSpecificationDto],
        function_id: str,
        function_version_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeploymentResponse:
        """
        Update Function Deployment

        Updates the deployment specs of the specified function version. It's important  to note that GPU type and backend configurations cannot be modified through  this endpoint. If the specified function is public, then Account Admin cannot  perform this operation. Access to this endpoint mandates a bearer token with 'deploy_function' scope in the  HTTP Authorization header.

        PUT /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}

        Args:
            deploymentSpecifications: Deployment specs with Backend, GPU, instance-type, etc. details
            functionId: Function id
            functionVersionId: Function version id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.deployments.functions.versions.update(
            deployment_specifications=[
                {
                    "backend": "string",
                    "gpu": "string",
                    "max_instances": 123,
                    "min_instances": 123,
                }
            ],
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        _json = to_encodable(
            item={"deployment_specifications": deployment_specifications},
            dump_with=params._SerializerFunctionDeploymentRequest,
        )
        return self._base_client.request(
            method="PUT",
            path=f"/v2/nvcf/deployments/functions/{function_id}/versions/{function_version_id}",
            json=_json,
            cast_to=models.DeploymentResponse,
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
        graceful: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FunctionResponse:
        """
        Delete Function Deployment

        Deletes the deployment associated with the specified function. Upon  deletion, any active instances will be terminated, and the function's status  will transition to 'INACTIVE'. To undeploy a function version gracefully,  specify 'graceful=true' query parameter, allowing current tasks to complete  before terminating the instances. If the specified function version is public,  then Account Admin cannot perform this operation. Access to this endpoint mandates a bearer token with 'deploy_function' scope in the  HTTP Authorization header.

        DELETE /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}

        Args:
            graceful: Query param to deactivate function for graceful shutdown
            functionId: Function id
            functionVersionId: Function version id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.deployments.functions.versions.delete(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        _query: QueryParams = {}
        if not isinstance(graceful, type_utils.NotGiven):
            encode_query_param(
                _query,
                "graceful",
                to_encodable(item=graceful, dump_with=bool),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/nvcf/deployments/functions/{function_id}/versions/{function_version_id}",
            query_params=_query,
            cast_to=models.FunctionResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        function_id: str,
        function_version_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeploymentResponse:
        """
        Get Function Deployment Details

        Allows Account Admins to retrieve the deployment details of the specified  function version. Access to this endpoint mandates a bearer token with 'deploy_function' scope in the  HTTP Authorization header.

        GET /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}

        Args:
            functionId: Function id
            functionVersionId: Function version id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.deployments.functions.versions.get(
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/nvcf/deployments/functions/{function_id}/versions/{function_version_id}",
            cast_to=models.DeploymentResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        deployment_specifications: typing.List[params.GpuSpecificationDto],
        function_id: str,
        function_version_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeploymentResponse:
        """
        Deploy Function

        Initiates deployment for the specified function version. Upon invocation of  this endpoint, the function's status transitions to 'DEPLOYING'. If the  specified function version is public, then Account Admin cannot perform this  operation. Access to this endpoint mandates a bearer token with 'deploy_function' scope in the  HTTP Authorization header.

        POST /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}

        Args:
            deploymentSpecifications: Deployment specs with Backend, GPU, instance-type, etc. details
            functionId: Function id
            functionVersionId: Function version id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.deployments.functions.versions.create(
            deployment_specifications=[
                {
                    "backend": "string",
                    "gpu": "string",
                    "max_instances": 123,
                    "min_instances": 123,
                }
            ],
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        _json = to_encodable(
            item={"deployment_specifications": deployment_specifications},
            dump_with=params._SerializerFunctionDeploymentRequest,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/nvcf/deployments/functions/{function_id}/versions/{function_version_id}",
            json=_json,
            cast_to=models.DeploymentResponse,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        deployment_specifications: typing.List[params.GpuSpecificationDto],
        function_id: str,
        function_version_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeploymentResponse:
        """
        Update Function Deployment

        Updates the deployment specs of the specified function version. It's important  to note that GPU type and backend configurations cannot be modified through  this endpoint. If the specified function is public, then Account Admin cannot  perform this operation. Access to this endpoint mandates a bearer token with 'deploy_function' scope in the  HTTP Authorization header.

        PUT /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}

        Args:
            deploymentSpecifications: Deployment specs with Backend, GPU, instance-type, etc. details
            functionId: Function id
            functionVersionId: Function version id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.deployments.functions.versions.update(
            deployment_specifications=[
                {
                    "backend": "string",
                    "gpu": "string",
                    "max_instances": 123,
                    "min_instances": 123,
                }
            ],
            function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            function_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```

        """
        _json = to_encodable(
            item={"deployment_specifications": deployment_specifications},
            dump_with=params._SerializerFunctionDeploymentRequest,
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/v2/nvcf/deployments/functions/{function_id}/versions/{function_version_id}",
            json=_json,
            cast_to=models.DeploymentResponse,
            request_options=request_options or default_request_options(),
        )
