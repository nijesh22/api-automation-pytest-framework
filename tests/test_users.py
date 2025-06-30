from utils.assertions import assert_status_code, assert_response_key_exists
from utils.endpoints import get_users_by_page


def test_get_users_page_1():

   response = get_users_by_page(1)
   assert_status_code(response, 200)
   assert_response_key_exists(response, "data")