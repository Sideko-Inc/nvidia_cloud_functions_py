import pydantic


class ArtifactDto(pydantic.BaseModel):
    """
    Data Transfer Object(DTO) representing an artifact
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: str = pydantic.Field(
        alias="name",
    )
    """
    Artifact name
    """
    uri: str = pydantic.Field(
        alias="uri",
    )
    """
    Artifact URI
    """
    version: str = pydantic.Field(
        alias="version",
    )
    """
    Artifact version
    """
