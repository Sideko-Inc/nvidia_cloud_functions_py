import typing
import pydantic


class InstanceType(pydantic.BaseModel):
    """
    InstanceType
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    default: typing.Optional[bool] = pydantic.Field(alias="default", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
