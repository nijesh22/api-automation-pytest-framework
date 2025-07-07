import pytest

from utils.api_helper import update, delete, logger, delete_jph
from utils.assertions import assert_status_code, assert_response_time_under
from utils.logs import log_response_details


@pytest.mark.skip(reason="Skipping this test for now")
def test_delete_user_with_valid_id():

    response = delete("/users/2")
    assert_status_code(response, 204)

    log_response_details(response, log_body=False)

    assert_response_time_under(response, 2)


@pytest.mark.skip(reason="Skipping this test for now")
def test_delete_user_with_invalid_id():

    response = delete("/users/2")
    assert_status_code(response, 204)

    log_response_details(response, log_body=False)

    assert_response_time_under(response, 2)

@pytest.mark.skip(reason="Skipping this test for now")
def test_delete_user_twice():

    #delete user once
    response_1 = delete("/users/2")
    assert_status_code(response_1, 204)

    log_response_details(response_1, log_body=False)


    #delete user twice
    response_2 = delete("/users/2")
    assert_status_code(response_2, [204, 404])

    log_response_details(response_2, log_body=False)

    assert_response_time_under(response_1, 2)
    assert_response_time_under(response_2, 2)

@pytest.mark.skip(reason="Skipping this test for now")
def test_delete_post():

    response = delete_jph("/posts/1")
    assert_status_code(response, 204)


    log_response_details(response, log_body=False)

    assert_response_time_under(response, 2)

@pytest.mark.skip(reason="Skipping this test for now")
def test_delete_non_existent_post():

    response = delete_jph("/posts/111111")
    assert_status_code(response, 404)

    log_response_details(response, log_body=False)
    assert_response_time_under(response, 2)






