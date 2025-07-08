import pytest
from utils.api_helper import update
from utils.assertions import assert_status_code, assert_content_type_json, assert_response_time_under, \
    assert_user_update_response
from utils.logs import log_response_details
from utils.payloads import create_update_user_payload, create_user_payload, create_user_payloads


@pytest.mark.skip(reason="Skipping this test for now")
def test_update_user_with_valid_data():

    payload = create_update_user_payload("morpheus updated", "zion resident updated")

    response = update("/users/2", json=payload)

    # Assert response status
    assert_status_code(response, 200)

    log_response_details(response)

    json_data = response.json()

    assert_user_update_response(json_data, "morpheus@@@@", "zion resident@@@@")

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

    payload = create_update_user_payload("morpheus", "zion resident")

    response = update("/users/99999", json=payload)

    # Assert response status
    assert_status_code(response, 404)

    log_response_details(response)

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

@pytest.mark.skip(reason="Skipping this test for now")
def test_update_user_with_special_characters():

    payload = create_update_user_payload("morpheus@@@@", "zion resident@@@@")

    response = update("/users/2", json=payload)

    # Assert response status
    assert_status_code(response, 200)

    log_response_details(response)

    json_data = response.json()

    assert_user_update_response(json_data, "morpheus@@@@", "zion resident@@@@")

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

@pytest.mark.skip(reason="Skipping this test for now")
def test_update_user_extra_keys():

    payload = create_user_payloads("John", "Engineer", age=30, isAdmin=True)


    response = update("/users/2", json=payload)

    # Assert response status
    assert_status_code(response, 404)

    log_response_details(response)

    json_data = response.json()

    assert_user_update_response(json_data, "morpheus@@@@", "zion resident@@@@")

    assert_response_time_under(response, 2)
    assert_content_type_json(response)