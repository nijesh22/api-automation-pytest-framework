import pytest

from utils.api_helper import post, logger
from utils.assertions import assert_status_code

@pytest.mark.skip(reason="Skipping this test for now")
def test_login_successful():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = post("/login", json=payload)

    # Assert response status
    assert_status_code(response, 200)

    logger.info(f"URL: {response.request.url}")
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {response.text}")

@pytest.mark.skip(reason="Skipping this test for now")
def test_login_with_invalid_email():
    payload = {
        "email": "invalidtest@gmail.com",
        "password": "cityslicka"
    }

    response = post("/login", json=payload)

    # Assert response status
    assert_status_code(response, 400)

    logger.info(f"URL: {response.request.url}")
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {response.text}")

@pytest.mark.skip(reason="Skipping this test for now")
def test_login_with_missing_password():
    payload = {
    "email": "peter@klaven"
}

    response = post("/login", json=payload)

    # Assert response status
    assert_status_code(response, 400)

    logger.info(f"URL: {response.request.url}")
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {response.text}")

    json_data = response.json()
    assert "error" in json_data
    assert json_data["error"] == "Missing password"