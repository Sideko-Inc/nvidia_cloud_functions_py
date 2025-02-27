import typing_extensions
import pydantic


class CreateAssetRequest(typing_extensions.TypedDict):
    """
    Request payload to create an asset-id and the corresponding pre-signed URL to upload an asset of specified content-type to AWS S3 bucket.
    """

    content_type: typing_extensions.Required[str]
    """
    Content type of the asset such image/png, image/jpeg, etc.
    """

    description: typing_extensions.Required[str]
    """
    Asset description
    """


class _SerializerCreateAssetRequest(pydantic.BaseModel):
    """
    Serializer for CreateAssetRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    content_type: str = pydantic.Field(
        alias="contentType",
    )
    description: str = pydantic.Field(
        alias="description",
    )
