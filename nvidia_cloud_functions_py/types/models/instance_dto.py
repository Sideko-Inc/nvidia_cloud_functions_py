import typing
import typing_extensions
import pydantic


class InstanceDto(pydantic.BaseModel):
    """
    Data Transfer Object(DTO) representing a spot instance
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    backend: typing.Optional[str] = pydantic.Field(alias="backend", default=None)
    """
    Backend where the instance is running
    """
    function_id: typing.Optional[str] = pydantic.Field(alias="functionId", default=None)
    """
    Function executing on the instance
    """
    function_version_id: typing.Optional[str] = pydantic.Field(
        alias="functionVersionId", default=None
    )
    """
    Function version executing on the instance
    """
    gpu: typing.Optional[str] = pydantic.Field(alias="gpu", default=None)
    """
    GPU name powering the instance
    """
    instance_created_at: typing.Optional[str] = pydantic.Field(
        alias="instanceCreatedAt", default=None
    )
    """
    Instance creation timestamp
    """
    instance_id: typing.Optional[str] = pydantic.Field(alias="instanceId", default=None)
    """
    Unique id of the instance
    """
    instance_status: typing.Optional[
        typing_extensions.Literal["ACTIVE", "DELETED", "ERRORED", "PREEMPTED"]
    ] = pydantic.Field(alias="instanceStatus", default=None)
    """
    Instance status
    """
    instance_type: typing.Optional[str] = pydantic.Field(
        alias="instanceType", default=None
    )
    """
    GPU instance-type powering the instance
    """
    instance_updated_at: typing.Optional[str] = pydantic.Field(
        alias="instanceUpdatedAt", default=None
    )
    """
    Instance's last updated timestamp
    """
    location: typing.Optional[str] = pydantic.Field(alias="location", default=None)
    """
    Location such as zone name or region where the instance is running
    """
    nca_id: typing.Optional[str] = pydantic.Field(alias="ncaId", default=None)
    """
    NVIDIA Cloud Account Id that owns the function running on the instance
    """
    sis_request_id: typing.Optional[str] = pydantic.Field(
        alias="sisRequestId", default=None
    )
    """
    SIS request-id used to launch this instance
    """
