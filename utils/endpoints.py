import allure
from utils.api_helper import get, get_post

@allure.step("Send GET /users with page={page}")
def get_users_by_page(page=None):
    params = {"page": page} if page is not None else {}
    response = get("/users", params=params)
    allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)
    return response

@allure.step("Send GET /users with id={user_id}")
def get_users_by_valid_id(user_id):
    response = get("/users", params={"id": user_id})
    allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)
    return response

@allure.step("Get post by ID with id={ids}")
def get_post_by_id(ids):
    response = get_post("/posts", params={"id": ids})
    allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)
    return response

@allure.step("Get posts filter with userId = {userId}")
def get_post_filter_with_userid(userId):
    response = get_post("/posts", params={"userId": userId})
    allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)
    return response