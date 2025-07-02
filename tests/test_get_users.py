import pytest

from utils.assertions import assert_status_code, assert_response_key_exists, assert_empty_response
from utils.endpoints import get_users_by_page, get_users_by_valid_id

@pytest.mark.skip(reason="Skipping this test for now")
def test_get_users_page_1():
   response = get_users_by_page(1)
   assert_status_code(response, 200)
   assert_response_key_exists(response, "data")

@pytest.mark.skip(reason="Skipping this test for now")
def test_get_users_page_2():
   response = get_users_by_page(2)
   assert_status_code(response, 200)
   assert_response_key_exists(response, "data")

@pytest.mark.skip(reason="Skipping this test for now")
def test_get_users_valid_id():
   response = get_users_by_valid_id(2)
   assert_status_code(response, 200)
   assert_response_key_exists(response, "data")

@pytest.mark.skip(reason="Skipping this test for now")
def test_get_users_invalid_id():
   response = get_users_by_valid_id(35)
   assert_status_code(response, 404)
   assert_empty_response(response)

@pytest.mark.skip(reason="Skipping this test for now")
def test_get_users_without_param():
   response = get_users_by_page()
   assert_status_code(response, 200)
   assert_response_key_exists(response, "data")

@pytest.mark.skip(reason="Skipping this test for now")
def test_get_users_non_numeric_param():
   response = get_users_by_page('abc')
   assert response.json().get("page") == 1
   assert_status_code(response, 200)
   assert_response_key_exists(response, "data")

