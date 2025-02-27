import typing
import pydantic


class Cluster(pydantic.BaseModel):
    """
    Cluster
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    k8s_version: typing.Optional[str] = pydantic.Field(alias="k8sVersion", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
