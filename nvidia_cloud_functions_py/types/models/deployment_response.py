import pydantic

from .function_deployment_dto import FunctionDeploymentDto


class DeploymentResponse(pydantic.BaseModel):
    """
    Function Deployment Response
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    deployment: FunctionDeploymentDto = pydantic.Field(
        alias="deployment",
    )
    """
    Function deployment response
    """
