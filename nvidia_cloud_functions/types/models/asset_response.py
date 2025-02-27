import typing
import pydantic

from .asset_dto import AssetDto


class AssetResponse(pydantic.BaseModel):
    """
    AssetResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    asset: typing.Optional[AssetDto] = pydantic.Field(alias="asset", default=None)
    """
    Data Transfer Object(DTO) representing an asset
    """
