import typing
import pydantic


class AssetDto(pydantic.BaseModel):
    """
    Data Transfer Object(DTO) representing an asset
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    asset_id: typing.Optional[str] = pydantic.Field(alias="assetId", default=None)
    """
    Asset id
    """
    content_type: typing.Optional[str] = pydantic.Field(
        alias="contentType", default=None
    )
    """
    Content-type specified when creating the asset
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    Description specified when creating the asset
    """
