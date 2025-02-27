import typing
import typing_extensions
import pydantic

from .instance_dto import InstanceDto
from .container_environment_entry_dto import ContainerEnvironmentEntryDto
from .artifact_dto import ArtifactDto


class FunctionDto(pydantic.BaseModel):
    """
    Data Transfer Object(DTO) representing a function
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active_instances: typing.Optional[typing.List[InstanceDto]] = pydantic.Field(
        alias="activeInstances", default=None
    )
    """
    List of active instances for this function.
    """
    api_body_format: typing.Optional[
        typing_extensions.Literal["CUSTOM", "PREDICT_V2"]
    ] = pydantic.Field(alias="apiBodyFormat", default=None)
    """
    Invocation request body format
    """
    container_args: typing.Optional[str] = pydantic.Field(
        alias="containerArgs", default=None
    )
    """
    Args used to launch the container
    """
    container_environment: typing.Optional[
        typing.List[ContainerEnvironmentEntryDto]
    ] = pydantic.Field(alias="containerEnvironment", default=None)
    """
    Environment settings used to launch the container
    """
    container_image: typing.Optional[str] = pydantic.Field(
        alias="containerImage", default=None
    )
    """
    Optional custom container
    """
    created_at: str = pydantic.Field(
        alias="createdAt",
    )
    """
    Function creation timestamp
    """
    health_uri: str = pydantic.Field(
        alias="healthUri",
    )
    """
    Health endpoint for the container or helmChart
    """
    helm_chart: typing.Optional[str] = pydantic.Field(alias="helmChart", default=None)
    """
    Optional Helm Chart
    """
    helm_chart_service_name: typing.Optional[str] = pydantic.Field(
        alias="helmChartServiceName", default=None
    )
    """
    Helm Chart Service Name specified only when helmChart property is specified 
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique function id
    """
    inference_port: typing.Optional[int] = pydantic.Field(
        alias="inferencePort", default=None
    )
    """
    Optional port number where the inference listener is running - defaults to 8000 for Triton
    """
    inference_url: typing.Optional[str] = pydantic.Field(
        alias="inferenceUrl", default=None
    )
    """
    Entrypoint for invoking the container to process requests
    """
    models: typing.Optional[typing.List[ArtifactDto]] = pydantic.Field(
        alias="models", default=None
    )
    """
    Optional set of models
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    Function name
    """
    nca_id: str = pydantic.Field(
        alias="ncaId",
    )
    """
    NVIDIA Cloud Account Id
    """
    owned_by_different_account: typing.Optional[bool] = pydantic.Field(
        alias="ownedByDifferentAccount", default=None
    )
    """
    Indicates whether the function is owned by another account. If the account  that is being used to lookup functions happens to be authorized to invoke/list  this function which is owned by a different account, then this field is set  to true and ncaId will contain the id of the account that owns the function.  Otherwise, this field is not set as it defaults to false. 
    """
    resources: typing.Optional[typing.List[ArtifactDto]] = pydantic.Field(
        alias="resources", default=None
    )
    """
    Optional set of resources.
    """
    status: typing_extensions.Literal[
        "ACTIVE", "DELETED", "DEPLOYING", "ERROR", "INACTIVE"
    ] = pydantic.Field(
        alias="status",
    )
    """
    Function status
    """
    version_id: str = pydantic.Field(
        alias="versionId",
    )
    """
    Unique function version id
    """
