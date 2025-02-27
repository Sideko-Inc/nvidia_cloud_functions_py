import typing
import pydantic

from .cluster import Cluster
from .gpu import Gpu


class ClusterGroup(pydantic.BaseModel):
    """
    ClusterGroup
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    authorized_nca_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="authorizedNcaIds", default=None
    )
    clusters: typing.Optional[typing.List[Cluster]] = pydantic.Field(
        alias="clusters", default=None
    )
    gpus: typing.Optional[typing.List[Gpu]] = pydantic.Field(alias="gpus", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    nca_id: typing.Optional[str] = pydantic.Field(alias="ncaId", default=None)
