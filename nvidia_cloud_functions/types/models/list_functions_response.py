import typing
import pydantic

from .function_dto import FunctionDto


class ListFunctionsResponse(pydantic.BaseModel):
    """
    Response body containing list of functions
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    functions: typing.List[FunctionDto] = pydantic.Field(
        alias="functions",
    )
    """
    List of functions
    """
