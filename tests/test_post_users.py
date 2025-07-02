import pytest
from utils.api_helper import post
from utils.assertions import assert_status_code
from utils.logger import Logger

logger = Logger.get_logger()

@pytest.mark.skip(reason="Skipping this test for now")
def test_create_user_with_valid_data():


    payload = {
        "name": "John",
        "job": "QA Engineer"
    }

    response = post("/users", json=payload)

    # Assert response status
    assert_status_code(response, 201)

    # Assert keys exist
    json_data = response.json()
    logger.info(f"Created User : {json_data}")
    assert "id" in json_data
    assert json_data["name"] == "John"
    assert json_data["job"] == "QA Engineer"
    assert "createdAt" in json_data

@pytest.mark.skip(reason="Skipping this test for now")
def test_create_user_with_empty_name():

    payload = {
        "name": "",
        "job": "QA Engineer"
    }

    response = post("/users", json=payload)

    # Assert response status
    assert_status_code(response, 201)

    # Assert keys exist
    json_data = response.json()
    logger.info(f"Created User data with empty name : {json_data}")
    assert json_data["name"] == "" , "expected name to be empty"

@pytest.mark.skip(reason="Skipping this test for now")
def test_create_user_with_empty_job():


    payload = {
        "name": "niju mannuel",
        "job": ""
    }

    response = post("/users", json=payload)

    # Assert response status
    assert_status_code(response, 201)

    # Assert keys exist
    json_data = response.json()
    logger.info(f"Created User data with empty job name : {json_data}")
    assert  json_data["job"] == "", "expected job to be empty"

@pytest.mark.skip(reason="Skipping this test for now")
def test_create_with_empty_payload():

    payload = {}

    response = post("/users", json=payload)

    # Assert response status
    assert_status_code(response, 201)

    # Assert keys exist
    json_data = response.json()
    logger.info(f"Created User data with empty job name : {json_data}")
    assert "id" in json_data
    assert "createdAt" in json_data

    assert "name" not in json_data
    assert "job" not in json_data

@pytest.mark.skip(reason="Skipping this test for now")
def test_create_user_with_long_name_and_job():

    payload = {
        "name": "Niju Mannuel " * 20,  # ~260+ characters
        "job": "Senior Lead Principal Architect Automation Expert DevOps Cloud Specialist " * 5  # ~350+ characters
    }

    response = post("/users", json=payload)

    # Assert response status
    assert_status_code(response, 201)

    # Assert keys exist
    json_data = response.json()
    logger.info(f"Created User data with empty job name : {json_data}")
    assert  json_data["name"] == "Niju Mannuel " * 20, "name is different"
    assert json_data["job"] == "Senior Lead Principal Architect Automation Expert DevOps Cloud Specialist " * 5 , "expected job name is different"

#@pytest.mark.skip(reason="Skipping this test for now")
def test_create_user_with_special_characters():


    payload = {
        "name": "John@@@",
        "job": "QA Engineer/@*"
    }

    response = post("/users", json=payload)

    # Assert response status
    assert_status_code(response, 201)

    # Assert keys exist
    json_data = response.json()
    logger.info(f"Created User : {json_data}")
    assert "id" in json_data
    assert json_data["name"] == "John@@@"
    assert json_data["job"] == "QA Engineer/@*"
    assert "createdAt" in json_data