import typing
import typing_extensions
import pydantic

from .request_header_dto import RequestHeaderDto, _SerializerRequestHeaderDto


class InvokeFunctionRequest(typing_extensions.TypedDict):
    """
    Request body for creating a job/task for inference/train using a GPU powered spot instance in cloud.
    """

    request_body: typing_extensions.Required[typing.Dict[str, typing.Any]]

    request_header: typing_extensions.NotRequired[RequestHeaderDto]
    """
    Data Transfer Object(DTO) representing header/address for Cloud Functions processing. 
    """


class _SerializerInvokeFunctionRequest(pydantic.BaseModel):
    """
    Serializer for InvokeFunctionRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    request_body: typing.Dict[str, typing.Any] = pydantic.Field(
        alias="requestBody",
    )
    request_header: typing.Optional[_SerializerRequestHeaderDto] = pydantic.Field(
        alias="requestHeader", default=None
    )
