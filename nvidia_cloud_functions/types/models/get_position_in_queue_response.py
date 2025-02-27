import typing
import pydantic


class GetPositionInQueueResponse(pydantic.BaseModel):
    """
    Request position in queue for invocation request
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    function_id: str = pydantic.Field(
        alias="functionId",
    )
    """
    Function id
    """
    function_version_id: str = pydantic.Field(
        alias="functionVersionId",
    )
    """
    Function version id
    """
    position_in_queue: typing.Optional[int] = pydantic.Field(
        alias="positionInQueue", default=None
    )
    """
    Position of request in queue
    """
