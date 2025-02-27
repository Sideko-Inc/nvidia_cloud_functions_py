import typing
import pydantic


class DeploymentHealthDto(pydantic.BaseModel):
    """
    Data Transfer Object(DTO) representing deployment error
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    backend: str = pydantic.Field(
        alias="backend",
    )
    """
    Backend/CSP where the GPU powered instance will be launched
    """
    error: str = pydantic.Field(
        alias="error",
    )
    """
    Deployment error
    """
    gpu: str = pydantic.Field(
        alias="gpu",
    )
    """
    GPU Type as per SDD
    """
    instance_type: typing.Optional[str] = pydantic.Field(
        alias="instanceType", default=None
    )
    """
    Instance type
    """
    sis_request_id: typing.Optional[str] = pydantic.Field(
        alias="sisRequestId", default=None
    )
    """
    SIS Request ID
    """
