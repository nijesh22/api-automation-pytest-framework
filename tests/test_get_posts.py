import pytest
from utils.api_helper import get_post
from utils.assertions import assert_status_code, assert_response_key_exists, assert_empty_response, \
   assert_empty_list_response, assert_content_type_json, assert_response_time_under
from utils.endpoints import get_post_by_id, get_post_filter_with_userid
from utils.logger import Logger

logger = Logger.get_logger()

@pytest.mark.skip(reason="Skipping this test for now")
def test_get_post_by_id():
   response = get_post_by_id(1)
   json_body = response.json()
   assert isinstance(json_body, list), "Expected response to be a list"
   assert len(json_body) > 0, "Expected at least one item in the list"

   post = json_body[0]  # ✅ this is the actual post dictionary
   assert post["id"] == 1
   assert "title" in post
   assert "body" in post
   assert_status_code(response, 200)

   assert_response_time_under(response, 2)
   assert_content_type_json(response)

@pytest.mark.skip(reason="Skipping this test for now")
def test_get_post_with_invalid_id():
   response = get_post_by_id(111)
   assert_empty_list_response(response)
   assert_status_code(response, 200)

   assert_response_time_under(response, 2)

   assert_content_type_json(response)

@pytest.mark.skip(reason="Skipping this test for now")
def test_get_post_direct_invalid_id():
   response = get_post("/posts/99999")  # no query param
   assert_status_code(response, 200)

   assert_response_time_under(response, 2)

   assert_content_type_json(response)

@pytest.mark.skip(reason="Skipping this test for now")
def test_get_posts():
   response = get_post("/posts")
   assert_status_code(response, 200)
   json_data = response.json()
   assert isinstance(json_data, list), "Expected a list of posts"
   assert len(json_data) > 0, "Expected at least one post"
   logger.info(f"Total posts received: {len(json_data)}")

   assert_response_time_under(response, 2)

   assert_content_type_json(response)

@pytest.mark.skip(reason="Skipping this test for now")
def test_get__posts_filter_userid():
   response = get_post_filter_with_userid(1)
   assert_status_code(response, 200)
   json_data = response.json()
   assert isinstance(json_data, list), "Expected a list of posts"
   assert len(json_data) > 0, "Expected at least one post"
   logger.info(f"Total posts received: {len(json_data)}")

   assert_response_time_under(response, 2)

   assert_content_type_json(response)