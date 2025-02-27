import typing
import typing_extensions
import pydantic

from .gpu_specification_dto import GpuSpecificationDto
from .deployment_health_dto import DeploymentHealthDto


class FunctionDeploymentDto(pydantic.BaseModel):
    """
    Function deployment response
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    deployment_specifications: typing.List[GpuSpecificationDto] = pydantic.Field(
        alias="deploymentSpecifications",
    )
    """
    Function deployment details
    """
    function_id: str = pydantic.Field(
        alias="functionId",
    )
    """
    Function id
    """
    function_status: typing_extensions.Literal[
        "ACTIVE", "DELETED", "DEPLOYING", "ERROR", "INACTIVE"
    ] = pydantic.Field(
        alias="functionStatus",
    )
    """
    Function status
    """
    function_version_id: str = pydantic.Field(
        alias="functionVersionId",
    )
    """
    Function version id
    """
    health_info: typing.Optional[typing.List[DeploymentHealthDto]] = pydantic.Field(
        alias="healthInfo", default=None
    )
    """
    Health info for a deployment specification is included only if there are any  issues/errors. 
    """
    nca_id: str = pydantic.Field(
        alias="ncaId",
    )
    """
    NVIDIA Cloud Account Id
    """
    request_queue_url: str = pydantic.Field(
        alias="requestQueueUrl",
    )
    """
    SQS Request Queue URL
    """
