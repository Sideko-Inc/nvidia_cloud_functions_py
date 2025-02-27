import typing
import pydantic

from .authorized_party_dto import AuthorizedPartyDto


class AuthorizedPartiesByFunctionDto(pydantic.BaseModel):
    """
    Data Transfer Object(DTO) representing a function with authorized accounts
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    authorized_parties: typing.Optional[typing.List[AuthorizedPartyDto]] = (
        pydantic.Field(alias="authorizedParties", default=None)
    )
    """
    Authorized parties allowed to invoke the function
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Function id
    """
    nca_id: str = pydantic.Field(
        alias="ncaId",
    )
    """
    NVIDIA Cloud Account Id
    """
    version_id: typing.Optional[str] = pydantic.Field(alias="versionId", default=None)
    """
    Function version id
    """
