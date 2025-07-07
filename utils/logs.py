from utils.api_helper import logger


def log_response_details(response, log_url=True, log_status=True, log_body=True):

    if log_url:
        logger.info(f"URL: {response.request.url}")
    if log_status:
        logger.info(f"Status Code: {response.status_code}")
    if log_body:
        logger.info(f"Response: {response.text}")
