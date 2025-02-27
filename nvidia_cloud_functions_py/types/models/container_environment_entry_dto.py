import pydantic


class ContainerEnvironmentEntryDto(pydantic.BaseModel):
    """
    Data Transfer Object(DTO) representing a container environment entry
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    key: str = pydantic.Field(
        alias="key",
    )
    """
    Container environment key
    """
    value: str = pydantic.Field(
        alias="value",
    )
    """
    Container environment value
    """
