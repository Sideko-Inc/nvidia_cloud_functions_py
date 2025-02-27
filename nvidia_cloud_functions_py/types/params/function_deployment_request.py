import typing
import typing_extensions
import pydantic

from .gpu_specification_dto import GpuSpecificationDto, _SerializerGpuSpecificationDto


class FunctionDeploymentRequest(typing_extensions.TypedDict):
    """
    Request to deploy a function
    """

    deployment_specifications: typing_extensions.Required[
        typing.List[GpuSpecificationDto]
    ]
    """
    Deployment specs with Backend, GPU, instance-type, etc. details
    """


class _SerializerFunctionDeploymentRequest(pydantic.BaseModel):
    """
    Serializer for FunctionDeploymentRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    deployment_specifications: typing.List[_SerializerGpuSpecificationDto] = (
        pydantic.Field(
            alias="deploymentSpecifications",
        )
    )
