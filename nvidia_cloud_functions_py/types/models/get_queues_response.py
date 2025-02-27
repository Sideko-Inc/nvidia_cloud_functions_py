import typing
import pydantic

from .queue_dto import QueueDto


class GetQueuesResponse(pydantic.BaseModel):
    """
    Request queue details of all the functions with same id in an account
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
    queues: typing.List[QueueDto] = pydantic.Field(
        alias="queues",
    )
    """
    Details of all the queues associated with same named functions
    """
