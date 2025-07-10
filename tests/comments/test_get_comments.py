import pytest
from utils.api_helper import get_post
from utils.assertions import assert_status_code, assert_content_type_json, assert_response_time_under, \
    assert_comment_schema, assert_list_response, assert_empty_list_response_0
from utils.logger import Logger

logger = Logger.get_logger()

##@pytest.mark.skip(reason="Skipping this test for now")
def test_get_all_comments():
   response = get_post("/comments")
   assert_status_code(response, 200)
   for comment in response.json():
       assert_comment_schema(comment)

   assert_response_time_under(response, 2)

   assert_content_type_json(response)


##@pytest.mark.skip(reason="Skipping this test for now")
def test_get_comments_by_id():
    response = get_post("/comments/1")
    assert_status_code(response, 200)
    comment = response.json()
    assert_comment_schema(comment)

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

# #@pytest.mark.skip(reason="Skipping this test for now")
def test_get_comments_by_post_id():
    response = get_post("/comments?postId=1")
    assert_status_code(response, 200)
    json_data = response.json()
    assert_list_response(json_data, empty_msg="Expected at least one post id", type_msg="Expected a list of post id")

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

# #@pytest.mark.skip(reason="Skipping this test for now")
def test_get_comments_by_invalid_post_id():
    response = get_post("/comments?postId=111")
    assert_status_code(response, 200)
    json_body = response.json()

    assert_empty_list_response_0(json_body, label="comments")

    assert_response_time_under(response, 2)
    assert_content_type_json(response)


# #@pytest.mark.skip(reason="Skipping this test for now")
def test_get_comments_by_large_post_id():
    response = get_post("/comments?postId=100")
    assert_status_code(response, 200)
    json_data = response.json()
    assert_list_response(json_data, empty_msg="Expected at least one comment for postId=100", type_msg="Expected a list of comments")

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

#@pytest.mark.skip(reason="Skipping this test for now")
def test_get_comments_non_integer_id():
    response = get_post("/comments/abc")
    assert_status_code(response, 404)

    assert_response_time_under(response, 2)
    assert_content_type_json(response)

