import typing
import pydantic


class CreateAssetResponse(pydantic.BaseModel):
    """
    Response body containing asset-id and the corresponding pre-signed URL to upload an asset of specified content-type to AWS S3 bucket.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    asset_id: typing.Optional[str] = pydantic.Field(alias="assetId", default=None)
    """
    Unique id of the asset to be uploaded to AWS S3 bucket
    """
    content_type: typing.Optional[str] = pydantic.Field(
        alias="contentType", default=None
    )
    """
    Content type of the asset such image/png, image/jpeg, etc.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    Asset description to be used when uploading the asset
    """
    upload_url: typing.Optional[str] = pydantic.Field(alias="uploadUrl", default=None)
    """
    Pre-signed upload URL to upload asset
    """
