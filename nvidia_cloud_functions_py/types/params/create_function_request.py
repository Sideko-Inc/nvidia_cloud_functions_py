import typing
import typing_extensions
import pydantic

from .container_environment_entry_dto import (
    ContainerEnvironmentEntryDto,
    _SerializerContainerEnvironmentEntryDto,
)
from .artifact_dto import ArtifactDto, _SerializerArtifactDto


class CreateFunctionRequest(typing_extensions.TypedDict):
    """
    Request payload to create function.
    """

    api_body_format: typing_extensions.NotRequired[
        typing_extensions.Literal["CUSTOM", "PREDICT_V2"]
    ]
    """
    Invocation request body format
    """

    container_args: typing_extensions.NotRequired[str]
    """
    Args to be passed when launching the container
    """

    container_environment: typing_extensions.NotRequired[
        typing.List[ContainerEnvironmentEntryDto]
    ]
    """
    Environment settings for launching the container
    """

    container_image: typing_extensions.NotRequired[str]
    """
    Optional custom container image
    """

    health_uri: typing_extensions.NotRequired[str]
    """
    Health endpoint for the container or the helmChart
    """

    helm_chart: typing_extensions.NotRequired[str]
    """
    Optional Helm Chart
    """

    helm_chart_service_name: typing_extensions.NotRequired[str]
    """
    Helm Chart Service Name is required when helmChart property is specified 
    """

    inference_port: typing_extensions.NotRequired[int]
    """
    Optional port number where the inference listener is running. Defaults to 8000  for Triton. 
    """

    inference_url: typing_extensions.Required[str]
    """
    Entrypoint for invoking the container to process a request
    """

    models: typing_extensions.NotRequired[typing.List[ArtifactDto]]
    """
    Optional set of models
    """

    name: typing_extensions.Required[str]
    """
    Function name must start with lowercase/uppercase/digit and can only contain lowercase, uppercase, digit, hyphen, and underscore characters
    """

    resources: typing_extensions.NotRequired[typing.List[ArtifactDto]]
    """
    Optional set of resources
    """


class _SerializerCreateFunctionRequest(pydantic.BaseModel):
    """
    Serializer for CreateFunctionRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    api_body_format: typing.Optional[
        typing_extensions.Literal["CUSTOM", "PREDICT_V2"]
    ] = pydantic.Field(alias="apiBodyFormat", default=None)
    container_args: typing.Optional[str] = pydantic.Field(
        alias="containerArgs", default=None
    )
    container_environment: typing.Optional[
        typing.List[_SerializerContainerEnvironmentEntryDto]
    ] = pydantic.Field(alias="containerEnvironment", default=None)
    container_image: typing.Optional[str] = pydantic.Field(
        alias="containerImage", default=None
    )
    health_uri: typing.Optional[str] = pydantic.Field(alias="healthUri", default=None)
    helm_chart: typing.Optional[str] = pydantic.Field(alias="helmChart", default=None)
    helm_chart_service_name: typing.Optional[str] = pydantic.Field(
        alias="helmChartServiceName", default=None
    )
    inference_port: typing.Optional[int] = pydantic.Field(
        alias="inferencePort", default=None
    )
    inference_url: str = pydantic.Field(
        alias="inferenceUrl",
    )
    models: typing.Optional[typing.List[_SerializerArtifactDto]] = pydantic.Field(
        alias="models", default=None
    )
    name: str = pydantic.Field(
        alias="name",
    )
    resources: typing.Optional[typing.List[_SerializerArtifactDto]] = pydantic.Field(
        alias="resources", default=None
    )
