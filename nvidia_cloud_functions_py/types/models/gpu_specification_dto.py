import typing
import pydantic


class GpuSpecificationDto(pydantic.BaseModel):
    """
    Data Transfer Object(DTO) representing GPU specification.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    availability_zones: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="availabilityZones", default=None
    )
    """
    List of availability-zones(or clusters) in the cluster group
    """
    backend: str = pydantic.Field(
        alias="backend",
    )
    """
    Backend/CSP where the GPU powered instance will be launched
    """
    configuration: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="configuration", default=None
    )
    gpu: str = pydantic.Field(
        alias="gpu",
    )
    """
    GPU name from the cluster
    """
    instance_type: typing.Optional[str] = pydantic.Field(
        alias="instanceType", default=None
    )
    """
    Instance type, based on GPU, assigned to a Worker
    """
    max_instances: int = pydantic.Field(
        alias="maxInstances",
    )
    """
    Maximum number of spot instances for the deployment
    """
    max_request_concurrency: typing.Optional[int] = pydantic.Field(
        alias="maxRequestConcurrency", default=None
    )
    """
    Max request concurrency between 1 (default) and 1024.
    """
    min_instances: int = pydantic.Field(
        alias="minInstances",
    )
    """
    Minimum number of spot instances for the deployment
    """
