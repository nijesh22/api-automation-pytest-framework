import pytest
from utils.api_helper import post, logger, update
from utils.assertions import assert_status_code, assert_content_type_json, assert_response_time_under
from utils.logs import log_response_details


@pytest.mark.skip(reason="Skipping this test for now")
def test_update_user_with_valid_data():
    payload = {
    "name": "morpheus updated",
    "job": "zion resident updated"
}

    response = update("/users/2", json=payload)

    # Assert response status
    assert_status_code(response, 200)

    log_response_details(response)

    json_data = response.json()
    assert json_data["name"] == "morpheus updated"
    assert json_data["job"] == "zion resident updated"
    assert "updatedAt" in json_data

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

@pytest.mark.skip(reason="Skipping this test for now")
def test_update_user_with_empty_body():
    payload = {}

    response = update("/users/2", json=payload)

    # Assert response status
    assert_status_code(response, 200)

    log_response_details(response)

    json_data = response.json()
    assert "updatedAt" in json_data
    assert len(json_data) == 1

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

@pytest.mark.skip(reason="Skipping this test for now")
def test_update_user_with_invalid_id():
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = update("/users/99999", json=payload)

    # Assert response status
    assert_status_code(response, 404)

    log_response_details(response)

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

@pytest.mark.skip(reason="Skipping this test for now")
def test_update_user_with_special_characters():
    payload = {
        "name": "morpheus@@@@",
        "job": "zion resident@@@@"
    }

    response = update("/users/2", json=payload)

    # Assert response status
    assert_status_code(response, 200)

    log_response_details(response)

    json_data = response.json()
    assert json_data["name"] == "morpheus@@@@"
    assert json_data["job"] == "zion resident@@@@"
    assert "updatedAt" in json_data

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

@pytest.mark.skip(reason="Skipping this test for now")
def test_update_user_extra_keys():
    payload = {
        "name": "John",
        "job": "Engineer",
        "age": 30,
        "isAdmin": True
    }

    response = update("/users/2", json=payload)

    # Assert response status
    assert_status_code(response, 404)

    log_response_details(response)

    json_data = response.json()
    assert json_data["name"] == "morpheus@@@@"
    assert json_data["job"] == "zion resident@@@@"
    assert "updatedAt" in json_data

    assert_response_time_under(response, 2)
    assert_content_type_json(response)