import pydantic

from .function_dto import FunctionDto


class CreateFunctionResponse(pydantic.BaseModel):
    """
    Response body for create function request.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    function: FunctionDto = pydantic.Field(
        alias="function",
    )
    """
    Data Transfer Object(DTO) representing a function
    """
