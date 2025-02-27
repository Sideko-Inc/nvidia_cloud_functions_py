import typing
import typing_extensions
import pydantic


class AuthorizedPartyDto(typing_extensions.TypedDict):
    """
    Data Transfer Object(DTO) representing an authorized party.
    """

    client_id: typing_extensions.NotRequired[str]
    """
    Client Id -- 'sub' claim in the JWT. This field should not be  specified anymore.
    """

    nca_id: typing_extensions.Required[str]
    """
    NVIDIA Cloud Account authorized to invoke the function
    """


class _SerializerAuthorizedPartyDto(pydantic.BaseModel):
    """
    Serializer for AuthorizedPartyDto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    client_id: typing.Optional[str] = pydantic.Field(alias="clientId", default=None)
    nca_id: str = pydantic.Field(
        alias="ncaId",
    )
