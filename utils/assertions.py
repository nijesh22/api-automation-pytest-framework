from utils.api_helper import logger

def assert_status_code(response, expected_code):
    assert response.status_code == expected_code, \
        f"Expected {expected_code}, got {response.status_code}"

def assert_response_key_exists(response, key):
    json_data = response.json()
    assert key in json_data, f"Key '{key}' not found in response"

def assert_empty_response(response):
    assert response.json() == {}, "Expected empty JSON response for invalid user ID"

def assert_empty_list_response(response):
    assert isinstance(response.json(), list), "Expected list"
    assert len(response.json()) == 0, "Expected empty list in response"

def assert_content_type_json(response):
    content_type = response.headers.get("Content-Type", "")
    assert content_type.startswith("application/json"), \
        f"Expected JSON, but got: {content_type}"
    logger.info("Content Type Verified Successfully")


def assert_response_time_under(response, max_seconds=2):

    response_time = response.elapsed.total_seconds()
    assert response_time < max_seconds, \
        f"⚠️ Response time too high: {response_time:.2f}s"

    logger.info(f"✅ Response time OK: {response_time:.2f}s")

def assert_post_creation_response(json_data, expected_title, expected_body):

    assert "id" in json_data, "Missing 'id' in response"
    assert json_data["title"] == expected_title, f"Title mismatch. Expected: {expected_title}"
    assert json_data["body"] == expected_body, f"Body mismatch. Expected: {expected_body}"
    assert "createdAt" in json_data, "Missing 'createdAt' in response"

def assert_comment_schema(comment):

    assert "postId" in comment, "Missing key: postId"
    assert "id" in comment, "Missing key: id"
    assert "name" in comment, "Missing key: name"
    assert "email" in comment, "Missing key: email"
    assert "body" in comment, "Missing key: body"

def assert_list_response(json_data, empty_msg="Expected non-empty list", type_msg="Expected a list"):

    assert isinstance(json_data, list), type_msg
    assert len(json_data) > 0, empty_msg
    logger.info(f"✅ Total items received: {len(json_data)}")


def assert_user_update_response(json_data, expected_name, expected_job, check_updated_at=True):

    assert json_data["name"] == expected_name, f"Expected name '{expected_name}', got '{json_data.get('name')}'"
    assert json_data["job"] == expected_job, f"Expected job '{expected_job}', got '{json_data.get('job')}'"

    if check_updated_at:
        assert "updatedAt" in json_data, "Expected 'updatedAt' field in response"

def assert_user_creation_response(json_data, expected_name, expected_job):

    logger.info(f"✅ Created User: {json_data}")

    assert "id" in json_data, "Missing 'id' in response"
    assert json_data["name"] == expected_name, f"Expected name '{expected_name}', got '{json_data.get('name')}'"
    assert json_data["job"] == expected_job, f"Expected job '{expected_job}', got '{json_data.get('job')}'"
    assert "createdAt" in json_data, "Missing 'createdAt' in response"

def assert_empty_list_response_0(json_data, label="items"):

    assert isinstance(json_data, list), f"Expected a list of {label}"
    assert len(json_data) == 0, f"Expected no {label}, but got {len(json_data)}"
    logger.info(f"✅ No {label} found as expected")

def assert_user_fields(json_data, expected_name=None, expected_job=None):
    logger.info(f"Created User data with empty job name : {json_data}")
    if expected_name is not None:
        assert json_data["name"] == expected_name, f"Expected name '{expected_name}', got '{json_data.get('name')}'"
    else:
        assert "name" not in json_data, "Name should not be in response"

    if expected_job is not None:
        assert json_data["job"] == expected_job, f"Expected job '{expected_job}', got '{json_data.get('job')}'"
    else:
        assert "job" not in json_data, "Job should not be in response"




