import pytest
from utils.api_helper import post
from utils.assertions import assert_status_code, assert_content_type_json, assert_response_time_under, \
    assert_user_creation_response, assert_user_fields
from utils.logger import Logger
from utils.payloads import create_user_payload

logger = Logger.get_logger()

#@pytest.mark.skip(reason="Skipping this test for now")
def test_create_user_with_valid_data():

    payload = create_user_payload("John", "QA Engineer")

    response = post("/users", json=payload)

    assert_status_code(response, 201)

    json_data = response.json()

    assert_user_creation_response(json_data, "John", "QA Engineer")

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

#@pytest.mark.skip(reason="Skipping this test for now")
def test_create_user_with_empty_name():

    payload = create_user_payload("", "QA Engineer")

    response = post("/users", json=payload)

    assert_status_code(response, 201)

    json_data = response.json()
    assert_user_fields(json_data, "", "QA Engineer")

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

#@pytest.mark.skip(reason="Skipping this test for now")
def test_create_user_with_empty_job():

    payload = create_user_payload("niju mannuel", "")

    response = post("/users", json=payload)

    assert_status_code(response, 201)

    json_data = response.json()

    assert_user_fields(json_data, "niju mannuel", "")

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

#@pytest.mark.skip(reason="Skipping this test for now")
def test_create_with_empty_payload():

    payload = {}

    response = post("/users", json=payload)

    assert_status_code(response, 201)

    json_data = response.json()
    logger.info(f"Created User data with empty job name : {json_data}")
    assert "id" in json_data
    assert "createdAt" in json_data

    assert "name" not in json_data
    assert "job" not in json_data

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

#@pytest.mark.skip(reason="Skipping this test for now")
def test_create_user_with_long_name_and_job():

    payload = create_user_payload("Niju Mannuel " * 20, "Senior Lead Principal Architect Automation Expert DevOps Cloud Specialist " * 5)

    response = post("/users", json=payload)

    assert_status_code(response, 201)

    json_data = response.json()

    assert_user_fields(json_data, "Niju Mannuel " * 20, "Senior Lead Principal Architect Automation Expert DevOps Cloud Specialist " * 5)

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

#@pytest.mark.skip(reason="Skipping this test for now")
def test_create_user_with_special_characters():

    payload = create_user_payload("John@@@", "QA Engineer/@*")

    response = post("/users", json=payload)

    assert_status_code(response, 201)

    json_data = response.json()

    assert_user_creation_response(json_data, "John@@@", "QA Engineer/@*")

    assert_response_time_under(response, 2)
    assert_content_type_json(response)