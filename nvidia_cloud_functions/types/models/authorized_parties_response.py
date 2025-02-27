import pydantic

from .authorized_parties_by_function_dto import AuthorizedPartiesByFunctionDto


class AuthorizedPartiesResponse(pydantic.BaseModel):
    """
    Parties authorized to invoke function
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    function: AuthorizedPartiesByFunctionDto = pydantic.Field(
        alias="function",
    )
    """
    Data Transfer Object(DTO) representing a function with authorized accounts
    """
