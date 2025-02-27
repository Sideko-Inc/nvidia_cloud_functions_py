import typing
import pydantic


class NvcfPexecFunctionsVersionsCreateResponseArrItem(pydantic.BaseModel):
    """
    NvcfPexecFunctionsVersionsCreateResponseArrItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    char: typing.Optional[str] = pydantic.Field(alias="char", default=None)
    direct: typing.Optional[bool] = pydantic.Field(alias="direct", default=None)
    double: typing.Optional[float] = pydantic.Field(alias="double", default=None)
    float: typing.Optional[float] = pydantic.Field(alias="float", default=None)
    int: typing.Optional[int] = pydantic.Field(alias="int", default=None)
    long: typing.Optional[int] = pydantic.Field(alias="long", default=None)
    read_only: typing.Optional[bool] = pydantic.Field(alias="readOnly", default=None)
    short: typing.Optional[int] = pydantic.Field(alias="short", default=None)
