

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
