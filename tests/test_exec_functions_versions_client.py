import pytest
import pydantic

from nvidia_cloud_functions import AsyncClient, Client
from nvidia_cloud_functions.environment import Environment
from nvidia_cloud_functions.types import models


def test_create_200_success_default():
    """Tests a POST request to the /v2/nvcf/exec/functions/{functionId}/versions/{versionId} endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.InvokeFunctionResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(environment=Environment.MOCK_SERVER)
    response = client.exec.functions.versions.create(
        function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        request_body={},
        version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.InvokeFunctionResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_default():
    """Tests a POST request to the /v2/nvcf/exec/functions/{functionId}/versions/{versionId} endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.InvokeFunctionResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(environment=Environment.MOCK_SERVER)
    response = await client.exec.functions.versions.create(
        function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        request_body={},
        version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.InvokeFunctionResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
