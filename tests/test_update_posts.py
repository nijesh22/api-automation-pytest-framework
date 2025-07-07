import pytest

from utils.api_helper import update_jph, logger
from utils.assertions import assert_status_code, assert_content_type_json, assert_response_time_under
from utils.logs import log_response_details


@pytest.mark.skip(reason="Skipping this test for now")
def test_update_post_by_id():
    payload = {

  "title": "updated title",
  "body": "updated body"
}

    response = update_jph("/posts/1", json=payload)

    # Assert response status
    assert_status_code(response, 200)

    log_response_details(response)

    json_data = response.json()
    assert json_data["title"] == "updated title"
    assert json_data["body"] == "updated body"
    assert "id" in json_data

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

@pytest.mark.skip(reason="Skipping this test for now")
def test_update_post_with_invalid_id():
    payload = {
  "title": "title updated",
  "body": "quia et recusandae consequuntur expedita et cum"
}

    response = update_jph("/posts/1111", json=payload)

    # Assert response status
    assert_status_code(response, 200)

    log_response_details(response)

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

@pytest.mark.skip(reason="Skipping this test for now")
def test_update_post_empty_payload():
    payload = {}

    response = update_jph("/posts/1", json=payload)

    # Assert response status
    assert_status_code(response, 200)

    log_response_details(response)

    json_data = response.json()
    assert "id" in json_data
    assert len(json_data) == 1

    assert_response_time_under(response, 2)
    assert_content_type_json(response)


@pytest.mark.skip(reason="Skipping this test for now")
def test_update_post_invalid_field_type():
    payload = {
        "title": True, # invalid field type
        "body": "quia et recusandae consequuntur expedita et cum"
    }

    response = update_jph("/posts/1", json=payload)

    # Assert response status
    assert_status_code(response, 422)

    log_response_details(response)

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

