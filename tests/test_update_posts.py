import pytest

from utils.api_helper import update_jph, logger
from utils.assertions import assert_status_code


@pytest.mark.skip(reason="Skipping this test for now")
def test_update_post_by_id():
    payload = {

  "title": "updated title",
  "body": "updated body"
}

    response = update_jph("/posts/1", json=payload)

    # Assert response status
    assert_status_code(response, 200)

    logger.info(f"URL: {response.request.url}")
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {response.text}")

    json_data = response.json()
    assert json_data["title"] == "updated title"
    assert json_data["body"] == "updated body"
    assert "id" in json_data

@pytest.mark.skip(reason="Skipping this test for now")
def test_update_post_with_invalid_id():
    payload = {
  "title": "title updated",
  "body": "quia et recusandae consequuntur expedita et cum"
}

    response = update_jph("/posts/1111", json=payload)

    # Assert response status
    assert_status_code(response, 200)

    logger.info(f"URL: {response.request.url}")
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {response.text}")

@pytest.mark.skip(reason="Skipping this test for now")
def test_update_post_empty_payload():
    payload = {}

    response = update_jph("/posts/1", json=payload)

    # Assert response status
    assert_status_code(response, 200)

    logger.info(f"URL: {response.request.url}")
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {response.text}")

    json_data = response.json()
    assert "id" in json_data
    assert len(json_data) == 1


@pytest.mark.skip(reason="Skipping this test for now")
def test_update_post_invalid_field_type():
    payload = {
        "title": True, # invalid field type
        "body": "quia et recusandae consequuntur expedita et cum"
    }

    response = update_jph("/posts/1", json=payload)

    # Assert response status
    assert_status_code(response, 422)

    logger.info(f"URL: {response.request.url}")
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {response.text}")

