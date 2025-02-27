import typing
import typing_extensions
import pydantic

from .authorized_party_dto import AuthorizedPartyDto, _SerializerAuthorizedPartyDto


class AuthorizedPartiesRequest(typing_extensions.TypedDict):
    """
    Request to associated authorized parties for a specific version or allversions of a function
    """

    authorized_parties: typing_extensions.Required[typing.List[AuthorizedPartyDto]]
    """
    Parties authorized to invoke function
    """


class _SerializerAuthorizedPartiesRequest(pydantic.BaseModel):
    """
    Serializer for AuthorizedPartiesRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    authorized_parties: typing.List[_SerializerAuthorizedPartyDto] = pydantic.Field(
        alias="authorizedParties",
    )
