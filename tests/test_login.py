import pytest

from utils.api_helper import post, logger
from utils.assertions import assert_status_code, assert_content_type_json, assert_response_time_under
from utils.logs import log_response_details


@pytest.mark.skip(reason="Skipping this test for now")
def test_login_successful():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = post("/login", json=payload)

    # Assert response status
    assert_status_code(response, 200)

    log_response_details(response)

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

@pytest.mark.skip(reason="Skipping this test for now")
def test_login_with_invalid_email():
    payload = {
        "email": "invalidtest@gmail.com",
        "password": "cityslicka"
    }

    response = post("/login", json=payload)

    # Assert response status
    assert_status_code(response, 400)

    log_response_details(response)

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

#@pytest.mark.skip(reason="Skipping this test for now")
def test_login_with_missing_password():
    payload = {
    "email": "peter@klaven"
}

    response = post("/login", json=payload)

    # Assert response status
    assert_status_code(response, 400)

    log_response_details(response)

    json_data = response.json()
    assert "error" in json_data
    assert json_data["error"] == "Missing password"

    assert_response_time_under(response, 2)
    assert_content_type_json(response)