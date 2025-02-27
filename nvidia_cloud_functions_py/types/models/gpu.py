import typing
import pydantic

from .instance_type import InstanceType


class Gpu(pydantic.BaseModel):
    """
    Gpu
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    instance_types: typing.Optional[typing.List[InstanceType]] = pydantic.Field(
        alias="instanceTypes", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
