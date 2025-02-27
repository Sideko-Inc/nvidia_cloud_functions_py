import pytest
import pydantic

from nvidia_cloud_functions_py import AsyncClient, Client
from nvidia_cloud_functions_py.environment import Environment
from nvidia_cloud_functions_py.types import models


def test_create_200_success_default():
    """Tests a POST request to the /v2/nvcf/functions endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CreateFunctionResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(environment=Environment.MOCK_SERVER)
    response = client.nvcf.functions.create(
        inference_url="http://www.example.com", name="string"
    )
    try:
        pydantic.TypeAdapter(models.CreateFunctionResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_default():
    """Tests a POST request to the /v2/nvcf/functions endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CreateFunctionResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(environment=Environment.MOCK_SERVER)
    response = await client.nvcf.functions.create(
        inference_url="http://www.example.com", name="string"
    )
    try:
        pydantic.TypeAdapter(models.CreateFunctionResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v2/nvcf/functions endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ListFunctionsResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(environment=Environment.MOCK_SERVER)
    response = client.nvcf.functions.list()
    try:
        pydantic.TypeAdapter(models.ListFunctionsResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v2/nvcf/functions endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ListFunctionsResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(environment=Environment.MOCK_SERVER)
    response = await client.nvcf.functions.list()
    try:
        pydantic.TypeAdapter(models.ListFunctionsResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
