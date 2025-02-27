import typing
import pydantic

from .cluster_group import ClusterGroup


class ClusterGroupsResponse(pydantic.BaseModel):
    """
    ClusterGroupsResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cluster_groups: typing.Optional[typing.List[ClusterGroup]] = pydantic.Field(
        alias="clusterGroups", default=None
    )
