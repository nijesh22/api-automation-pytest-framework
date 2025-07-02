import pytest

from utils.api_helper import get_post
from utils.assertions import assert_status_code
from utils.logger import Logger

logger = Logger.get_logger()

@pytest.mark.skip(reason="Skipping this test for now")
def test_get_all_comments():
   response = get_post("/comments")
   assert_status_code(response, 200)
   for comment in response.json():
       assert "postId" in comment
       assert "id" in comment
       assert "name" in comment
       assert "email" in comment
       assert "body" in comment


@pytest.mark.skip(reason="Skipping this test for now")
def test_get_comments_by_id():
    response = get_post("/comments/1")
    assert_status_code(response, 200)
    comment = response.json()
    assert "postId" in comment
    assert "id" in comment
    assert "name" in comment
    assert "email" in comment
    assert "body" in comment

@pytest.mark.skip(reason="Skipping this test for now")
def test_get_comments_by_post_id():
    response = get_post("/comments?postId=1")
    assert_status_code(response, 200)
    json_data = response.json()
    assert isinstance(json_data, list), "Expected a list of post id"
    assert len(json_data) > 0, "Expected at least one post id"
    logger.info(f"Total post id received: {len(json_data)}")

@pytest.mark.skip(reason="Skipping this test for now")
def test_get_comments_by_invalid_post_id():
    response = get_post("/comments?postId=111")
    assert_status_code(response, 200)
    json_body = response.json()
    assert isinstance(json_body, list), "Expected a list of post id"
    assert len(json_body) == 0, "Expected no comments for invalid postId"


@pytest.mark.skip(reason="Skipping this test for now")
def test_get_comments_by_large_post_id():
    response = get_post("/comments?postId=100")
    assert_status_code(response, 200)
    json_data = response.json()
    assert isinstance(json_data, list), "Expected a list of comments"
    assert len(json_data) > 0, "Expected at least one comment for postId=100"
    logger.info(f"Total comments received for postId=100 : {len(json_data)}")

@pytest.mark.skip(reason="Skipping this test for now")
def test_get_comments_non_integer_id():
    response = get_post("/comments/abc")
    assert_status_code(response, 404)

