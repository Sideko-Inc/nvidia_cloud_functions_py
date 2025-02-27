import typing_extensions
import pydantic


class ContainerEnvironmentEntryDto(typing_extensions.TypedDict):
    """
    Data Transfer Object(DTO) representing a container environment entry
    """

    key: typing_extensions.Required[str]
    """
    Container environment key
    """

    value: typing_extensions.Required[str]
    """
    Container environment value
    """


class _SerializerContainerEnvironmentEntryDto(pydantic.BaseModel):
    """
    Serializer for ContainerEnvironmentEntryDto handling case conversions
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
