import typing
import pydantic


class ListFunctionIdsResponse(pydantic.BaseModel):
    """
    Response body containing list of function ids in an account
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    function_ids: typing.List[str] = pydantic.Field(
        alias="functionIds",
    )
    """
    List of function ids
    """
