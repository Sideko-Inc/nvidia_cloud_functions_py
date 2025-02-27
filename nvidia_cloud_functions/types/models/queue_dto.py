import typing
import typing_extensions
import pydantic


class QueueDto(pydantic.BaseModel):
    """
    Data Transfer Object(DTO) representing a request queue for function version
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    function_name: str = pydantic.Field(
        alias="functionName",
    )
    """
    Function name
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
    queue_depth: typing.Optional[int] = pydantic.Field(alias="queueDepth", default=None)
    """
    Approximate number of messages in the request queue
    """
