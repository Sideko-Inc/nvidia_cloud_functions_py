import typing
import typing_extensions
import pydantic

from .metering_data_entry_dto import (
    MeteringDataEntryDto,
    _SerializerMeteringDataEntryDto,
)


class RequestHeaderDto(typing_extensions.TypedDict):
    """
    Data Transfer Object(DTO) representing header/address for Cloud Functions processing.
    """

    input_asset_references: typing_extensions.NotRequired[typing.List[str]]
    """
    List of UUIDs corresponding to the uploaded assets to be used as input for executing the task.
    """

    metering_data: typing_extensions.NotRequired[typing.List[MeteringDataEntryDto]]
    """
    Metadata used for billing/metering purposes.
    """

    poll_duration_seconds: typing_extensions.NotRequired[int]
    """
    Polling timeout duration.
    """


class _SerializerRequestHeaderDto(pydantic.BaseModel):
    """
    Serializer for RequestHeaderDto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    input_asset_references: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="inputAssetReferences", default=None
    )
    metering_data: typing.Optional[typing.List[_SerializerMeteringDataEntryDto]] = (
        pydantic.Field(alias="meteringData", default=None)
    )
    poll_duration_seconds: typing.Optional[int] = pydantic.Field(
        alias="pollDurationSeconds", default=None
    )
