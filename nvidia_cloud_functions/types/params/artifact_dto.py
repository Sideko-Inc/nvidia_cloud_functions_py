import typing_extensions
import pydantic


class ArtifactDto(typing_extensions.TypedDict):
    """
    Data Transfer Object(DTO) representing an artifact
    """

    name: typing_extensions.Required[str]
    """
    Artifact name
    """

    uri: typing_extensions.Required[str]
    """
    Artifact URI
    """

    version: typing_extensions.Required[str]
    """
    Artifact version
    """


class _SerializerArtifactDto(pydantic.BaseModel):
    """
    Serializer for ArtifactDto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: str = pydantic.Field(
        alias="name",
    )
    uri: str = pydantic.Field(
        alias="uri",
    )
    version: str = pydantic.Field(
        alias="version",
    )
