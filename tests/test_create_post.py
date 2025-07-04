import pytest

from utils.api_helper import post, logger
from utils.assertions import assert_status_code


@pytest.mark.skip(reason="Skipping this test for now")
def test_create_post_with_title_and_body():
    payload = {

    "title": "new title",
    "body": "new body"
  }

    response = post("/posts", json=payload)

    # Assert response status
    assert_status_code(response, 201)

    logger.info(f"URL: {response.request.url}")
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {response.text}")

    json_data = response.json()
    assert "id" in json_data
    assert json_data["title"] == "new title"
    assert json_data["body"] == "new body"
    assert "createdAt" in json_data

@pytest.mark.skip(reason="Skipping this test for now")
def test_create_post_with_missing_title():
    payload = {

    "title": "",
    "body": "new body"
  }

    response = post("/posts", json=payload)

    # Assert response status
    assert_status_code(response, 201)

    logger.info(f"URL: {response.request.url}")
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {response.text}")

    json_data = response.json()
    assert "id" in json_data
    assert json_data["title"] == ""
    assert json_data["body"] == "new body"
    assert "createdAt" in json_data