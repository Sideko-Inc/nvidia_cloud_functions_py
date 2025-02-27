import typing_extensions
import pydantic

from .authorized_party_dto import AuthorizedPartyDto, _SerializerAuthorizedPartyDto


class PatchAuthorizedPartyRequest(typing_extensions.TypedDict):
    """
    Request payload to associate/disassociate authorized party with function
    """

    authorized_party: typing_extensions.Required[AuthorizedPartyDto]
    """
    Data Transfer Object(DTO) representing an authorized party.
    """


class _SerializerPatchAuthorizedPartyRequest(pydantic.BaseModel):
    """
    Serializer for PatchAuthorizedPartyRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    authorized_party: _SerializerAuthorizedPartyDto = pydantic.Field(
        alias="authorizedParty",
    )
