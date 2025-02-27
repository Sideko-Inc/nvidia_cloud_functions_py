import pytest
import pydantic
import typing

from nvidia_cloud_functions_py import AsyncClient, Client
from nvidia_cloud_functions_py.environment import Environment
from nvidia_cloud_functions_py.types import models


def test_create_200_success_default():
    """Tests a POST request to the /v2/nvcf/pexec/functions/{functionId}/versions/{versionId} endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.NvcfPexecFunctionsVersionsCreateResponseObj, typing.List[models.NvcfPexecFunctionsVersionsCreateResponseArrItem]]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(environment=Environment.MOCK_SERVER)
    response = client.nvcf.pexec.functions.versions.create(
        data={},
        function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(
            models.NvcfPexecFunctionsVersionsCreateResponseObj
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    try:
        pydantic.TypeAdapter(
            typing.List[models.NvcfPexecFunctionsVersionsCreateResponseArrItem]
        ).validate_python(response)
        is_stream = True
    except pydantic.ValidationError:
        is_stream = False
    assert any([is_json, is_stream]), "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_default():
    """Tests a POST request to the /v2/nvcf/pexec/functions/{functionId}/versions/{versionId} endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.NvcfPexecFunctionsVersionsCreateResponseObj, typing.List[models.NvcfPexecFunctionsVersionsCreateResponseArrItem]]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(environment=Environment.MOCK_SERVER)
    response = await client.nvcf.pexec.functions.versions.create(
        data={},
        function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(
            models.NvcfPexecFunctionsVersionsCreateResponseObj
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    try:
        pydantic.TypeAdapter(
            typing.List[models.NvcfPexecFunctionsVersionsCreateResponseArrItem]
        ).validate_python(response)
        is_stream = True
    except pydantic.ValidationError:
        is_stream = False
    assert any([is_json, is_stream]), "failed response type check"
