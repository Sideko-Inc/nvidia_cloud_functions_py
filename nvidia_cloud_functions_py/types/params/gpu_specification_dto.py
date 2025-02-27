import typing
import typing_extensions
import pydantic


class GpuSpecificationDto(typing_extensions.TypedDict):
    """
    Data Transfer Object(DTO) representing GPU specification.
    """

    availability_zones: typing_extensions.NotRequired[typing.List[str]]
    """
    List of availability-zones(or clusters) in the cluster group
    """

    backend: typing_extensions.Required[str]
    """
    Backend/CSP where the GPU powered instance will be launched
    """

    configuration: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    gpu: typing_extensions.Required[str]
    """
    GPU name from the cluster
    """

    instance_type: typing_extensions.NotRequired[str]
    """
    Instance type, based on GPU, assigned to a Worker
    """

    max_instances: typing_extensions.Required[int]
    """
    Maximum number of spot instances for the deployment
    """

    max_request_concurrency: typing_extensions.NotRequired[int]
    """
    Max request concurrency between 1 (default) and 1024.
    """

    min_instances: typing_extensions.Required[int]
    """
    Minimum number of spot instances for the deployment
    """


class _SerializerGpuSpecificationDto(pydantic.BaseModel):
    """
    Serializer for GpuSpecificationDto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    availability_zones: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="availabilityZones", default=None
    )
    backend: str = pydantic.Field(
        alias="backend",
    )
    configuration: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="configuration", default=None
    )
    gpu: str = pydantic.Field(
        alias="gpu",
    )
    instance_type: typing.Optional[str] = pydantic.Field(
        alias="instanceType", default=None
    )
    max_instances: int = pydantic.Field(
        alias="maxInstances",
    )
    max_request_concurrency: typing.Optional[int] = pydantic.Field(
        alias="maxRequestConcurrency", default=None
    )
    min_instances: int = pydantic.Field(
        alias="minInstances",
    )
