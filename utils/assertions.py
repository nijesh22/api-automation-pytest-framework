

def assert_status_code(response, expected_code):
    assert response.status_code == expected_code, \
        f"Expected {expected_code}, got {response.status_code}"

def assert_response_key_exists(response, key):
    json_data = response.json()
    assert key in json_data, f"Key '{key}' not found in response"
