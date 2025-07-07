import pytest
from utils.api_helper import post, logger
from utils.assertions import assert_status_code, assert_content_type_json, assert_response_time_under
from utils.logs import log_response_details


@pytest.mark.skip(reason="Skipping this test for now")
def test_register_with_valid_email_password():
    payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

    response = post("/register", json=payload)

    # Assert response status
    assert_status_code(response, 200)

    log_response_details(response)

    json_data = response.json()
    assert "token" in json_data, "Token not found in response"

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

@pytest.mark.skip(reason="Skipping this test for now")
def test_register_with_existing_user():
    payload = {
        "email": "",
        "password": "pistol"
    }

    response = post("/register", json=payload)

    # Assert response status
    assert_status_code(response, 400)

    log_response_details(response)

    json_data = response.json()
    assert "error" in json_data, "error not found in response"

    assert_response_time_under(response, 2)
    assert_content_type_json(response)