import typing
import pydantic

from .authorized_parties_by_function_dto import AuthorizedPartiesByFunctionDto


class ListAuthorizedPartiesResponse(pydantic.BaseModel):
    """
    Parties authorized to invoke function
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    functions: typing.List[AuthorizedPartiesByFunctionDto] = pydantic.Field(
        alias="functions",
    )
    """
    Functions with authorized parties and other details
    """
