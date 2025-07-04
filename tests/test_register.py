import pytest

from utils.api_helper import post, logger
from utils.assertions import assert_status_code


@pytest.mark.skip(reason="Skipping this test for now")
def test_register_with_valid_email_password():
    payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

    response = post("/register", json=payload)

    # Assert response status
    assert_status_code(response, 200)

    logger.info(f"URL: {response.request.url}")
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {response.text}")

    json_data = response.json()
    assert "token" in json_data, "Token not found in response"

@pytest.mark.skip(reason="Skipping this test for now")
def test_register_with_existing_user():
    payload = {
        "email": "",
        "password": "pistol"
    }

    response = post("/register", json=payload)

    # Assert response status
    assert_status_code(response, 400)

    logger.info(f"URL: {response.request.url}")
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {response.text}")

    json_data = response.json()
    assert "error" in json_data, "error not found in response"