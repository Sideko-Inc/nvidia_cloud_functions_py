import typing
import pydantic


class AuthorizedPartyDto(pydantic.BaseModel):
    """
    Data Transfer Object(DTO) representing an authorized party.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    client_id: typing.Optional[str] = pydantic.Field(alias="clientId", default=None)
    """
    Client Id -- 'sub' claim in the JWT. This field should not be  specified anymore.
    """
    nca_id: str = pydantic.Field(
        alias="ncaId",
    )
    """
    NVIDIA Cloud Account authorized to invoke the function
    """
