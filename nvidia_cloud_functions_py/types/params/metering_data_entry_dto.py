import typing_extensions
import pydantic


class MeteringDataEntryDto(typing_extensions.TypedDict):
    """
    Data Transfer Object(DTO) representing a billing/metering data entry
    """

    key: typing_extensions.Required[str]
    """
    Metering/Billing key
    """

    value: typing_extensions.Required[str]
    """
    Metering/Billing value
    """


class _SerializerMeteringDataEntryDto(pydantic.BaseModel):
    """
    Serializer for MeteringDataEntryDto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    key: str = pydantic.Field(
        alias="key",
    )
    value: str = pydantic.Field(
        alias="value",
    )
