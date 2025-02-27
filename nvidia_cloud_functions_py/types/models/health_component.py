import typing
import pydantic


class HealthComponent(pydantic.BaseModel):
    """
    HealthComponent
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    status: typing.Optional[str] = pydantic.Field(alias="status", default=None)
