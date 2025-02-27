import pytest
import pydantic

from nvidia_cloud_functions_py import AsyncClient, Client
from nvidia_cloud_functions_py.environment import Environment
from nvidia_cloud_functions_py.types import models


def test_patch_200_success_default():
    """Tests a PATCH request to the /v2/nvcf/authorizations/functions/{functionId}/add endpoint.

    Operation: patch
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.AuthorizedPartiesResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(environment=Environment.MOCK_SERVER)
    response = client.nvcf.authorizations.functions.add.patch(
        authorized_party={"nca_id": "string"},
        function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.AuthorizedPartiesResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_default():
    """Tests a PATCH request to the /v2/nvcf/authorizations/functions/{functionId}/add endpoint.

    Operation: patch
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.AuthorizedPartiesResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(environment=Environment.MOCK_SERVER)
    response = await client.nvcf.authorizations.functions.add.patch(
        authorized_party={"nca_id": "string"},
        function_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.AuthorizedPartiesResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
