import typing
import typing_extensions
import pydantic


class InvokeFunctionResponse(pydantic.BaseModel):
    """
    Response body with result from a request for executing a job/task as a cloud function using a GPU powered spot/on-demand instance.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    error_code: typing.Optional[int] = pydantic.Field(alias="errorCode", default=None)
    """
    Error code from the container while executing cloud function.
    """
    percent_complete: typing.Optional[int] = pydantic.Field(
        alias="percentComplete", default=None
    )
    """
    Progress indicator for the task/job executing cloud function.
    """
    req_id: typing.Optional[str] = pydantic.Field(alias="reqId", default=None)
    """
    Request id
    """
    response: typing.Optional[str] = pydantic.Field(alias="response", default=None)
    """
    Response/result of size < 5MB size for the task/job executing cloud function.
    """
    response_reference: typing.Optional[str] = pydantic.Field(
        alias="responseReference", default=None
    )
    """
    For large results, responseReference will be a pre-signeddownload URL.
    """
    status: typing.Optional[
        typing_extensions.Literal[
            "errored", "fulfilled", "in-progress", "pending-evaluation", "rejected"
        ]
    ] = pydantic.Field(alias="status", default=None)
    """
    Status of the task/job executing cloud function.
    """
