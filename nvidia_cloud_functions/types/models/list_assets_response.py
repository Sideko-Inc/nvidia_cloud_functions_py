import typing
import pydantic

from .asset_dto import AssetDto


class ListAssetsResponse(pydantic.BaseModel):
    """
    Response body containing list of assets of the current nca id
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    assets: typing.Optional[typing.List[AssetDto]] = pydantic.Field(
        alias="assets", default=None
    )
    """
    List of assets uploaded for the nca id
    """
