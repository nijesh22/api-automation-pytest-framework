import allure
from utils.api_helper import get

@allure.step("Send GET /users with page={page}")
def get_users_by_page(page):
    response = get("/users", params={"page": page})
    allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)
    return response