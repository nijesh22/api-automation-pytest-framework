import pytest
from utils.api_helper import post, logger
from utils.assertions import assert_status_code, assert_content_type_json, \
    assert_response_time_under, assert_post_creation_response
from utils.logs import log_response_details
from utils.payloads import create_post_payload


@pytest.mark.skip(reason="Skipping this test for now")
def test_create_post_with_title_and_body():

    payload = create_post_payload(title="new title", body="new body")

    response = post("/posts", json=payload)

    # Assert response status
    assert_status_code(response, 201)
    log_response_details(response)

    json_data = response.json()

    assert_post_creation_response(json_data, "new title", "new body")

    assert_response_time_under(response, 2)

    assert_content_type_json(response)

@pytest.mark.skip(reason="Skipping this test for now")
def test_create_post_with_missing_title():

    payload = create_post_payload(title="", body="new body")

    response = post("/posts", json=payload)

    # Assert response status
    assert_status_code(response, 201)

    log_response_details(response)

    json_data = response.json()

    assert_post_creation_response(json_data, "", "new body")

    assert_response_time_under(response, 2)

    assert_content_type_json(response)